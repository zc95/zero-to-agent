# 5.1 列表详解｜官方示例
# https://docs.python.org/zh-cn/3.13/tutorial/datastructures.html#more-on-lists
# 按官方顺序整理。交互解释器会直接显示的值，在脚本里用 print() 显示。
# 各组示例下方附有题目、标准答案和解析。

from collections import deque
from math import pi


# ----------------------------------------------------------------------
# 示例 1｜列表方法
# append 加入一项，extend 加入可迭代对象里的所有项，insert 按索引插入。
# remove 按值删除第一项，pop 按索引删除并返回该项，clear 清空列表。
# count 计算出现次数，index 返回首次命中的索引，也可限定搜索范围。
# sort、reverse 就地修改，返回 None。copy 返回浅拷贝。
fruits = ["orange", "apple", "pear", "banana", "kiwi", "apple", "banana"]
print(fruits.count("apple"))
print(fruits.count("tangerine"))
print(fruits.index("banana"))
print(fruits.index("banana", 4))
fruits.reverse()
print(fruits)
fruits.append("grape")
print(fruits)
fruits.sort()
print(fruits)
print(fruits.pop())

# index 和 remove 找不到指定的值时会报 ValueError。pop 越界时报 IndexError。
# 下面两种比较会报 TypeError，可以单独取消注释尝试。
# sorted([None, 'hello', 10])
# 3 + 4j < 5 + 7j


# 题目：两个 index("banana", ...) 调用各返回多少？最后的 pop() 取出了什么？
#       如果写成 fruits = fruits.sort()，fruits 会变成什么？
# 标准答案：索引依次是 3 和 6，pop() 取出 pear。赋值 fruits = fruits.sort() 会得到 None。
# 解析：index() 返回相对于原列表的索引。sort() 原地排序，末项变成 pear，返回值是 None。


# ----------------------------------------------------------------------
# 示例 2｜5.1.1 用列表实现栈
# 知识点：append() 从末尾加入元素，pop() 默认从末尾取出元素，后进先出。
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)
print(stack.pop())
print(stack)
print(stack.pop())
print(stack.pop())
print(stack)


# 题目：三次 pop() 按顺序取出什么？最后 stack 里还有哪些元素？
# 标准答案：依次取出 7、6、5，剩下 [3, 4]。
# 解析：append() 和无参 pop() 都操作列表末尾，所以最后加入的元素最先被取出。


# ----------------------------------------------------------------------
# 示例 3｜5.1.2 用 deque 实现队列
# 知识点：队列先进先出。deque 的 append() 从末尾加入，popleft() 从开头取出。
# 列表也能 pop(0)，但剩下的元素需要前移。
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")
print(queue.popleft())
print(queue.popleft())
print(queue)


# 题目：最先离开的是哪两个人？剩下的人按什么顺序排队？
# 标准答案：依次取出 Eric、John，剩下 Michael、Terry、Graham。
# 解析：popleft() 从队首取元素，append() 加到队尾，因此按到达顺序取出。


# ----------------------------------------------------------------------
# 示例 4｜5.1.3 三种写法生成平方列表
# 知识点：列表推导式的 for 负责取值，最前面的表达式负责生成列表元素。
# 普通 for 的循环变量会留在当前作用域，推导式里的变量只在推导式内部使用。
squares = []
for x in range(10):
    squares.append(x**2)
print(squares)

squares = list(map(lambda x: x**2, range(10)))
print(squares)

squares = [x**2 for x in range(10)]
print(squares)


# 题目：三种写法结果是否相同？最后一个数是多少？推导式中哪个部分算平方？
# 标准答案：三种结果相同，最后一个数是 81，推导式开头的 x**2 计算平方。
# 解析：range(10) 依次提供 0 到 9，三种写法都对每个数字执行一次平方运算。


# ----------------------------------------------------------------------
# 示例 5｜多个 for 和一个 if
# 知识点：推导式里的 for 和 if 从左向右读，顺序对应普通嵌套循环。
print([(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y])

combs = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            combs.append((x, y))
print(combs)


# 题目：只看 x 为 1 的情况，会生成哪几个元组，顺序是什么？为什么没有 (1, 1)？
# 标准答案：依次生成 (1, 3)、(1, 4)。
# 解析：y 按 3、1、4 的顺序取值，x 和 y 相等时，条件 x != y 为假。


# ----------------------------------------------------------------------
# 示例 6｜转换、筛选、取绝对值与去空格
# 知识点：for 后的 if 决定是否留下元素，for 前的表达式决定留下什么值。
vec = [-4, -2, 0, 2, 4]
print([x * 2 for x in vec])
print([x for x in vec if x >= 0])
print([abs(x) for x in vec])

freshfruit = ["  banana", "  loganberry ", "passion fruit  "]
print([weapon.strip() for weapon in freshfruit])


# 题目：筛掉负数的结果是什么？abs(x) 生成的列表为什么仍有 5 项？
# 标准答案：筛选得到 [0, 2, 4]。绝对值列表有 5 项。
# 解析：筛选用 if 决定是否保留。abs(x) 对每个元素做转换，每次都生成一项。


# ----------------------------------------------------------------------
# 示例 7｜生成元组、展平列表、组合函数
# 知识点：生成元组时用圆括号包住整个表达式。两个 for 也可以逐层遍历列表。
print([(x, x**2) for x in range(6)])
# [x, x**2 for x in range(6)]  # 故意报错，元组表达式缺少圆括号。

vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print([num for elem in vec for num in elem])
print([str(round(pi, i)) for i in range(1, 6)])


# 题目：元组列表的最后一项是什么？展平后的列表有几项？
#       最后一行里 round() 和 str() 的作用分别是什么？
# 标准答案：最后一项是 (5, 25)，展平后有 9 项。round() 按小数位舍入，str() 转成字符串。
# 解析：内层 for 依次展开每个子列表。round(pi, i) 先计算，再把结果传给 str()。


# ----------------------------------------------------------------------
# 示例 8｜5.1.4 嵌套推导式和 zip() 转置矩阵
# 知识点：外层先选列索引 i，内层遍历每一行并取出该列的元素。
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
print([[row[i] for row in matrix] for i in range(4)])

transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print(transposed)

transposed = []
for i in range(4):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print(transposed)

# *matrix 把三行分别传给 zip()。zip() 每次从这三行各取一项。
print(list(zip(*matrix)))


# 题目：转置后的第一行由哪些数字组成？zip() 那行里，每一组是列表还是元组？
# 标准答案：第一行取 1、5、9。zip() 每次给出一个元组，所以第一组是 (1, 5, 9)。
# 解析：转置第一列时 i 是 0，依次读取三行的第 0 项。list(zip(*matrix)) 的外层是列表。
