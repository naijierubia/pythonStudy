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


def condition01(item):
    return item.height < 170


def first01(item):
    return item.face_score > 95


def first02(item):
    return item.name == '方怡'


def count01(item):
    return len(item.name) > 2


def count02(item):
    return item.age < 25


def format01(item):
    return item.name


def format02(item):
    return (item.name, item.age)


for item in IterableHelper.find_all(list_wife, condition01):
    print(item)

print(IterableHelper.get_count(list_wife, count02))

for item in IterableHelper.print_all(list_wife, format02):
    print(item)

print(IterableHelper.is_exist(list_wife, lambda item: item.height > 170))

print(IterableHelper.sum_item(list_wife, lambda item: item.height))
print(IterableHelper.find_max(list_wife, lambda element: element.age))
print(IterableHelper.find_min(list_wife, lambda element: element.age))
print()
for item in IterableHelper.down_by(list_wife, lambda item: item.height):
    print(item)
