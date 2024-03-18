class CommodityModel:
    def __init__(self, name='', price=0, uid=0):
        self.name = name
        self.price = price
        self.uid = uid


class CommodityController:
    commodity_uid = 100

    def __init__(self):
        self.__commodity_list = []
        self.__order_list = []

    @property
    def commodity_list(self):
        return self.__commodity_list

    @property
    def order_list(self):
        return self.__order_list

    def add_commodity(self, commodity):
        commodity.uid = self.commodity_uid
        self.__commodity_list.append(commodity)
        self.commodity_uid += 1

    def buy(self, uid, count):
        self.add_commodity_to_order(uid, count)

    def settlement(self, money):
        self.calculate_total_money()
        self.pay(money)
        self.order_list.clear()

    def find_commodity_by_uid(self, uid):
        for item in self.__commodity_list:
            if item.uid == uid:
                return item
        return False

    def add_commodity_to_order(self, uid, count):
        commodity = self.find_commodity_by_uid(uid)
        commodity.count = count
        self.order_list.append(commodity)

    def calculate_total_money(self):
        total_money = 0
        for item in self.order_list:
            total_money += item.price * item.count
        return total_money

    def pay(self, money):
        total_money = self.calculate_total_money()
        if money >= total_money:
            print('收款%d元,找您%d元' % (money, money - total_money))
        else:
            print('余额不足')


class CommodityViewer:
    def __init__(self):
        self.__controller = CommodityController()

    def commodity(self):
        self.__controller.add_commodity(CommodityModel('苹果', 8))
        self.__controller.add_commodity(CommodityModel('香蕉', 3))
        self.__controller.add_commodity(CommodityModel('梨子', 4))
        self.__controller.add_commodity(CommodityModel('草莓', 10))
    selection = 0

    def main(self):
        self.commodity()
        while True:
            self.print_menu()
            self.select()


    def print_commodity_info(self):
        tplt = "{0:^8}\t{1:^10}\t{2:^8}\t{3:^8}"
        print(tplt.format('商品编号', '商品名称', '商品价格', chr(12288)))
        list01 = self.__controller.commodity_list
        for item in list01:
            print(tplt.format(item.uid, item.name, item.price, chr(12288)))

    def print_menu(self):
        print(
            '1)购买商品:\n'
            '2)结账\n'
            # '3)离开\n'
        )

    def select(self):
        selection = int(input('请选择您需要进行的操作:'))
        if selection == 1:
            self.buy()
        elif selection == 2:
            self.settlement()
        elif selection == 3:
            pass

    def buy(self):
        self.print_commodity_info()
        commodity = int(input('请输入需要购买物品的uid:'))
        count = int(input('请输入需要购买的数量:'))
        self.__controller.buy(commodity, count)

    def settlement(self):
        print('下面是您所购买的物品清单:')
        self.print_order_info()
        money = int(input('请输入您支付金额:'))
        self.__controller.settlement(money)

    def print_order_info(self):
        tplt = "{0:^8}\t{1:^8}\t{2:^8}\t{3:^8}"
        print(tplt.format('商品名称', '商品价格', '商品数量', chr(12288)))
        list01 = self.__controller.order_list
        for item in list01:
            print(tplt.format(item.name, item.price, item.count, chr(12288)))


viewer = CommodityViewer()
viewer.main()
