# 第 9 章测试｜类的基础
# https://docs.python.org/zh-cn/3.13/tutorial/classes.html


# ----------------------------------------------------------------------
# 第 1 题｜实例属性与方法
class Counter:
    def __init__(self, start=0):
        self.value = start

    def increment(self):
        self.value += 1


first = Counter()
second = Counter(4)
first.increment()
print(first.value, second.value)

# 题目：打印什么？increment() 中的 self 指向谁？
# 标准答案：打印 1 4。调用 first.increment() 时 self 就是 first。
# 解析：两个实例各自保存 value，第一次递增只修改 first 的属性。


# ----------------------------------------------------------------------
# 第 2 题｜方法覆写
class DoubleCounter(Counter):
    def increment(self):
        super().increment()
        super().increment()


counter = DoubleCounter(10)
counter.increment()
print(counter.value)

# 题目：结果是多少？调用了哪个类的 increment()？
# 标准答案：12。先进入子类的 increment()，它执行两次父类的方法。
# 解析：两次 super() 调用操作的 self 都是同一个 DoubleCounter 实例。
