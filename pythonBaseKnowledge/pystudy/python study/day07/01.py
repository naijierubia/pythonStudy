# class Wife:
#     pass
#
#
# ak = Wife()
# ak.name = '阿珂'
#
# print(ak.name)


# class Dog:
#     def __init__(self, species=None, honeyname=None, age=None, gender=None):
#         self. species = species
#         self. honeyname = honeyname
#         self. age = age
#         self. gender = gender
#
#
# labrador01 = Dog('拉布拉多', '小黄', 6, '公')
# chenery01 = Dog('雪纳瑞', '小白', 5, '母')
# # 查看实例变量
# print(labrador01.__dict__)


class Wife:
    wife_count = 0

    @classmethod
    def print_wife_count(cls):
        print('美少女收录数量为:', cls.wife_count)

    def __init__(self, name='', score=0, age=0):
        self.name = name
        self.score = score
        self.age = age
        Wife.wife_count += 1

    def print_name(self):
        print(self.name)


miku = Wife('初音未来', 94, 17)
rina = Wife('绪方理奈', 98, 22)
yuki = Wife('长门有希', 86, 16)
firekeep = Wife('防火女', 92, 24)
list01 = [miku, rina, yuki, firekeep]


def get_name():
    list_name = []
    for item in list01:
        list_name.append(item)
    return list_name


for item in get_name():
    item.print_name()


def screen_from_score(a):
    list_score = []
    for item in list01:
        if item.score > a:
            list_score.append(item)
    return list_score


for item in screen_from_score(90):
    item.print_name()


def get_age_max():
    max_age = list01[0]
    for i in range(1, len(list01)):
        if max_age.age < list01[i].age:
            max_age = list01[i]
    return max_age


get_age_max().print_name()


def ascending_order_from_score():
    for x in range(len(list01) - 1):
        for y in range(x, len(list01)):
            if list01[x].score > list01[y].score:
                list01[x], list01[y] = list01[y], list01[x]


ascending_order_from_score()
for item in list01:
    item.print_name()

Wife.print_wife_count()