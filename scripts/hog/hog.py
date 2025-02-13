from matplotlib import pyplot as plt
import torch
import torch.nn as nn
import torch.nn.functional as F
import math
import time

import torchvision


def timeit(x, func, iter=10):
	torch.cuda.synchronize()
	start = time.time()
	for _ in range(iter):
		y = func(x)
	torch.cuda.synchronize()
	runtime = (time.time()-start)/iter
	return runtime

class HOGLayer_previous(nn.Module):
    def __init__(self, nbins=10, pool=8, max_angle=math.pi, stride=1, padding=1, dilation=1):
        super(HOGLayer_previous, self).__init__()
        self.nbins = nbins
        self.stride = stride
        self.padding = padding
        self.dilation = dilation
        self.pool = pool
        self.max_angle = max_angle
        mat = torch.FloatTensor([[1, 0, -1],
                                 [2, 0, -2],
                                 [1, 0, -1]])
        mat = torch.cat((mat[None], mat.t()[None]), dim=0)
        self.register_buffer("weight", mat[:,None,:,:])
        self.pooler = nn.AvgPool2d(pool, stride=pool, padding=0, ceil_mode=False, count_include_pad=True)

    def forward(self, x):
        with torch.no_grad():
            gxy = F.conv2d(x, self.weight, None, self.stride,
                            self.padding, self.dilation, 1)
            #2. Mag/ Phase
            mag = gxy.norm(dim=1)
            norm = mag[:,None,:,:]
            phase = torch.atan2(gxy[:,0,:,:], gxy[:,1,:,:])

            #3. Binning Mag with linear interpolation
            phase_int = phase / self.max_angle * self.nbins
            phase_int = phase_int[:,None,:,:]

            n, c, h, w = gxy.shape
            out = torch.zeros((n, self.nbins, h, w), dtype=torch.float, device=gxy.device)
            out.scatter_(1, phase_int.floor().long()%self.nbins, norm)
            out.scatter_add_(1, phase_int.ceil().long()%self.nbins, 1 - norm)

            return self.pooler(out)




class HOGLayerMoreComplicated(nn.Module):
    def __init__(self, nbins, pool, max_angle=math.pi, stride=1, padding=1, dilation=1,
                 mean_in=False, max_out=False):
        super(HOGLayerMoreComplicated, self).__init__()
        self.nbins = nbins
        self.stride = stride
        self.padding = padding
        self.dilation = dilation
        self.pool = pool
        self.max_angle = max_angle
        self.max_out = max_out
        self.mean_in = mean_in

        mat = torch.FloatTensor([[1, 0, -1],
                                 [2, 0, -2],
                                 [1, 0, -1]])
        mat = torch.cat((mat[None], mat.t()[None]), dim=0)
        self.register_buffer("weight", mat[:,None,:,:])
        self.pooler = nn.AvgPool2d(pool, stride=pool, padding=0, ceil_mode=False, count_include_pad=True)

    def forward(self, x):
        if self.mean_in:
            return self.forward_v1(x)
        else:
            return self.forward_v2(x)

    def forward_v1(self, x):
        if x.size(1) > 1:
            x = x.mean(dim=1)[:,None,:,:]

        gxy = F.conv2d(x, self.weight, None, self.stride,
                       self.padding, self.dilation, 1)
        # 2. Mag/ Phase
        mag = gxy.norm(dim=1)
        norm = mag[:, None, :, :]
        phase = torch.atan2(gxy[:, 0, :, :], gxy[:, 1, :, :])

        # 3. Binning Mag with linear interpolation
        phase_int = phase / self.max_angle * self.nbins
        phase_int = phase_int[:, None, :, :]

        n, c, h, w = gxy.shape
        out = torch.zeros((n, self.nbins, h, w), dtype=torch.float, device=gxy.device)
        out.scatter_(1, phase_int.floor().long() % self.nbins, norm)
        out.scatter_add_(1, phase_int.ceil().long() % self.nbins, 1 - norm)

        return self.pooler(out)

    def forward_v2(self, x):
        batch_size, in_channels, height, width = x.shape
        weight = self.weight.repeat(3, 1, 1, 1)
        gxy = F.conv2d(x, weight, None, self.stride,
                        self.padding, self.dilation, groups=in_channels)

        gxy = gxy.view(batch_size, in_channels, 2, height, width)

        if self.max_out:
            gxy = gxy.max(dim=1)[0][:,None,:,:,:]

        #2. Mag/ Phase
        mags = gxy.norm(dim=2)
        norms = mags[:,:,None,:,:]
        phases = torch.atan2(gxy[:,:,0,:,:], gxy[:,:,1,:,:])

        #3. Binning Mag with linear interpolation
        phases_int = phases / self.max_angle * self.nbins
        phases_int = phases_int[:,:,None,:,:]

        out = torch.zeros((batch_size, in_channels, self.nbins, height, width),
                          dtype=torch.float, device=gxy.device)
        out.scatter_(2, phases_int.floor().long()%self.nbins, norms)
        out.scatter_add_(2, phases_int.ceil().long()%self.nbins, 1 - norms)

        out = out.view(batch_size, in_channels * self.nbins, height, width)
        out = torch.cat((self.pooler(out), self.pooler(x)), dim=1)

        return out
    

class HOGLayer(nn.Module):
    def __init__(self, orientations, pixels_per_cell, cells_per_block, block_norm, transform_sqrt=False, feature_vector=True, visualize=False):
        super(HOGLayer, self).__init__()
        self.orientations = orientations
        self.pixels_per_cell = pixels_per_cell
        self.cells_per_block = cells_per_block
        self.block_norm = block_norm
        self.transform_sqrt = transform_sqrt
        self.feature_vector = feature_vector
        self.visualize = visualize

        # Sobel filter for gradient computation
        mat = torch.FloatTensor([[1, 0, -1],
                                 [2, 0, -2],
                                 [1, 0, -1]])
        mat = torch.cat((mat[None], mat.t()[None]), dim=0)
        self.register_buffer("weight", mat[:, None, :, :])
        
    def _hog_channel_gradient(channel):
        g_row = torch.empty(channel.shape, dtype=channel.dtype)
        g_row[0, :] = 0
        g_row[-1, :] = 0
        g_row[1:-1, :] = channel[2:, :] - channel[:-2, :]
        g_col = torch.empty(channel.shape, dtype=channel.dtype)
        g_col[:, 0] = 0
        g_col[:, -1] = 0
        g_col[:, 1:-1] = channel[:, 2:] - channel[:, :-2]

        return g_row, g_col
    
    def forward_bis(self, x: torch.Tensor):
        
        g_row, g_col = self._hog_channel_gradient(x)
        
        s_row, s_col = x.size(2), x.size(3)
        c_row, c_col = self.pixels_per_cell
        b_row, b_col = self.cells_per_block

        n_cells_row = int(s_row // c_row)  # number of cells along row-axis
        n_cells_col = int(s_col // c_col)  # number of cells along col-axis

        # compute orientations integral images
        orientation_histogram = torch.zeros(
            (n_cells_row, n_cells_col, self.orientations), dtype=float
        )
        g_row = g_row.astype(float, copy=False)
        g_col = g_col.astype(float, copy=False)
        

    def forward(self, x):
        with torch.no_grad():
            if self.transform_sqrt:
                x = torch.sqrt(x)

            # Compute gradients
            gxy = F.conv2d(x, self.weight, stride=1, padding=1)
            mag = gxy.norm(dim=1)
            phase = torch.atan2(gxy[:, 0, :, :], gxy[:, 1, :, :])

            # Quantize phase into bins
            phase_int = phase / math.pi * self.orientations
            phase_int = phase_int[:, None, :, :]

            n, h, w = x.shape[0], x.shape[2], x.shape[3]
            out = torch.zeros((n, self.orientations, h, w), dtype=torch.float, device=gxy.device)
            out.scatter_(1, phase_int.floor().long() % self.orientations, mag[:, None, :, :])
            out.scatter_add_(1, phase_int.ceil().long() % self.orientations, mag[:, None, :, :])

            # Pooling
            pooled = F.avg_pool2d(out, self.pixels_per_cell, stride=self.pixels_per_cell)

            if self.feature_vector:
                return pooled.view(n, -1)
            else:
                return pooled


if __name__ == '__main__':
    import cv2
    
    tr = torchvision.transforms.Compose([
        torchvision.transforms.ToTensor(),
        torchvision.transforms.Resize((256, 256)),
        torchvision.transforms.RandomCrop((224, 224), pad_if_needed=True)
    ])

    path = './scripts/hog_gpu/adriaen-van-ostade_a-fight-1.jpg'
    im = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    
    print(im.shape)

    x = tr(im)[None]
    
    print(x.shape)

    hog = HOGLayer(orientations=6, pixels_per_cell=(16, 16), cells_per_block=(2,2), block_norm='L2-Hys')
    y = hog(x)

    print(y.shape)