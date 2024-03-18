import torch
from torch.utils.tensorboard import SummaryWriter
writer = SummaryWriter()

# 创建输入数据x，范围从-5到5，步长为0.1
x = torch.arange(-5, 5, 0.1).view(-1, 1)
# 创建输入数据y，范围从-5到5，步长为0.1
y = -5 * x + 0.1 * torch.randn(x.size())

# 创建模型，线性回归模型，输入维度为1，输出维度为1
model = torch.nn.Linear(1, 1)
# 创建损失函数，均方误差损失函数
criterion = torch.nn.MSELoss()
# 创建优化器，使用随机梯度下降优化器，学习率为0.1
optimizer = torch.optim.SGD(model.parameters(), lr = 0.1)

# 定义训练函数
def train_model(iter):
    # 循环iter次，每次循环epoch次
    for epoch in range(iter):
        # 计算模型输出
        y1 = model(x)
        # 计算损失
        loss = criterion(y1, y)
        # 将损失添加到tensorboard中
        writer.add_scalar("Loss/train", loss, epoch)
        # 梯度归零
        optimizer.zero_grad()
        # 反向传播
        loss.backward()
        # 梯度更新
        optimizer.step()

# 调用训练函数，训练10次
train_model(100)
# 将tensorboard中的内容写入文件
writer.flush()