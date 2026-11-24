# 9.5 继承｜官方教程要点
# https://docs.python.org/zh-cn/3.13/tutorial/classes.html#inheritance

# 知识点：子类可覆写父类方法，也可用 super() 继续调用父类实现。
class Task:
    def __init__(self, title):
        self.title = title

    def describe(self):
        return self.title


class UrgentTask(Task):
    def describe(self):
        return "紧急：" + super().describe()


task = UrgentTask("建表")
print(task.describe(), isinstance(task, Task))

# 题目：打印什么？实例在哪里拿到 title？
# 标准答案：打印 紧急：建表 True。title 由继承的 Task.__init__ 初始化。
# 解析：UrgentTask 覆写了 describe，又调用父类方法取出标题后加前缀。
