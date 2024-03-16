""" 数据结构 """
import pandas as pd
import numpy as np

# series一维数组

# 1. 创建空的Series
s = pd.Series()
print(s)

# 2. 通过ndarray创建Series对象
data = np.array(["a", "b", "c", "d"])
s = pd.Series(data)
print(s)

# 3. 通过字典创建Series对象
data = {"a": 0.0, "b": 1.0, "c": 2.0}
s = pd.Series(data)
print(s)

# 4. 通过标量创建Series对象，即创建多个相同的数值
s = pd.Series(5, index=["a", "b", "c", "d"])
print(s)

""" 数据访问 """
# 1. 数字切片访问
print(s[:2])

# 2.标签切片访问，左右都闭
print(s["a":"c"])

""" property """
print(s.values)
print(s.index)
print(s.dtype)
print(s.size)
print(s.ndim)
print(s.shape)
