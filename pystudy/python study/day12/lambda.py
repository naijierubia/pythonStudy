def func01(a, b):
    return a > b


# 有参数和返回值
lambda01 = lambda a, b: a > b
print(lambda01(10, 20))


def func02():
    return "ok"


# 无参数有返回值
lambda02 = lambda: 'ok'
print(lambda02())


def func03():
    print('ok')


# 无参数无返回值
lambda03 = lambda: print('ok')
lambda03()


def func(a):
    print(a)


# 有参数无返回值
lambda04 = lambda a: print(a)
lambda04('a')

# lambda语句不支持赋值操作
# lambda语句不支持多语句
