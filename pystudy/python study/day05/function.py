"""
打印相对应的矩形
"""
# row = int(input('请输入行数:'))
# line = int(input('请输入列数:'))
# item = input('请输入填充内容:')
#
#
# def rectangle(row, line, item):
#     """
#     打印一个矩阵
#     :param row:行
#     :param line: 列
#     :param item: 填充物
#     :return: none
#     """
#     for r in range(row):
#         for c in range(line):
#             print(item, end='')
#         print()
#
#
# rectangle(row, line, item)

# '''
# 多位整数相加和
# '''
#
#
# def sum_integer(str_sum):
#     """
#     计算整数各位相加的和
#     :param str_sum:
#     :return:
#     """
#     add = 0
#     for item in str(str_sum):
#         add += int(item)
#     return add
#
#
# result = sum_integer(123456)
# print(result)

'''
查询列表元素是否重复
'''


def judge_unit_repeat(list01):
    for x in range(0, len(list01)-1):
        for y in range(x + 1, len(list01)):
            if list01[x] == list01[y]:
                return True
    return False


result = judge_unit_repeat([1, 3, 6, 8, 2, 7])
print(result)