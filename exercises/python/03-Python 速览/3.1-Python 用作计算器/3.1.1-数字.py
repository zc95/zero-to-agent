# [3.1.1. 数字](https://docs.python.org/zh-cn/3.13/tutorial/introduction.html#numbers)
# 官方在交互模式下直接输入表达式。这里用 print()，方便点击 ▶ 运行并查看结果。

# 基本运算与括号。整数是 int，5.0 和 1.6 是 float。
print(2 + 2)  # 4
print(50 - 5 * 6)  # 20
print((50 - 5 * 6) / 4)  # 5.0
print(8 / 5)  # 1.6

# / 是普通除法。对两个整数，// 求向下取整的商，% 求与该商对应的余数。
print(17 / 3)  # 5.666666666666667
print(17 // 3)  # 5
print(17 % 3)  # 2
print(5 * 3 + 2)  # 17

# ** 表示乘方。
print(5 ** 2)  # 25
print(2 ** 7)  # 128

# = 给变量赋值。运行到 print() 时才显示结果。
width = 20
height = 5 * 9
print(width * height)  # 900

# n 尚未定义。这里捕获示例故意触发的 NameError，让后续代码继续运行。
try:
    print(n)  # pyright: ignore[reportUndefinedVariable]
except NameError as error:
    print(f"NameError: {error}")

# 整数和浮点数混合进行这里的算术运算，结果是 float。
print(4 * 3.75 - 1)  # 14.0

# 官方交互模式示例。在终端输入 python，看到 >>> 后输入下列各行的代码。
# >>> tax = 12.5 / 100
# >>> price = 100.50
# >>> price * tax
# 12.5625
# >>> price + _
# 113.0625
# >>> round(_, 2)
# 113.06
# 交互模式会用 _ 记住上一个显示的表达式结果。脚本里用变量承接每一步。
tax = 12.5 / 100
price = 100.50
tax_amount = price * tax
print(tax_amount)  # 12.5625
total = price + tax_amount
print(total)  # 113.0625
print(round(total, 2))  # 113.06

# 官方还举了一个复数字面值。j 表示虚数单位。
print(3 + 5j)  # (3+5j)

# 官方脚注里的乘方优先级示例。
print(-3 ** 2)  # -9，先算 3 ** 2，再取负
print((-3) ** 2)  # 9，底数是 -3

# 额外练习。把除法那一组的 17 改成 -17，先猜 // 和 % 的结果，再运行。
