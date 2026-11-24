# 4.9.5 解包实参列表｜官方示例
# https://docs.python.org/zh-cn/3.13/tutorial/controlflow.html#unpacking-argument-lists
# 在函数定义里，* 和 ** 可以收集实参。在函数调用里，它们可以展开实参。
# 本节 2 道题均已核对。每个示例下方附有题目、标准答案和解析。


# ----------------------------------------------------------------------
# 示例 1：用 * 把列表展开成位置实参。
# 知识点：函数调用中的 *args 会按顺序取出 args 里的元素，逐个按位置传入。
# 教程在交互解释器中查看结果，这里用 print() 显示。
print(list(range(3, 6)))

args = [3, 6]
print(list(range(*args)))


# 题目：两行分别打印什么？去掉 *，改成 range(args)，传给 range() 的是什么？
# 标准答案：两行都打印 [3, 4, 5]。range(args) 收到一个实参，即列表 [3, 6]，
# 并抛出 TypeError。
# 解析：range(*args) 把列表展开为两个整数，等同于 range(3, 6)，终止值 6
# 不包含在结果中。range(args) 则传入整个列表，range() 无法把它当作整数。


# ----------------------------------------------------------------------
# 示例 2：用 ** 把字典展开成关键字实参。
# 知识点：函数调用中的 **d 把字典的键变成参数名，把对应的值按名字传入。
def parrot(voltage, state="a stiff", action="voom", type="Norwegian Blue"):
    print("-- This parrot wouldn't", action, end=" ")
    print("if you put", voltage, "volts through it.", end=" ")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)


# 题目：不用 **d，把这次调用改写成显式传关键字实参的形式。
#       字典中没有 type，函数里的 type 会取什么值？
# 标准答案：parrot(voltage="four million", state="bleedin' demised", action="VOOM")。
# type 使用默认值 "Norwegian Blue"。
# 解析：**d 将每个字典键作为参数名，并按原样传入对应的值。显式写出时，
# state 要保留完整字符串，action 要保留大写。因为没有传入 type，它才使用默认值。
