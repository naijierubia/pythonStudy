"""
数学运算符
"""
# id(obj)获取目标变量内存地址
# 对变量进行数学运算并非改变了变量，而是新建了个变量
# print('a' in 'b')表示成员运算，如果a包含于b则返回True

'''
索引 index
'''
# 定位单个元素
# 越界报错

# message = '阳光只有一种颜色'
# print(message[1])
# print(message[-1])

'''
切片 slice
'''
# 定位多个元素
# 越界不报错

# message = '阳光只有一种颜色'
# print(message[0:3:1])
# print(message[:3])
# print(message[::-1])

'''
test
'''
# aphorism = '人生苦短，我用python'
# print(aphorism[0] + aphorism[-1])
# print(aphorism[:1] + aphorism[-6:])
# print(aphorism[(len(aphorism)) // 2])  # 需要地板除出整数
# print(aphorism[::-1])

'''
根据变成打印正方形
'''
length = int(input('请输入边长:'))
i = length
while i > 0:
    if i == 1 or i == length:
        print('*' * length)
    else:
        print('*' + ' ' * (length-2) + '*')
    i -= 1
