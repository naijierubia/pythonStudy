""" 将多个矩阵组合成一个矩阵 """
import numpy as np

a = np.arange(1, 7).reshape(2, 3)
b = np.arange(7, 13).reshape(2, 3)

print(a)
print(b)

# 垂直堆叠
print(np.vstack((a, b)))
# 水平堆叠
print(np.hstack((a, b)))
# 深度堆叠，视角是从上到下的
print(np.dstack((a, b)))


# 切割
c = np.vstack((a, b))   # (4, 3)
a, b = np.vsplit(c, 2)
print(c)
print(a)
print(b)

c = np.hstack((a, b)) # (2, 6)
a, b = np.hsplit(c, 2)
print(c)
print(a)
print(b)

c = np.dstack((a, b))
a, b = np.dsplit(c, 2)
print(c)
print(a)
print(b)

"""
另外还有其他API能堆叠和拆分
"""
a = a.reshape(2, 3)
b = b.reshape(2, 3)
print(np.concatenate((a, b), axis=0))
print(np.concatenate((a, b), axis=1))

# 行堆叠和列堆叠，要的是元组
a = np.arange(1, 9)
b = np.arange(9, 17)
print(np.row_stack((a, b)))
print(np.column_stack((a, b)))