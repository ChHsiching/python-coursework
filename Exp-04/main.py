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
    # for pastry in pastries:
    #     for drink in drinks:
    #         print(pastry + ' + ' + drink)
    [print(pastry + ' + ' + drink) for pastry in pastries for drink in drinks]


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


# 2. 生成1000个0~100之间的随机整数，分别采用字典和集合统计每个元素的出现次数。
# import random
def generate_random_numbers(num, start, end):
    """
    生成 num 个 start 到 end 之间的随机整数
    :param num:
    :param start:
    :param end:
    :return:
    """
    # “_”作为占位符变量，无需关注它的迭代值
    # 代码目的在于循环 num 次，每次生成一个指定范围内的随机整数
    return [random.randint(start, end) for _ in range(num)]


def count_elements_with_dict(random_int_list):
    """
    采用字典统计列表中元素出现的次数
    :param random_int_list:
    :return result:
    """
    result = {}
    # 1
    # for num in random_int_list:
    #     if num in result:
    #         result[num] += 1
    #     else:
    #         result[num] = 1
    # return result

    # 2
    # for num in random_int_list:
    #     result[num] = result.get(num, 0) + 1
    # return result
    # 不可以在字典推导式中使用这个逻辑，它在生成过程中依赖于固定的初始状态
    # result 在字典推导式中的每一次循环都是空初始状态（result = {}）
    # 因此返回的字典中每一个元素都是 num : 0 + 1
    # 错误代码:
    # return {num: result.get(num, 0) + 1 for num in random_int_list}

    # 3
    result = {num: random_int_list.count(num) for num in set(random_int_list)}
    return result


# 采用集合统计列表中元素出现的次数
def count_elements_with_set(random_int_list):
    """
    采用集合统计列表中元素出现的次数
    :param random_int_list:
    :return:
    """
    # return {num: random_int_list.count(num) for num in random_int_list}
    # return {num: sum(1 for _ in random_int_list if _ == num) for num in set(random_int_list)}
    # 使用集合统计出现次数
    unique_numbers = set(random_int_list)  # 获取唯一元素
    set_counts = {(num, random_list.count(num)) for num in unique_numbers}
    return {num: sum(1 for _ in random_int_list if _ == num) for num in random_int_list}


random_list = generate_random_numbers(1000, 0, 100)
dict_result = count_elements_with_dict(random_list)
set_result = count_elements_with_set(random_list)
print(random_list)
print(dict_result)
print(set_result)

del generate_random_numbers
del count_elements_with_dict
del count_elements_with_set
del random_list
del dict_result
del set_result


# 3. 输入两个分别包含若干整数的列表lstA和lstB，输出一个字典，要求使用列表lstA中的元素作为键，列表lstB中元素作为值，并且最终字典中的元素数量取决于lstA和lstB中元素最少的列表的数量。
def create_dict(lstA, lstB):
    return {key: value for key, value in zip(lstA, lstB)}


# 获取用户输入
lstA = list(map(int, input("请输入lstA中的整数，以空格分隔：").split()))
lstB = list(map(int, input("请输入lstB中的整数，以空格分隔：").split()))

# 生成字典并输出结果
result = create_dict(lstA, lstB)
print("生成的字典为：", result)

del lstA, lstB
del create_dict
del result


#


