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


# 3. 给出一个包含若干整数的列表[23,16,18,19,76,121,33,57,80]，输出一个新列表，要求新列表中只包含原列表中的偶数。
def even_list(int_list):
    """
    输入整数列表，输出由其中的偶数组成的列表
    :param int_list:
    :return:
    """
    return [num for num in int_list if num % 2 == 0]


input_list = [int(num) for num in input("请输入包含若干整数的列表，用空格分隔：").split()]
even_list = even_list(input_list)
print(even_list)

del input_list
del even_list


# 4. 编写程序，用户输入一个列表和两个整数作为下标，然后用切片获取并输出介入两个下标之间的元素组成的子列表。例如，用户输入[1,2,3,4,5,6]和2，5后，程序输出[3,4,5,6]。
def list_slicing(int_list, start_int, end_int):
    """
    输入一个列表两个整数下标，获取介入两个下标之间的元素组成的子列表
    :param int_list:
    :param start_int:
    :param end_int:
    :return:
    """
    # return [num for num in int_list[range(start_int, end_int + 1)]]
    return [num for num in int_list[start_int: end_int + 1]]


input_list = [int(num) for num in input("请输入包含若干整数的列表，用空格分隔：").split()]
start = int(input("请输入切片开始的下标："))
end = int(input("请输入切片结束的下标："))
list_slicing = list_slicing(input_list, start, end)
print(list_slicing)

del input_list
del list_slicing


