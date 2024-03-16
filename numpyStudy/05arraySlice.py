"""
切片
用,分割维度
"""
import numpy as np

ary = np.arange(1, 19).reshape(3, 6)
print(ary, ary.shape)
# 后两列的数据
print(ary[1:, :])
print(ary[:, ::2])

print(ary[::2, :])
print(ary[:, :3])

ary = ary.reshape(2, 3, 3)
print(ary, ary.shape)
print(ary[:, :2, :2])