# [5.1.3. 列表推导式](https://docs.python.org/zh-cn/3.13/tutorial/datastructures.html#list-comprehensions)
# 用列表推导式筛选任务并取出标题，练习把遍历、筛选和转换写在同一个表达式里。

tasks = [
    {"title": "看 Python 视频", "done": True},
    {"title": "练习列表和字典", "done": False},
    {"title": "学习函数", "done": False},
]

print(tasks[0]["title"])

# 练习：用列表推导式收集已完成任务的标题，再打印结果。
