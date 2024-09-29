# I. 课外自行完成部分

# 2 (1)
print("Hello World")
# 2 (2)
print(f"9999**99 = {9999**99}")

# 3. 导库
import random
import numpy

# 4. 内置函数
# (1) help, id
help(help)
a = 1
print(f"a的地址={id(a)}，1的地址={id(1)}")
a += 1
print(f"a的地址={id(a)}，2的地址={id(2)}")

# (2) bin, oct, hex, ord, chr

# (3) list, tuple, dict, set, frozenset, type, isinstance

# (4) max, min, sum

# (5) input, print

# (6) sorted, reversed, enumerate, map, filter, range, zip, eval


# II. 必做部分

# 1. 输入任意大的自然数，输出各位数字之和
sum_num = 0
num = int(input("请输入自然数："))
while True:
    bit = num % 10          # num 的最低位
    sum_num += bit          # 最低为加和
    num = int(num / 10)     # num 舍弃最低位
    if num == 0:            # num 只剩最后一位
        break
print(f"各位数字之和={sum_num}")

# 两行代码实现此功能
# 作为字符串输入
number = input("请输入任意大的自然数: ")
print(sum(int(digit) for digit in number))


# 2. 计算圆柱体的体积、表面积（结果保留两位小数）
import math

radius = 66.0
height = 24.2

bottom_area = math.pi * (radius ** 2)
bottom_perimeter = 2 * math.pi * radius

volume = bottom_area * height
surface_area = bottom_perimeter * height

print(f"体积 = {round(volume, 2)}，表面积 = {round(surface_area, 2)}")


# 3. 三门课成绩
scores = list(map(float, input("请输入语文、数学、英语的考试成绩（以空格为间隔）：").split()))
print(f"总分 = {sum(scores)}，平均分 = {round(sum(scores) / 3, 2)}，最高分 = {max(scores)}，最低分 = {min(scores)}")
# 输入成绩并使用 split() 方法将其分割成列表
# scores_input = input("请输入小明的语文、数学和英语成绩（以空格分隔）: ")
# scores = list(map(float, scores_input.split()))  # 将输入的字符串转换为浮点数列表
#
# # (1) 计算总和、平均分、最高分和最低分
# total = sum(scores)
# average = total / len(scores)
# highest = max(scores)
# lowest = min(scores)
#
# # 输出计算结果
# print(f"三门成绩的总和: {total:.2f}")
# print(f"三门成绩的平均分: {average:.2f}")
# print(f"三门成绩的最高分: {highest:.2f}")
# print(f"三门成绩的最低分: {lowest:.2f}")
#
# # (2) 判断是否有零分
# has_zero = any(score == 0 for score in scores)  # 检查是否有成绩为零的情况
# if has_zero:
#     print("有成绩为零分。")
# else:
#     print("没有零分。")
#
# # (3) 根据权重计算总评成绩
# weights = [0.5, 0.3, 0.2]  # 语文、数学、英语的权重
# final_score = sum(score * weight for score, weight in zip(scores, weights))  # 加权计算
# print(f"小明的最终总评成绩: {final_score:.2f}")


# 4. 找零钱


# 5. 进制转换


