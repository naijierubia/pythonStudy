"""
打印图案
"""

# for line in range(4):
#     for item in range(5):
#         if item % 2:
#             print('#', end='')
#         else:
#             print('*', end='')
#     print()
#

'''
比较大小
'''

# list_number = []
# while True:
#     number_in = input('请输入数字:')
#     if number_in == '':
#         break
#     list_number.append(float(number_in))
# for v in range(len(list_number) - 1):
#     for item in range(v + 1, len(list_number)):
#         if list_number[v] > list_number[item]:
#             list_number[v], list_number[item] = list_number[item], list_number[v]
# print(list_number)

'''
打印列表
'''
"""
    打印二维列表第四行第三列元素。
    从左到右打印二维列表第二行所有元素。
    从上到下打印二维列表第一列所有元素。
    将二维列表按照表格状输出到终端。
"""
# list01 = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
#     [13, 14, 15, 16],
# ]
# print(list01[3][2])
#
# for item in range(len(list01[1])):
#     print(list01[1][item])
#
# for item in range(len(list01)):
#     print(list01[item][0])
#
# for y in range(len(list01)):
#     for x in range(len(list01[y])):
#         print(list01[y][x], end='\t')
#     print()

'''
方阵转置
'''
list01 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
]
for y in range(len(list01)-1):
    for x in range(y + 1, len(list01)):
        list01[y][x], list01[x][y] = list01[x][y], list01[y][x]
print(list01)
