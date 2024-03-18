""" 
掩码，即过滤复合条件的元素出来

 """

import numpy as np

a = np.arange(1, 101)
# 过滤出能被3整除的元素
print(a[a % 3 == 0])
print(a)
# 过滤出能被3整除的元素，并将这些元素替换为999
a[a % 3 == 0] = 999
print(a)

# 根据列表取出相应位置的元素
names = np.array(["Mi", "Apple", "Huawei", "Oppo", "Vivo"])
rank = [0, 3, 4, 2, 1, 3, 2, 1]
print(names[rank])
