# 9.3 初探类｜官方教程要点
# https://docs.python.org/zh-cn/3.13/tutorial/classes.html#a-first-look-at-classes

# 知识点：类定义创建类对象。调用类时创建实例，__init__ 初始化实例属性。
# 实例调用方法时，Python 自动把实例作为 self 传入。
class Dog:
    kind = "canine"

    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)


fido = Dog("Fido")
buddy = Dog("Buddy")
fido.add_trick("roll over")
print(fido.kind, buddy.kind)
print(fido.tricks, buddy.tricks)

# 题目：kind 和 tricks 哪个共享？两份 tricks 各是什么？
# 标准答案：kind 定义在类上。fido.tricks 是 ['roll over']，buddy.tricks 是 []。
# 解析：每个实例执行自己的 __init__，各自创建列表。可变的类属性则可能被实例共享。
