# # alt + enter 掉出选项
# class Cellphone:
#     def __init__(self, brand, price, color):
#         self. brand = brand
#         self. price = price
#         self. color = color
#
#     def call(self):
#         print(self.brand, '打电话')
#
#
# iphone = Cellphone('苹果', 9999, '灰色')
# huawei01 = Cellphone('华为', 9999, '黑色')
# huawei01.call()

class Dog:
    def __init__(self, species=None, honeyname=None, age=None, gender=None):
        self. species = species
        self. honeyname = honeyname
        self. age = age
        self. gender = gender

    def eating(self):
        print(self.species, '干饭')


labrador01 = Dog('拉布拉多', '小黄', 6, '公')
chenery01 = Dog('雪纳瑞', '小白', 5, '母')
labrador01.eating()
chenery01.eating()

list01 = [
    labrador01,
    chenery01,
    Dog('沙皮'),
    Dog('拉布拉多', '大白')
]


def find_labrador():
    list_labrador = []
    for dog_species in list01:
        if dog_species.species == '拉布拉多':
            list_labrador.append(dog_species)
    return list_labrador


for item in find_labrador():
    print(item.honeyname)
