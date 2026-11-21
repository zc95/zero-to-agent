# [3.2. 走向编程的第一步](https://docs.python.org/zh-cn/3.13/tutorial/introduction.html#first-steps-towards-programming)
# 按官方顺序演示斐波那契数列和 print() 的用法。

# 斐波那契数列从 0 和 1 开始，之后每一项都是前两项之和。
a, b = 0, 1
while a < 10:
    print(a)  # 依次输出 0、1、1、2、3、5、8，每个数字单独一行
    # 先用旧的 a 和 b 算好右边，再把两个结果依次赋给左边。
    a, b = b, a + b

# 循环体由缩进标记。a 变为 13 时，a < 10 为假，循环结束。
# 在交互模式逐行输入 while 循环时，最后输入一个空行来执行整段代码。

# print() 接收多个参数时，默认用空格隔开。
i = 256 * 256
print('The value of i is', i)  # The value of i is 65536

# end=',' 把每次输出的结尾改成逗号。整组数字会显示在同一行。
a, b = 0, 1
while a < 1000:
    print(a, end=',')
    a, b = b, a + b

# 输出：0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,
