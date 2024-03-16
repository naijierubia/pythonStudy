from bll import CommodityController
from model import CommodityModel


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