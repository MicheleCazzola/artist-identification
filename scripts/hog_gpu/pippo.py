import torch
import torch.nn.functional as F
import numpy as np
import torchvision
from skimage.feature import hog


def hog_custom(
    images: torch.Tensor,
    orientations: int = 9,
    pixels_per_cell: tuple = (8, 8),
    cells_per_block: tuple = (3, 3),
    block_norm: str = 'L2-Hys',
    visualize: bool = False,
    transform_sqrt: bool = False,
    feature_vector: bool = True,
    channel_axis: int = None,
):
    if channel_axis is not None:
        images = images.permute(0, 3, 1, 2)  # Move channels to the first dimension

    if transform_sqrt:
        images = torch.sqrt(images)

    if images.ndim == 4:
        g_row_by_ch = torch.empty_like(images)
        g_col_by_ch = torch.empty_like(images)
        g_magn = torch.empty_like(images)

        for idx_ch in range(images.shape[1]):
            g_row_by_ch[:, idx_ch], g_col_by_ch[:, idx_ch] = compute_channel_gradient(images[:, idx_ch])
            g_magn[:, idx_ch] = torch.hypot(g_row_by_ch[:, idx_ch], g_col_by_ch[:, idx_ch])

        idcs_max = g_magn.argmax(dim=1)
        g_row = g_row_by_ch[torch.arange(images.shape[0]).unsqueeze(1), idcs_max, torch.arange(images.shape[2]).unsqueeze(1), torch.arange(images.shape[3])]
        g_col = g_col_by_ch[torch.arange(images.shape[0]).unsqueeze(1), idcs_max, torch.arange(images.shape[2]).unsqueeze(1), torch.arange(images.shape[3])]
    else:
        g_row, g_col = compute_channel_gradient(images)

    s_row, s_col = images.shape[-2:]
    c_row, c_col = pixels_per_cell
    b_row, b_col = cells_per_block

    n_cells_row = s_row // c_row
    n_cells_col = s_col // c_col
    
    orientation_histogram = compute_hog_hist(
        g_col, g_row, c_col, c_row, s_col, s_row, n_cells_col, n_cells_row, orientations, images.shape[0]
    )

    n_blocks_row = (n_cells_row - b_row) + 1
    n_blocks_col = (n_cells_col - b_col) + 1
    if n_blocks_col <= 0 or n_blocks_row <= 0:
        min_row = b_row * c_row
        min_col = b_col * c_col
        raise ValueError(
            'The input image is too small given the values of '
            'pixels_per_cell and cells_per_block. '
            'It should have at least: '
            f'{min_row} rows and {min_col} cols.'
        )
    normalized_blocks = torch.zeros((images.shape[0], n_blocks_row, n_blocks_col, b_row, b_col, orientations), dtype=torch.float32)

    for r in range(n_blocks_row):
        for c in range(n_blocks_col):
            block = orientation_histogram[:, r:r + b_row, c:c + b_col, :]
            normalized_blocks[:, r, c, :] = normalize_block(block, method=block_norm)

    if feature_vector:
        normalized_blocks = normalized_blocks.view(images.shape[0], -1)

    if visualize:
        return normalized_blocks
    else:
        return normalized_blocks


def normalize_block(block, method: str, eps: float = 1e-5):
    if method == 'L1':
        out = block / (torch.sum(torch.abs(block), dim=(-1, -2, -3), keepdim=True) + eps)
    elif method == 'L1-sqrt':
        out = torch.sqrt(block / (torch.sum(torch.abs(block), dim=(-1, -2, -3), keepdim=True) + eps))
    elif method == 'L2':
        out = block / torch.sqrt(torch.sum(block**2, dim=(-1, -2, -3), keepdim=True) + eps**2)
    elif method == 'L2-Hys':
        out = block / torch.sqrt(torch.sum(block**2, dim=(-1, -2, -3), keepdim=True) + eps**2)
        out = torch.minimum(out, torch.tensor(0.2))
        out = out / torch.sqrt(torch.sum(out**2, dim=(-1, -2, -3), keepdim=True) + eps**2)
    else:
        raise ValueError('Selected block normalization method is invalid.')

    return out


def compute_channel_gradient(channel: torch.Tensor):
    g_row = torch.empty_like(channel)
    g_row[:, 0, :] = 0
    g_row[:, -1, :] = 0
    g_row[:, 1:-1, :] = channel[:, 2:, :] - channel[:, :-2, :]
    g_col = torch.empty_like(channel)
    g_col[:, :, 0] = 0
    g_col[:, :, -1] = 0
    g_col[:, :, 1:-1] = channel[:, :, 2:] - channel[:, :, :-2]

    return g_row, g_col


def compute_hog_hist(
    g_col: torch.Tensor, g_row: torch.Tensor, c_col: int, c_row: int, s_col: int, s_row: int, n_cells_col: int, n_cells_row: int, orientations: int, batch_size: int
):
    magnitude = torch.hypot(g_col, g_row)
    orientation = torch.atan2(g_row, g_col) * (180.0 / np.pi) % 180.0

    orientation_bin = (orientation * (orientations / 180.0)).long()
    orientation_bin[orientation_bin == orientations] = 0

    cell_magnitude = magnitude.unfold(1, c_row, c_row).unfold(2, c_col, c_col)
    cell_orientation_bin = orientation_bin.unfold(1, c_row, c_row).unfold(2, c_col, c_col)

    orientation_histogram = torch.zeros((batch_size, n_cells_row, n_cells_col, orientations), dtype=torch.float32)
    for o in range(orientations):
        mask = (cell_orientation_bin == o).float()
        hist = torch.sum(cell_magnitude * mask, dim=(-1, -2))
        orientation_histogram[:, :, :, o] = hist

    return orientation_histogram

if __name__ == '__main__':
    import cv2
    from PIL import Image
    
    tr = torchvision.transforms.Compose([
        torchvision.transforms.Resize((256, 256)),
        torchvision.transforms.RandomCrop((224, 224), pad_if_needed=True)
    ])

    path = './scripts/hog_gpu/adriaen-van-ostade_a-fight-1.jpg'
    im = Image.open(open(path, 'rb')).convert('RGB')
    print(im.size)
    x = torchvision.transforms.Compose([
        torchvision.transforms.ToTensor(),
        torchvision.transforms.Resize((256, 256)),
        torchvision.transforms.RandomCrop((224, 224), pad_if_needed=True)
    ])(im).unsqueeze(0)
    
    print(x.shape)
    # im = torch.randn(8, 3, 514, 611)
    
    DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'
    
    # print(im.shape)

    # x: torch.Tensor = tr(im)
    
    print(x.shape)
    
    x = x.permute(0, 2, 3, 1)
    gray_custom = lambda img: 0.299 * img[:, :, :, 0] + 0.587 * img[:, :, :, 1] + 0.114 * img[:, :, :, 2]
    y_custom = hog_custom(gray_custom(x).to(DEVICE), orientations=6, pixels_per_cell=(16, 16), cells_per_block=(2,2), block_norm='L2-Hys')
    
    gray = lambda img: 0.299 * img[:, :, 0] + 0.587 * img[:, :, 1] + 0.114 * img[:, :, 2]
    y = np.array([
        hog(gray(x_b), orientations=6, pixels_per_cell=(16, 16), cells_per_block=(2,2), block_norm='L2-Hys')
        for x_b in x.numpy()
    ])
    print(y_custom.shape)
    print(y.shape)
    
    cosine_similarity = F.cosine_similarity(y_custom, torch.tensor(y))
    print(cosine_similarity)
