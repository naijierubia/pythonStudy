class Bomb:
    def explode(self, target):
        target.damage()


class AttackTarget:
    def damage(self):
        pass
# ***********************************************************


class Player(AttackTarget):
    def __init__(self, name='', hp=0):
        self.name = name
        self.hp = hp

    def damage(self):
        super().damage()
        self.hp -= 10
        print(self.name, '受伤')


class Enemy(AttackTarget):
    def __init__(self, name='', hp=0):
        self.name = name
        self.hp = hp

    def damage(self):
        super().damage()
        self.hp -= 20
        print(self.name, '受伤')


g01 = Bomb()
p01 = Player('jame', 120)
e01 = Enemy('den', 200)
print(p01.__dict__)
print(e01.__dict__)
g01.explode(p01)
print(p01.__dict__)
g01.explode(e01)
print(e01.__dict__)