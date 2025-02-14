from torch.optim.lr_scheduler import _LRScheduler

class CustomMultiStepLR(_LRScheduler):
    def __init__(self, optimizer, milestones, factors, last_epoch=-1):
        """
        Custom multi-step LR scheduler with different gamma values for each step.

        Args:
            optimizer (Optimizer): Wrapped optimizer.
            milestones (list): List of epoch indices at which to adjust the learning rate.
            factors (list): List of gamma values for each milestone. Must be the same length as milestones.
            last_epoch (int): The index of the last epoch. Defaults to -1 (starts from epoch 0).
        """
        assert len(milestones) == len(factors), "Milestones and gammas must have the same length."
        self.milestones = milestones
        self.gammas = factors
        super().__init__(optimizer, last_epoch)

    def get_lr(self):
        """Calculate the learning rate for the current epoch."""
        factor = 1.0
        for milestone, gamma in zip(self.milestones, self.gammas):
            if self.last_epoch >= milestone:
                factor *= gamma
        return [base_lr * factor for base_lr in self.base_lrs]
    
    
if __name__ == '__main__':
    import torch
    import torch.optim as optim

    # Define model, optimizer, and scheduler
    model = torch.nn.Linear(1, 1)
    optimizer = optim.Adam(model.parameters(), lr=0.1, weight_decay=1e-4)
    scheduler = CustomMultiStepLR(optimizer, milestones=[2, 4], factors=[0.1, 0.5])

    # Print learning rate for each epoch
    for epoch in range(5):
        scheduler.step()
        print(f"Epoch {epoch}: LR: {scheduler.get_lr()[0]} == {optimizer.param_groups[0]['lr']}")