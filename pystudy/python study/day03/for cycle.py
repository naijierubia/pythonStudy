"""
求和 for
"""
# number = input('请输入一串一位数整数：')
# sum_value = 0
# for item in number:              # for循环便利的变量为字符串型
#     sum_value += int(item)
# print(sum_value)

'''
循环计数  range（）
'''
# print('打印0 1 2 3 4 5 的和')
# sum_value_1 = 0
# for item in range(6):
#     sum_value_1 += item
# print(sum_value_1)
#
# print('打印 2 3 4 5 6 7 的和')
# sum_value_1 = 0
# for item in range(2, 8):
#     sum_value_1 += item
# print(sum_value_1)
#
# print('打印0 2 4 6 的和')
# sum_value_1 = 0
# for item in range(0, 7, 2):
#     sum_value_1 += item
# print(sum_value_1)
#
# print('打印4 3 2 1 0 的和')
# sum_value_1 = 0
# for item in range(4, -1, -1):
#     sum_value_1 += item
# print(sum_value_1)
#
# print('打印-1 -2 -3 -4 的和')
# sum_value_1 = 0
# for item in range(-1, -5, -1):
#     sum_value_1 += item
# print(sum_value_1)

'''
累加1 - 50 且被5整除的数 continue
'''
# sum_value = 0
# for item in range(1, 51):
#     # 如果不满足累加条件，那么跳过当前数字
#     if item % 5 != 0:
#         continue
#     sum_value += item
# print(sum_value)

"""
累加10-50之间个位不是2,5,9的整数. unit
"""
sum_value = 0
for item in range(10, 51):
    unit = item % 10
    if unit == 2 or unit == 5 or unit == 9:
        continue
    sum_value += item
print(sum_value)
