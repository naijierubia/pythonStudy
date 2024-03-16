装饰器

私有类

类方法

私有变量

```py
class Number:
    def __init__(self):
        self.num = 1


number = Number()
number.x = 1
print(number.x)
```

父类传过去就行

自定义可迭代对象

抽象

```py
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


```



自定义迭代

```py
class MyIterable:
    def __init__(self, items):
        self.items = items

    def __iter__(self):
        # 迭代器对象初始化
        self.index = 0
        return self

    def __next__(self):
        # 返回下一个元素
        if self.index < len(self.items):
            result = self.items[self.index]
            self.index += 1
            return result
        else:
            # 到达迭代末尾，引发StopIteration异常
            raise StopIteration
        
# 使用示例
my_iterable = MyIterable([1, 2, 3, 4, 5])
for item in my_iterable:
    print(item)
```

```py
class StaffIterator:
    def __init__(self, data):
        self.data = data
        self.count = -1

    def __next__(self):
        # 迭代时下一个获取对象的方法
        self.count += 1
        if self.count > len(self.data)-1:
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
```

类中的变量修改后全程有效



作为包导入的文件夹必须包含

```py
__init__.py文件
```

在Python中，静态方法和类方法都是属于类的成员方法，但它们有以下几点区别：

1. 静态方法没有self参数，而类方法有一个self参数。
2. 静态方法内部不能访问类和实例的属性，而类方法可以访问类的属性，但不能访问实例的属性。
3. 静态方法的函数装饰器是@staticmethod，而类方法的函数装饰器是@classmethod。
4. 静态方法中不能使用cls参数，而类方法中可以使用cls参数。
5. 静态方法通常用于那些与实例无关的函数，而类方法通常用于那些操作类的属性或对所有实例都有效的函数。

下面是一个示例代码，展示了静态方法和类方法的区别：

```python
class MyClass:
    @staticmethod
    def static_method(arg1, arg2):
        # 静态方法没有self参数
        return arg1 + arg2

    @classmethod
    def class_method(cls, arg1, arg2):
        # 类方法有一个self参数和一个cls参数
        return cls.__name__ + ": " + str(arg1 + arg2)

my_instance = MyClass()
result1 = MyClass.static_method(10, 20)  # 静态方法不能访问实例或类的属性
result2 = MyClass.class_method(my_instance, 30, 40)  # 类方法可以访问类的属性
```

在上面的示例中，static_method是一个静态方法，它没有self参数，并且不能访问类和实例的属性。class_method是一个类方法，它有一个self参数和一个cls参数，并且可以访问类的属性。
