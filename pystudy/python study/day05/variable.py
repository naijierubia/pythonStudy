# """
# 函数参数与实际参数
# """
#
#
# def fun01(a, b, c):
#     print(a)
#     print(b)
#     print(c)
#
#
# # 位置实参
# fun01(1, 2, 3)
# # 序列实参
# list01 = [1, 2, 3]
# fun01(*list01)
# # 关键字实参
# fun01(a=1, c=3, b=2)
# # 字典实参
# dict01 = {'a': 1, 'c': 3, 'b': 2}
# fun01(**dict01)


# def fun02(a=0, b='', c=0.0):
#     print(a)
#     print(b)
#     print(c)
#
#
# # 默认参数
# fun02(1, '你好')

# def get_time_calc_seconds(h=0, m=0, s=0):
#     return h*3600 + m*60 + s
#
#
# print(get_time_calc_seconds(m=3))

def fun03(*args):
    print(args)


fun03('123', 0)
# 将实参合并为一个元组，只能有一个

