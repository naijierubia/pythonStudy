import torch
from torch.utils.tensorboard import SummaryWriter

# 写入logs文件
writer = SummaryWriter('logs')

# 需要为张量或者numpy数组
writer.add_image('input_image', torch.randn(1, 28, 28), dataformats='CHW')

for i in range(100):
    # title，y轴，x轴
    writer.add_scalar('y=x^2', i*i, i)

writer.close()

# tensorboard --logdir=logs --port 6007 启动