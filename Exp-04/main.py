import random


# 1. 餐厅下午茶
# 某餐厅推出了优惠下午茶套餐活动。顾客可以以优惠的价格从给定的糕点和给定的饮料中各选一款组成套餐。
# 已知，指定的糕点包括松饼(Muffins)、提拉米苏(Tiramisu)、芝士蛋糕(Cheese Cake)和三明治(Sandwich)；
# 指定的饮料包括红茶(Black tea,)、咖啡(Coffee)和橙汁(Orange Juice)。
# 请问，可以搭配出哪些套餐供客户选择？请依次打印输出各种套餐。
def print_menu(pastries, drinks):
    """
    输出所有优惠套餐搭配
    :param pastries:
    :param drinks:
    :return:
    """
    for pastry in pastries:
        for drink in drinks:
            print(pastry + ' + ' + drink)


discount_pastries = ['Muffins', 'Tiramisu', 'Cheese Cake', 'Sandwich']
discount_drinks = ['Black tea', 'Coffee', 'Orange Juice']
discount_pastries_chinese = ['松饼', '提拉米苏', '芝士蛋糕', '三明治']
discount_drinks_chinese = ['红茶', '咖啡', '橙汁']
print_menu(discount_pastries, discount_drinks)
print_menu(discount_pastries_chinese, discount_drinks_chinese)

del discount_pastries
del discount_drinks
del discount_pastries_chinese
del discount_drinks_chinese
del print_menu

