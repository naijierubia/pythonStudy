# """
# for 原理
# """
# list01 = [30, 25, 6]
# iterator = list01.__iter__()
# while True:
#     try:
#         item = iterator.__next__()
#         print(item)
#     except StopIteration:
#         break
# """"""
# tuple01 = (3, 25, 6)
# iterator = tuple01.__iter__()
# while True:
#     try:
#         item = iterator.__next__()
#         print(item)
#     except StopIteration:
#         break
# """"""
# dict01 = {'name': 'haruhi', 'age': 16, 'score': 98}
# iterator_key = list(dict01.keys()).__iter__()
# iterator_value = list(dict01.values()).__iter__()
#
# while True:
#     try:
#         item = iterator_key.__next__()
#         print(item)
#     except StopIteration:
#         break
# while True:
#     try:
#         item = iterator_value.__next__()
#         print(item)
#     except StopIteration:
#         break
# """"""
# iteror = dict01.__iter__()
# while True:
#     try:
#         key = iteror.__next__()
#         print(key,dict01[key])
#     except StopIteration:
#         break
# """"""


class StaffIterator:
    def __init__(self, data):
        self.data = data
        self.count = -1

    def __next__(self):
        # 迭代时下一个获取对象的方法
        self.count += 1
        if self.count > len(self.data)-1:
            self.count = -1
            raise StopIteration()
        return self.data[self.count]


class Staff:
    def __init__(self):
        self.__staff_list = []

    def add_staff(self, staff):
        self.__staff_list.append(staff)

    def __iter__(self):
        return StaffIterator(self.__staff_list)


staff = Staff()
staff.add_staff('御坂美琴')
staff.add_staff('长门有希')
staff.add_staff('五更琉璃')
iterator = staff.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break
