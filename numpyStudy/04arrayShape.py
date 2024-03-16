"""
改变矩阵的维度
resize用于改变数组的大小，多补0，少截取
reshape用于改变矩阵的维度，最后元素个数不能改变
"""
import numpy as np

# 原始矩阵
ary = np.arange(1, 19)
print(ary, ary.shape)

# 修改矩阵的维度
# 也可以通过修改属性修改
ary.resize(2, 9)
print(ary, ary.shape)
# 通过方法修改
ary1 = ary.reshape(3, 3, 2)
print(ary1, ary1.shape)

# 拷贝数组，对拷贝的数组进行修改，不会影响原始数组
ary2 = ary.flatten()
print(ary2, ary2.shape)
