# 传统思想
list01 = [32, 58, 456, 456, 86, 968, 645, 435, 983546, 8453, 89]


def get_evennumber01(list):
    list_even = []
    for item in list:
        if item % 2 == 0:
            list_even.append(item)
    return list_even


result = get_evennumber01(list01)
for item in result:
    print(item)


# 生成器思想


def get_evennumber02(list):
    for item in list:
        if item % 2 == 0:
            yield item


result = get_evennumber02(list01)
for item in result:
    print(item)

"""
自定义生成器
"""
dict_name = {'初音未来': 16, '长门有希': 17, '御坂美琴': 15}


def my_enumerate(iterable):
    # 初始化计数器，生成器函数调用时会保留里面的变量，直到拿完里面的数据
    count = 0
    for item in iterable:
        tuple_result = (count, item)
        yield tuple_result
        count += 1


for item in my_enumerate(dict_name):
    print(item)


"""
自定义my_zip
"""
list_name = ['五更琉璃', '千反田爱瑠', '五河琴里']
list_room = [102, 106, 305]


def my_zip(iterable01, iterable02):
    for i in range(len(iterable01)):
        tuple_result = (iterable01[i], iterable02[i])
        yield tuple_result


for item in my_zip(list_name, list_room):
    print(item)

