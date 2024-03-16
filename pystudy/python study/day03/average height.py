"""
打印平均身高
"""
list_height = list()

while True:
    str_height = input('请输入身高:')
    if str_height == '':
        break
    list_height.append(float(str_height))

print('总人数为:' + str(len(list_height)))
print('最大身高为:' + str(max(list_height)))
print('最小身高为:' + str(min(list_height)))
print('平均身高为:' + str(sum(list_height)/len(list_height)))
