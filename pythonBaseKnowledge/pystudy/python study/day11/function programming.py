"""
    函数式编程 - 思想
    首先find是一个比较大的概念，要怎么找呢？
    我们可以先定义一个函数，然后把这个函数作为参数传递给find函数，
    这样find函数就可以根据这个函数的返回值来判断是否符合条件。
"""
list01 = [4, 54, 56, 65, 67, 7]


# “封装” -- 分


def condition01(item):
    return item > 50


def condition02(item):
    return item < 10


# 通用
# “继承” - 隔
def find(func):
    for item in list01:
        # if item < 10:
        # if condition02(item):
        if func(item):
            yield item


# "多态" - 做
for item in find(condition01):
    print(item)

for item in find(condition02):
    print(item)

"""
练习
"""


class Wife:
    def __init__(self, name="", face_score=0, age=0, height=0):
        self.name = name
        self.face_score = face_score
        self.age = age
        self.height = height


list_wife = [
    Wife("双儿", 96, 22, 166),
    Wife("阿珂", 100, 23, 173),
    Wife("小郡主", 96, 22, 161),
    Wife("方怡", 86, 27, 166),
    Wife("苏荃", 99, 31, 176),
    Wife("建宁", 93, 24, 163),
    Wife("曾柔", 88, 26, 170),
]


def find(list, func):
    for item in list:
        if func(item):
            yield item.name


def face(item):
    return item.face_score > 90


def height(item):
    return item.height < 170


for item in find(list_wife, face):
    print(item)
print()
for item in find(list_wife, height):
    print(item)

