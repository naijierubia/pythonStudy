# 商品信息,shift + f6 rename variable
dict_commodity_information = {
    101: {"name": "屠龙刀", "price": 10000},
    102: {"name": "倚天剑", "price": 10000},
    103: {"name": "九阴白骨爪", "price": 8000},
    104: {"name": "九阳神功", "price": 9000},
    105: {"name": "降龙十八掌", "price": 8000},
    106: {"name": "乾坤大挪移", "price": 10000}
}
list_order = []


def buy():
    print_commodity_information()
    create_order()
    print_commodity_order()


def print_commodity_information():
    for key, value in dict_commodity_information.items():
        print('编号:%d 商品:%s 单价:%d ' % (key, value['name'], value['price']))


def create_order():
    while True:
        commodity_id = int(input('请输入需要购买商品的id:'))
        if commodity_id in dict_commodity_information:
            break
        else:
            print('请输入正确的商品id')

    commodity_number = int(input('请输入商品数量:'))
    list_order.append({'commodity_id': commodity_id, "commodity_number": commodity_number})


def print_commodity_order():
    for item in list_order:
        commodity01 = dict_commodity_information[item["commodity_id"]]
        print("商品：%s，单价：%d,数量:%d." % (commodity01["name"], commodity01["price"], item["commodity_number"]))


def settlement():
    calculate_price()
    pay()


def calculate_price():
    calculation_result = 0
    for item in list_order:
        calculation_result += dict_commodity_information[item['commodity_id']]['price'] * item['commodity_number']
    print('您需要支付:' + str(calculation_result))
    return calculation_result


def pay():
    while True:
        money = int(input('请输入支付金额:'))
        if money >= calculate_price():
            break
        else:
            print('金额不足,请重新支付')
    print('您支付了%d元，找您%d元' % (money, money - calculate_price()))
    list_order.clear()


def shopping():
    while True:
        select = int(input('请输入需要进行的操作: 购买输入1 结算输入2 离开输入3 \n'))
        if select == 1:
            buy()

        elif select == 2:
            settlement()

        elif select == 3:
            break
        else:
            print('请输入有效的数字！')


shopping()

