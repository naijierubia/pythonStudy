"""
循环录入字符串
"""
# list_temp = list()
# while True:
#     str_temp = input('请输入:')
#     if str_temp == '':
#         break
#     list_temp.append(str_temp)
#
# str_result = '、'.join(list_temp)
# print(str_result)


'''
英文单词翻转
'''
# str_message = input('请输入一句英文:')
# list_temp = str_message.split(' ')
# str_result = ' '.join(list_temp[::-1])
# print(str_result)

'''
列表推导式
'''
list01 = [item ** 2 for item in range(1, 11)]
print(list01)
list02 = [item for item in list01 if item % 2]  # 真值表达式
print(list02)
list03 = [item + 1 for item in list01 if item % 2 == 0 and item > 5]
print(list03)
