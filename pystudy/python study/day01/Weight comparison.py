"""
体重比较输出最大
"""
i = int(input('请输入需要比较的人数:'))
people = i
max_weight = float(input('请输入第1个人的体重:'))
min_weight = max_weight
total_weight = max_weight
n = 2
while i - 1 > 0:
    temp_weight = float(input('请输入第' + str(n) + '个人的体重:'))
    if temp_weight > max_weight:
        max_weight = temp_weight
    if temp_weight < min_weight:
        min_weight = temp_weight
    total_weight = total_weight + temp_weight
    i = i - 1
    n = n + 1
average_weight = total_weight / people
print('最大的体重为' + str(max_weight))
print('最小的体重为' + str(min_weight))
print('平均体重为' + str(average_weight))
