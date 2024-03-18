# 一系列变量组成的可变序列容器
# list[],添加
# list('')每个字符分别为一个元素

"""
追加
"""
# list01 = ['a', 1, '你好', 2022]
# list01.append('HELLO')
# print(list01)

'''
插入
'''
# list01 = ['a', 1, '你好', 2022]
# list01.insert(-1, 'HELLO')
# list01.insert(1, 'HELLO')
# print(list01)

'''
获取
'''
# 索引和切片
# 切片后的列表和原列表不是同一个列表

'''
循环
'''
# 通过for循环遍历所有对象
list01 = ['a', 1, '你好', 2022]
# for item in list01[::-1]:
#     print(item)
# 倒着获取一个列表,这样写不会创建新的列表占用内存
# for i in range(len(list01)-1, -1, -1):
#     print(list01[i])

'''
修改
'''
# 通过上述几种获取方式重新给对象赋值
