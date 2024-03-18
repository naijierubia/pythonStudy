"""
    静态方法
"""


class Vector2:
    """
        向量
    """

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    @staticmethod
    def get_left():
        return Vector2(0, -1)

    @staticmethod
    def get_right():
        return Vector2(0, 1)

    @staticmethod
    def get_up():
        return Vector2(-1, 0)


class DoubleListHelper:
    """
        二维列表助手类
    """

    @staticmethod
    def get_elements(list_target, vect_pos, vect_dir, count):
        """ 
         
            获取指定位置向指定方向获取指定数量的元素
            list_target:二维列表
            vect_pos: 起始位置
            vect_dir: 方向
            count: 数量
            当只是需要循环时用__代替，习惯用法，即一般函数内部就有循环的逻辑

         """
        list_result = []
        for __ in range(count):
            vect_pos.x += vect_dir.x
            vect_pos.y += vect_dir.y
            element = list_target[vect_pos.x][vect_pos.y]
            list_result.append(element)
        return list_result


pos = Vector2(2, 1)
right = Vector2.get_right()
pos.x += right.x
pos.y += right.y
print(pos.x)
print(pos.y)

list01 = [
    ["00", "01", "02", "03", "04"],
    ["10", "11", "12", "13", "14"],
    ["20", "21", "22", "23", "24"],
    ["30", "31", "32", "33", "34"],
]

print(DoubleListHelper.get_elements(list01, Vector2(3, 0), Vector2.get_right(), 3))

# 练习:32位置 向上获取3个元素
print(DoubleListHelper.get_elements(list01, Vector2(3, 2), Vector2.get_up(), 3))
# 练习:34位置 向左获取3个元素
print(DoubleListHelper.get_elements(list01, Vector2(3, 4), Vector2.get_left(), 3))
