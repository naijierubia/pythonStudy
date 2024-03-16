# pytorch入门

## 数据集制作

```py
from torch.utils.data import Dataset,DataLoader
import torchvision.transforms as transforms


class CustomDataset(Dataset):
    def __init__(self, data, labels, transform=None):
        self.data = data
        self.labels = labels
        self.transform = transform

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        image = self.data[idx]
        label = self.labels[idx]
        if self.transform:
            image = self.transform(image)
        return image, label


# 假设您已经有一个包含图像和标签的列表
images = [...]
labels = [...]

# 定义数据增强（可选）
transform = transforms.Compose(
    [
        transforms.Resize((32, 32)),
        transforms.ToTensor(),
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
    ]
)

# 创建数据集实例
dataset = CustomDataset(images, labels, transform=transform)

```

## 数据集加载

```py
DataLoader(dataset, batch_size=1, shuffle=None, sampler=None, batch_sampler=None, num_workers=0, collate_fn=None, pin_memory=False, drop_last=False, timeout=0, worker_init_fn=None, multiprocessing_context=None, generator=None, *, prefetch_factor=None, persistent_workers=False, pin_memory_device='cuda')
```

其中：

1. dataset：数据集，必须是PyTorch中的Dataset对象。
2. batch_size：每个小批量的样本数量。
3. shuffle：是否在每个epoch之后打乱数据。在训练神经网络时，通常需要设置shuffle为True，以便网络在训练过程中看到不同的数据样本。
4. num_workers：用于数据加载的线程数量。如果您的系统支持多线程，可以设置num_workers大于1，以加快数据加载速度。但是，请注意，过多的线程可能会导致内存不足。
5. collate_fn：用于将多个数据样本组合成一个批量的函数。PyTorch提供了默认的函数，通常不需要修改。
6. pin_memory：是否将数据加载到固定内存中，以加快数据传输速度。如果您的数据集很大，可以设置pin_memory为True。
7. drop_last：是否抛弃最后一个不完整的批量。如果您的数据集的大小不能被batch_size整除，设置drop_last为True可以确保每个epoch的批量数量是固定的。

例如，以下代码创建了一个DataLoader对象，其中 batch size为32，每个epoch后打乱数据，使用4个线程加载数据，并将数据加载到固定内存中：

## nn.Module骨架

```py
import torch
import torch.nn as nn

class NeuralNetwork(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        # 需要初始化父类
        super(NeuralNetwork, self).__init__()
        # 定义网络结构

        """
        self.hidden = nn.Linear(input_size, hidden_size)  
        self.relu = nn.ReLU()                            
        self.output = nn.Linear(hidden_size, output_size) 
        """


        
        # 一般使用nn.Sequential
        self.model = nn.Module( 
        nn.Linear(input_size, hidden_size),
        nn.ReLU(),
        nn.Linear(hidden_size, output_size)
        )

    def forward(self, x):
        # 向前传递操作
        """
        x = self.hidden(x)
        x = self.relu(x)
        x = self.output(x) 
        """
        x = self.model(x)
        return x

input_size = 10
hidden_size = 20
output_size = 5

model = NeuralNetwork(input_size, hidden_size, output_size)

```

## 损失函数与反向传播

```py
import torch
import torch.nn as nn

# 创建一个简单的神经网络
class NeuralNetwork(nn.Module):
    def __init__(self):
        super(NeuralNetwork, self).__init__()
        self.fc = nn.Linear(2, 1)

    def forward(self, x):
        return self.fc(x)

model = NeuralNetwork()

# 定义损失函数
criterion = nn.MSELoss()

# 生成一些随机输入和输出数据
x = torch.randn(10, 2)
y = torch.randn(10, 1)

# 前向传播
output = model(x)

# 计算损失
loss = criterion(output, y)

# 反向传播
loss.backward()

# 更新权重
nn.utils.clip_grad_value_(model.parameters(), 1)
optimizer.step()

```

## 优化器

```py
import torch
import torch.nn as nn
import torch.optim as optim

# 创建一个神经网络模型
model = nn.Linear(10, 1)

# 定义损失函数
criterion = nn.MSELoss()

# 创建一个优化器对象，学习率设置为0.01
optimizer = optim.Adam(model.parameters(), lr=0.01)

# 生成一些随机输入和输出数据
x = torch.randn(100, 10)
y = torch.randn(100, 1)

# 训练网络
for epoch in range(100):
    # 前向传播
    output = model(x)
    
    # 计算损失
    loss = criterion(output, y)
    
    # 梯度清零
    optimizer.zero_grad()
    
    # 反向传播
    loss.backward()
    
    # 更新权重
    optimizer.step()

```

## 模型保存与加载

```py
import torch
import torch.nn as nn

class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.conv1 = nn.Conv2d(1, 32, 3, 1)
        self.conv2 = nn.Conv2d(32, 64, 3, 1)
        self.fc1 = nn.Linear(9216, 128)
        self.fc2 = nn.Linear(128, 10)

    def forward(self, x):
        x = self.conv1(x)
        x = nn.functional.relu(x)
        x = self.conv2(x)
        x = nn.functional.relu(x)
        x = nn.functional.max_pool2d(x, 2)
        x = torch.flatten(x, 1)
        x = self.fc1(x)
        x = nn.functional.relu(x)
        x = self.fc2(x)
        return nn.functional.log_softmax(x, dim=1)

model = SimpleModel()
# 保存模型到文件
torch.save(model.state_dict(), 'simple_model.pth')
# 加载模型
loaded_model = SimpleModel()
loaded_model.load_state_dict(torch.load('simple_model.pth'))

```

## 使用GPU训练

```py
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
```

在网络模型，数据输入和标注，损失函数处使用gpu训练

