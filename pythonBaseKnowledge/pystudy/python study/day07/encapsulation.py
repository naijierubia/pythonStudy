class Enemy:

    def __init__(self, name='', hp=0, atk=1):
        self.__name = name
        self.__hp = hp
        self.__atk = atk

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, value):
        if 0 <= value <= 100:
            self.__hp = value

        else:
            raise Exception('输入数值在0-100之间')

    @property
    def atk(self):
        return self.__atk

    @atk.setter
    def atk(self, value):
        if 1 <= value <= 50:
            self.__atk = value

        else:
            raise Exception('输入数值在1-50之间')


enemy01 = Enemy('大大怪')
enemy02 = Enemy('小小怪')
enemy01.hp = 95
enemy02.atk = 35
print(enemy01.__dict__)
print(enemy02.__dict__)