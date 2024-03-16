# 注意力机制

注意力机制的核心重点就是让网络关注到它更需要关注的地方。

当我们使用卷积神经网络去处理图片的时候，我们会更希望卷积神经网络去注意应该注意的地方，而不是什么都关注，我们不可能手动去调节需要注意的地方，这个时候，如何让卷积神经网络去自适应的注意重要的物体变得极为重要。

注意力机制就是实现网络自适应注意的一个方式。

一般而言，注意力机制可以分为通道注意力机制，空间注意力机制，以及二者的结合。



在深度学习中，常见的注意力机制的实现方式有SENet，CBAM，ECA等等。



1. 空间注意力机制：要关注一只鸟，空间注意力就会让模型关注鸟本身，忽视鸟所在的环境中
2. 通道注意力机制：经过卷积之后会得到多个特征图，每一层都是特征，该机制会让模型关注应当关注的的特征

## SENet

![SENet](https://img-blog.csdnimg.cn/20201124130209827.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NDc5MTk2NA==,size_16,color_FFFFFF,t_70#pic_center)

给通道赋予权重

```py
import torch.nn as nn

class SENet(nn.Module):
    def __init__(self, channel, ratio=16):
        super(SENet, self).__init__()
        self.avg_pool = nn.AdaptiveAvgPool2d(1)
        self.fc = nn.Sequential(
                nn.Linear(channel, channel // ratio, bias=False),
                nn.ReLU(inplace=True),
                nn.Linear(channel // ratio, channel, bias=False),
                nn.Sigmoid()
        )

    def forward(self, x):
        b, c, _, _ = x.size()
        y = self.avg_pool(x).view(b, c)
        y = self.fc(y).view(b, c, 1, 1)
        return x * y

```

