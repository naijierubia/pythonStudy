"""
运算符
"""
number_01 = float(input('请输入第一个数字:'))
operator = input('请输入运算符:')
number_02 = float(input("请输入第二个数字:"))
if operator == '+':
    print('结果为：' + str(number_01 + number_02))
elif operator == '-':
    print('结果为：' + str(number_01 - number_02))
elif operator == '*':
    print('结果为：' + str(number_01 * number_02))
elif operator == '/':
    if number_02 != 0:
        print('结果为：' + str(number_01 / number_02))
    else:
        print('除数不能为0！')
else:
    print('请输入正确的运算符')
# elif表示if之间只要有一个满足就不执行其他的条件判断
