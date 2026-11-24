# 第 5 章测试｜数据结构
# https://docs.python.org/zh-cn/3.13/tutorial/datastructures.html
# 每题附标准答案和解析，可独立运行整份脚本。


# ----------------------------------------------------------------------
# 第 1 题｜复制、列表方法和切片
values = [3, 1, 2, 1]
original = values.copy()
values.remove(1)
del values[1:2]
print(values.pop(), values, original)

# 题目：打印什么？原始副本为什么没有跟着变？
# 标准答案：打印 1 [3] [3, 1, 2, 1]。
# 解析：remove 只删第一项 1，del 再删索引 1 上的 2。pop 从末尾取出 1。
# copy 创建了另一个外层列表，后面的删除操作都发生在 values 上。


# ----------------------------------------------------------------------
# 第 2 题｜字典、列表推导式和排序去重
rows = [
    {"name": "Bob", "active": True},
    {"name": "Ana"},
    {"name": "Ana", "active": True},
    {"name": "Bob", "active": True},
]
names = [row["name"] for row in rows if row.get("active", False)]
print(names, sorted(set(names)))

# 题目：两个列表分别是什么？缺少 active 的记录如何处理？
# 标准答案：['Bob', 'Ana', 'Bob'] 和 ['Ana', 'Bob']。
# 解析：缺少 active 时 get() 返回 False，条件筛掉该记录。set 去重，sorted 排序。


# ----------------------------------------------------------------------
# 第 3 题｜枚举、配对与比较
numbers = [5, 8, 3]
letters = ["a", "b"]
print(list(enumerate(letters, start=1)))
print(list(zip(letters, numbers)))
print((1, 4) < (2, 0))

# 题目：三行分别输出什么？zip 为什么没用上 3？
# 标准答案：[(1, 'a'), (2, 'b')]、[('a', 5), ('b', 8)]、True。
# 解析：enumerate 从指定索引开始。zip 默认在较短的输入耗尽时停止。
# 元组比较在第一项的 1 和 2 就分出大小。
