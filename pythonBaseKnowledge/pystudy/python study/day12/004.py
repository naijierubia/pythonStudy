"""
内置高阶函数
"""
from common.iterable_tools import IterableHelper


class Wife:
    def __init__(self, name="", face_score=0, age=0, height=0):
        self.name = name
        self.face_score = face_score
        self.age = age
        self.height = height

    def __str__(self):
        return '%s-%d-%d-%d' % (self.name, self.face_score, self.age, self.height)


list_wife = [
    Wife("双儿", 96, 22, 166),
    Wife("阿珂", 100, 23, 173),
    Wife("小郡主", 96, 22, 161),
    Wife("方怡", 86, 27, 166),
    Wife("苏荃", 99, 31, 176),
    Wife("建宁", 93, 24, 163),
    Wife("曾柔", 88, 26, 170),
]
'''
map类似于select函数，返回对应函数值
'''
for item in map(lambda item: item.name, list_wife):
    print(item)

'''
filter过滤器,类似find_all
'''
for item in filter(lambda item: item.face_score > 90, list_wife):
    print(item)

'''
max / min 求最大最小值
'''
print(max(list_wife, key=lambda item: item.face_score))
print(min(list_wife, key=lambda item: item.face_score))

'''
sorted 排序
'''
for item in sorted(list_wife, key=lambda item: item.height, reverse=True):
    print(item)
