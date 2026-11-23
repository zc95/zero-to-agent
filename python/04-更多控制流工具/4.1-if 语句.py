# 4.1 if 语句｜官方示例
# https://docs.python.org/zh-cn/3.13/tutorial/controlflow.html#if-statements
# 在终端运行此文件，按提示输入整数并按回车。

x = int(input("Please enter an integer: "))
if x < 0:
    x = 0
    print("Negative changed to zero")
elif x == 0:
    print("Zero")
elif x == 1:
    print("Single")
else:
    print("More")

# 输入 42：三个条件依次为假，执行 else，打印 More。x 仍为 42。
# 输入 -2：第一个条件为真，先把 x 改成 0，再打印 Negative changed to zero。
# 这一轮已经进入 if 分支，后面的 elif 和 else 都跳过，最终 x 为 0。
# 输入 0 或 1：分别命中两个 elif，打印 Zero 或 Single。
