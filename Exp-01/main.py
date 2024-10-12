# 1. 输出 1~100 之间能被7整除但不能被 5 整除的所有数

# for 循环
print("1~100之间能被7整除但不能同时被5整除的所有整数是：")
for num in range(1, 101):
    if num % 7 == 0 and num % 5 != 0:
        print(num)
print()

# while 循环
print("1~100之间能被7整除但不能同时被5整除的所有整数是：")
num = 1
while num < 101:
    if num % 7 == 0 and num % 5 != 0:
        print(num)
    num += 1
print()

# 列表推导式
print("1~100之间能被7整除但不能同时被5整除的所有整数是：")
print([num for num in range(1, 101) if num % 7 == 0 and num % 5 != 0])
print()

# 2. 打印九九乘法表
print("九九乘法表：")
for i in range(1, 10):
    for j in range(1, 10):
        print(f'{i} x {j} = {i * j}')
    print()
print()

# 3. 输入4位整数作为年份，判断其是否为闰年
year = int(input("请输入4位整数的年份: "))
# 如果年份能被400整除，则为闰年
# 如果年份能被4整除但不能被100整除也为闰年
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(f"{year} 是闰年")
else:
    print(f"{year} 不是闰年")
print()

# 4. 10的阶乘
num = 1
for i in range(1, 11):
    num = num * i
print(f"10的阶乘是{num}")
print()

# 5. 100以内所有奇数的和

# 循环
num = 0
for i in range(1, 101):
    if i % 2 != 0:
        num += i
print(f"100以内所有奇数的和是{num}")
print()

# 列表推导式
print(f"100以内所有奇数的和是{sum([num for num in range(1, 101) if num % 2 != 0])}")
print()


# 6. 分段函数计算
def function(x):
    y = None
    if x < 0:
        y = 0
    elif 0 <= x < 5:
        y = x
    elif 5 <= x < 10:
        y = 3 * x - 5
    elif 10 <= x < 20:
        y = 0.5 * x - 2
    elif 20 <= x:
        y = 0
    return y


# 测试数据
# print([function(x) for x in range(-5, 25)])
print(function(int(input('请输入x的值='))))


# 7. 计算糖果总数
count = 1
while True:
    if count % 1 == 0 and count % 2 == 1 and count % 3 == 0 and count % 4 == 1 and count % 5 == 4 and count % 6 == 3 and count % 7 == 0 and count % 8 == 1 and count % 9 == 0:
        print(f"最少有 {count} 个糖果")
        break
    count += 1
