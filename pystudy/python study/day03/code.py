# ord(字符串)返回unicode码，只支持一个字符串
# chr（整数）返回整数的字符串
"""
获取字符串，打印编码值
"""
# value_string = input('请输入字符串：')
# print('从左到右编码值依次为:')
# for item in value_string:
#     item_uni = ord(item)
#     print(str(item) + '的编码值为:' + str(item_uni))


'''
将编码值转换为字符串
'''
# while True:
#     str_code = input('请输入编码值:')
#     if str_code == '':
#         break
#     char = chr(int(str_code))
#     print(char)

# 三引号所见即所得，输入什么样子，打印出来就什么样子
# \"   \'    水平制表格\t    换行\n    \\盘符
# 打印前加r表示没有转义符


# 格式化字符串
# "..%d...%s...%f.."%(整数变量,字符串变量,小数变量) %.nf为保留n位小数
# 1 + 2 = 3
number_one = 1
number_two = 2
str_sum = "%d + %d = %d" % (number_one, number_two, number_one + number_two)
print(str_sum)
