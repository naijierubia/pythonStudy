import numpy as np

# numpy元数据和存储数据是分开存储的
"""
创建矩阵的方法
"""
# 利用numpy创建矩阵
ary01 = np.array([[1, 2, 3], [4, 5, 6]])
print(ary01)

# 创建一维数组
ary02 = np.arange(1, 10, 2)
print(ary02)

# 创建全1或全0矩阵
ary03 = np.ones((3, 3),dtype='int32')
print(ary03)
ary04 = np.zeros((3, 3),dtype='float64')
print(ary04)

# 构建结构类似的矩阵
ary05 = np.ones_like(ary01)
print(ary05)
ary06 = np.zeros_like(ary01)
print(ary06)

# 构建一个全2的矩阵
ary07 = np.full((3, 3), 2)
print(ary07)

"""
矩阵的属性
"""
# shape可读写
print(ary01,ary01.shape)
ary01.shape = (3,2)
print(ary01,ary01.shape)

#  dtype可读写
print(ary01,ary01.dtype)
ary01.dtype = 'float32'
print(ary01,ary01.dtype)

# size size属性可以拿到矩阵元素的个数，len属性可以拿到矩阵的行数
print(ary01.size,len(ary01))

# 也可修改成字符串和bool值
print(ary01.astype('str'))
