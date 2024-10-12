# I. 必做部分

# 1. 输入一个包含若干整数的列表，输出新列表，要求新列表中的所有元素来自于输入的列表，并且降序排列。
def sort_descending(disordered_list):
    """
    输入整数列表，输出降序列表
    :param disordered_list:
    :return descending_list:
    """
    # 对列表进行排序，默认为升序，使用 reverse 参数来改为降序
    descending_list = sorted(disordered_list, reverse=True)
    return descending_list


# input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# input_list = list(map(int, input("请输入包含若干整数的列表，用空格分隔：").split()))
input_list = [int(num) for num in input("请输入包含若干整数的列表，用空格分隔：").split()]
sorted_list = sort_descending(input_list)
print(sorted_list)

del input_list
del sorted_list


# 2. 列表推导式 。使用列表推导式生成列表，其元素为100以内所有能被3整除的整数。
def generate_list():
    """
    使用列表推导式生成列表，其元素为100以内所有能被3整除的整数。
    :return:
    """
    return [num for num in range(1, 100) if num % 3 == 0]


generate_list = generate_list()
print(generate_list)

del generate_list

