# 4.9.6 Lambda 表达式｜官方示例
# https://docs.python.org/zh-cn/3.13/tutorial/controlflow.html#lambda-expressions
# 每个示例下方附有题目、标准答案和解析。


# ----------------------------------------------------------------------
# 示例 1：用 lambda 返回一个小函数。
# 知识点：lambda a, b: a+b 表示一个接收 a、b 并返回 a+b 的匿名函数。
# 冒号后写一个表达式，计算结果就是返回值。lambda 可以用到外层函数的变量。
def make_incrementor(n):
    return lambda x: x + n


f = make_incrementor(42)
# 教程在交互解释器中直接调用，这里用 print() 显示返回值。
print(f(0))
print(f(1))


# 题目：f(0) 和 f(1) 分别返回什么？两次调用里，x 和 n 的值各来自哪里？
# 标准答案：f(0) 返回 42，f(1) 返回 43。x 来自每次调用 f 时传的值，
# n 来自创建这个函数时传给 make_incrementor 的 42。
# 解析：make_incrementor(42) 返回一个接收 x 的函数。这个函数仍能访问外层的
# n。f(0) 计算 0 + 42，f(1) 计算 1 + 42。


# ----------------------------------------------------------------------
# 示例 2：用 lambda 指定列表的排序依据。
# 知识点：sort(key=...) 会把每个元素交给 key 函数，按该函数的返回值排序。
# pair 是列表里的单个元素，pair[1] 取出这个元素的第二项。
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)


# 题目：排序后 pairs 的顺序是什么？为什么开头的数字不是排序依据？
# 标准答案：[(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]。
# 解析：key 函数取出每个元组的第二项，所以比较的是单词。单词按字母顺序
# 排为 four、one、three、two。整个元组一起移动，其中的数字仍跟着对应的单词。
