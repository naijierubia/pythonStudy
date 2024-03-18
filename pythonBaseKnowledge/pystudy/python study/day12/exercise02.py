"""
    使用内置高级函数实现下列功能：

    1. 在敌人列表中查找所有敌人名称与攻击力
    2. 在敌人列表中查找血量大于500的所有敌人
    3. 对敌人列表进行降序排列
    4. 找出列表[(1,),(2,2,2),(3,3)]中长度最大的元素
    5. 根据value对字典进行升序排列{"张无忌":306,"赵敏":305,"小昭":102}
"""


class Enemy:
    def __init__(self, name="", hp=0, atk=0, defence=0):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defence = defence

    def __str__(self):
        return "%s-%d-%d-%d" % (self.name, self.hp, self.atk, self.defence)


list_enemy = [
    Enemy("灭霸", 999, 555, 333),
    Enemy("成昆", 360, 100, 50),
    Enemy("玄冥二老", 300, 90, 70),
    Enemy("白骨精", 600, 200, 60),
]

for item in map(lambda item: (item.name, item.atk), list_enemy):
    print(item)

for item in filter(lambda item: item.hp > 500, list_enemy):
    print(item)
for item in sorted(list_enemy, key=lambda item: item.hp, reverse=True):
    print(item)
print(max([(1,), (2, 2, 2), (3, 3)], key=lambda item: len(item)))
for item in sorted({"张无忌": 306, "赵敏": 305, "小昭": 102}.items(), key=lambda item: item[1]):
    print(item)
