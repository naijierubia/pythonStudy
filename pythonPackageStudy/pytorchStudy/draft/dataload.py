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
