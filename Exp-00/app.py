# 1. 变量类型赋值和观察
var = 114  # 整型
print(f"var 的类型 (整型): {type(var)}")

var = 11.4  # 浮点型
print(f"var 的类型 (浮点型): {type(var)}")

var = "Hello Python!"  # 字符串
print(f"var 的类型 (字符串): {type(var)}", end="\n\n")

# 2. 变量的内存地址
x = 23
y = 23
my_list = [22, 23, 24, 25]

print(f"x 的内存地址: {id(x)}")
print(f"y 的内存地址: {id(y)}")
print(f"列表第二个元素的内存地址: {id(my_list[1])}", end="\n\n")

# 3. 比较浮点数是否相等
result_comparison = (0.9 - 0.3) == 0.6
print(f"0.9 - 0.3 是否等于 0.6? {result_comparison}", end="\n\n")

# 4. 复数操作
x = 23 + 34j
print(f"实部: {x.real}, 虚部: {x.imag}, 共轭复数: {x.conjugate()}", end="\n\n")

# 5. 创建列表、元组、字典和集合
my_list = [1, 2, 3, 4, 5]
my_tuple = (6, 7, 8, 9, 10)
my_dict = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
my_set = {11, 12, 13, 14, 15}

# 访问中间元素
list_middle = my_list[len(my_list) // 2]
tuple_middle = my_tuple[len(my_tuple) // 2]
dict_middle_key = list(my_dict.keys())[len(my_dict) // 2]
dict_middle_value = my_dict[dict_middle_key]

print(f"列表中间元素: {list_middle}, 元组中间元素: {tuple_middle}, 字典中间元素: {dict_middle_value}", end="\n\n")

# 6. 比较列表和元组中的元素
list_elem_2 = my_list[2]  # 下标为 2 的元素
tuple_elem_neg3 = my_tuple[-3]  # 下标为 -3 的元素
elements_equal = (list_elem_2 == tuple_elem_neg3)
print(f"列表中下标为 2 和元组中下标为 -3 的元素是否相同? {elements_equal}", end="\n\n")

# 7. 检查成员关系
membership_check = 23 in (1, 3, 23)
print(f"23 是否在 (1, 3, 23) 中? {membership_check}", end="\n\n")

# 8. 位运算
bitwise_operations = {
    '7 << 2': 7 << 2,
    '7 & 9': 7 & 9,
    '7 | 15': 7 | 15,
    '15 ^ 9': 15 ^ 9
}

print(bitwise_operations, end="\n\n")
