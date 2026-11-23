# 4.9.2 关键字参数｜官方示例
# https://docs.python.org/zh-cn/3.13/tutorial/controlflow.html#keyword-arguments
# 本节 4 道题均已核对。每个示例下方附有题目、标准答案和解析。


# ----------------------------------------------------------------------
# 示例 1：用位置参数和关键字参数调用 parrot()。
# 知识点：位置实参按顺序传入。关键字实参用 参数名=值 指定，也可以给必选参数传值。
# 省略带默认值的参数时使用默认值，关键字实参之间的顺序不影响参数绑定。
def parrot(voltage, state="a stiff", action="voom", type="Norwegian Blue"):
    print("-- This parrot wouldn't", action, end=" ")
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


parrot(1000)
parrot(voltage=1000)
parrot(voltage=1000000, action="VOOOOOM")
parrot(action="VOOOOOM", voltage=1000000)
parrot("a million", "bereft of life", "jump")
parrot("a thousand", state="pushing up the daisies")


# 题目：前两次调用的输出一样吗？第三、四次呢？最后一次调用给 voltage
#       和 state 传了什么值？action 和 type 又各用什么值？
# 标准答案：第 1、2 次输出相同，第 3、4 次输出也相同。最后一次调用中，
#     voltage = "a thousand"，state = "pushing up the daisies"，
#     action = "voom"，type = "Norwegian Blue"。
# 解析：前两次分别按位置和按名字给 voltage 传入 1000；第 3、4 次
#       只是调换了关键字实参的顺序。最后一次按位置传 voltage，按名字
#       传 state。action 和 type 都被省略，因此使用默认值。


# ----------------------------------------------------------------------
# 示例 2：四种无效的调用。
# 知识点：普通位置实参放在关键字实参前面。每个必选参数都要有值，参数名
# 必须能被函数接收，同一个参数也只能赋值一次。
# 以下是故意报错的示例，可以单独取消一行注释验证。
# parrot()
# parrot(voltage=5.0, 'dead')
# parrot(110, voltage=220)
# parrot(actor='John Cleese')


# 题目：从上到下，这四行各违反了哪条调用规则？
# 标准答案：依次是缺少必选参数、实参书写顺序错误、同一参数收到两个值、
#     传了函数不接受的参数名。
# 解析：parrot() 省略了没有默认值的 voltage。
#       parrot(voltage=5.0, 'dead') 把普通位置实参放在关键字实参后，报 SyntaxError。
#       parrot(110, voltage=220) 先按位置把 110 给 voltage，再按名字重复给值。
#       parrot(actor='John Cleese') 使用了函数不接受的名称 actor。
#       第 1、3、4 行在调用时都报 TypeError。


# ----------------------------------------------------------------------
# 示例 3：一个参数同时收到位置实参和关键字实参。
# 知识点：给同一个参数重复传值会触发 TypeError，即使两个值相同。
def function(a):
    pass


# function(0, a=0)


# 题目：两处 0 分别通过哪种方式传给了 a？删去哪一处可以让调用正常执行？
# 标准答案：第一个 0 是位置实参，a=0 是关键字实参。删掉任意一个实参都可以，
#     写成 function(0) 或 function(a=0)。
# 解析：两种传法都给同一个形参 a 赋值。即使两个值相等，重复传值也会报
#       TypeError。只保留一种传法时，a 恰好收到一个值。


# ----------------------------------------------------------------------
# 示例 4：用 *arguments 和 **keywords 接收多出来的实参。
# 知识点：*arguments 把额外的位置实参收进元组。**keywords 把额外的关键字
# 实参收进字典，保留调用时的传入顺序。两者一起用时，*arguments 在前面。
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])


cheeseshop(
    "Limburger",
    "It's very runny, sir.",
    "It's really very, VERY runny, sir.",
    shopkeeper="Michael Palin",
    client="John Cleese",
    sketch="Cheese Shop Sketch",
)


# 题目：这次调用把哪些值分别传给 kind、arguments 和 keywords？分隔线
#       之后会按什么顺序打印字典里的三个键？
# 标准答案：kind = "Limburger"。
#     arguments = ("It's very runny, sir.", "It's really very, VERY runny, sir.")。
#     keywords = {"shopkeeper": "Michael Palin", "client": "John Cleese",
#                 "sketch": "Cheese Shop Sketch"}。
#     分隔线后依次打印 shopkeeper、client、sketch 及各自的值。
# 解析：kind 接收第一个位置实参。*arguments 把剩余两个位置实参收进元组，
#       **keywords 把额外的关键字实参收进字典，遍历时按调用中的传入顺序输出。
