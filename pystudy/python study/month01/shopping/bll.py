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