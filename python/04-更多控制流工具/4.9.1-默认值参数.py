# 4.9.1 默认值参数｜官方示例
# https://docs.python.org/zh-cn/3.13/tutorial/controlflow.html#default-argument-values
# 本节 4 道题均已核对。每个示例下方附有题目、标准答案和解析。


# ----------------------------------------------------------------------
# 示例 1：调用 ask_ok() 时，可以省略带默认值的参数。
# 知识点：prompt 没有默认值，调用时必须提供。retries 和 reminder 有默认值。
# in 用来检查用户输入是否在给定的选项中。无效输入会减少剩余重试次数。
def ask_ok(prompt, retries=4, reminder="Please try again!"):
    while True:
        reply = input(prompt)
        if reply in {"y", "ye", "yes"}:
            return True
        if reply in {"n", "no", "nop", "nope"}:
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError("invalid user response")
        print(reminder)


# 官方给出的三种调用方式。想试交互时，可以任选一行取消注释。
# ask_ok('Do you really want to quit?')
# ask_ok('OK to overwrite the file?', 2)
# ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')


# 题目：第一、第二种调用各用什么 retries 和 reminder？用第二种方式调用时，
#       如果先输入 maybe、再输入 yes，程序会额外打印什么，最后返回什么？
# 标准答案：第一种用 retries=4，第二种用 retries=2。两种的 reminder 都是
#     "Please try again!"。第二种调用会额外打印一次该提醒，最后返回 True。
# 解析：省略的实参采用默认值。输入 maybe 时，两个 in 判断都不成立，
#       retries 从 2 减到 1，随后打印提醒。下一轮输入 yes，执行 return True。


# ----------------------------------------------------------------------
# 示例 2：默认值表达式在定义函数时求值。
# 知识点：执行 def 时会求出默认值，并供以后省略实参的调用使用。
i = 5


def f(arg=i):
    print(arg)


i = 6
f()


# 题目：f() 打印 5 还是 6？什么时候确定了 arg 的默认值？
# 标准答案：打印 5。arg 的默认值在执行 def 时确定。
# 解析：定义 f 时，i 的值为 5，这个值被保存为 arg 的默认值。后来将 i
#       重新赋值为 6，并不会改变已保存的默认值。f() 省略 arg，就使用 5。


# ----------------------------------------------------------------------
# 示例 3：用列表作为默认值。
# 知识点：默认表达式只求值一次。append() 会修改收到的列表，注意观察
# 多次省略 L 调用 f() 时，用到的是不是同一个列表。
def f(a, L=[]):
    L.append(a)
    return L


print(f(1))
print(f(2))
print(f(3))


# 题目：这三行分别打印什么？为什么第二次调用可以看到第一次加入的值？
# 标准答案：依次打印 [1]、[1, 2]、[1, 2, 3]。
# 解析：执行 def 时只创建一次默认列表。每次省略 L 都会使用同一个列表，
#       append() 直接修改它。第二次调用时，列表里已经有第一次加入的 1。
# 补充：单独运行示例 3 时，可用 f.__defaults__ 查看函数保存的默认值。
#       定义后是 ([],)，第一次调用 f(1) 后是 ([1],)。


# ----------------------------------------------------------------------
# 示例 4：用 None 作为默认值，在函数体里创建列表。
# 知识点：L 为 None 时才执行 L = []，随后把 a 加到列表里。
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L


# 补上同样的三次调用，方便与示例 3 对照。
print(f(1))
print(f(2))
print(f(3))


# 题目：这三行分别打印什么？空列表是在定义函数时创建，还是在调用时创建？
# 标准答案：依次打印 [1]、[2]、[3]。这三次调用都省略 L，各自创建一个空列表。
# 解析：默认值是 None。每次省略 L，进入函数时 L 都为 None，所以该次调用
#       会执行 L = []。每次新建的列表只收集本次传入的 a。
