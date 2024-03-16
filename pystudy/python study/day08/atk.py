class Player:
    def __init__(self, name='', atk_number=0):
        self.name = name
        self.atk_number = atk_number

    def do_atk(self, target):
        print(self.name, '发起了攻击，造成了', self.atk_number, '点伤害')
        target.injured(self.atk_number)


class Enemy:
    def __init__(self, name='', hp_number=0):
        self.name = name
        self.hp_number = hp_number

    def injured(self, value):
        self.hp_number -= value
        if self.hp_number <= 0:
            self.death()
        else:
            self.damage()

    def death(self):
        print(self.name, '被击沉')

    def damage(self):
        print(self.name, '受伤')


enterprise = Player('企业', 200)
akagi = Enemy('赤城', 160)
enterprise.do_atk(akagi)




