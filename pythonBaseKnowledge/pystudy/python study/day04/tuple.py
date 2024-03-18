"""
计算今年过去多少天
"""

tuple_01 = (31, 28, 31, 30, 31, 30, 31, 31, 30, 30, 30, 31)
mouth = int(input("请输入月份："))
day = int(input("请输入日期："))
sum_day = day
for item in tuple_01[:mouth - 1]:
    sum_day += item
print('一共过去了' + str(sum_day) + '天')

