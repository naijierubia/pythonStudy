# 类变量表示大家都能用的数据
"""
    类成员
        类变量：
"""



class ICBC:
    """
        工商银行
    """
    # 类变量：大家的数据(总行的钱)
    total_money = 1000000

    @classmethod
    def print_total_money(cls):
        # print("总行的钱：",ICBC.total_money)
        print("总行的钱：", cls.total_money)

    def __init__(self, name="", money=0):
        self.name = name
        self.money = money
        # 总行的钱减少
        ICBC.total_money -= money


i01  = ICBC("陶然亭支行",100000)
ICBC.print_total_money()

i02  = ICBC("天坛支行",100000)
ICBC.print_total_money()
