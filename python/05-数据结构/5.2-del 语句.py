# 5.2 del 语句｜官方教程要点
# https://docs.python.org/zh-cn/3.13/tutorial/datastructures.html#the-del-statement

# 知识点：del 语句：可删除单项、切片、全部内容或名称。
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)
del a[2:4]
print(a)
del a[:]
print(a)
del a
# print(a)  # 名称已经删除，单独运行会报 NameError。

# 题目：第二次删除之后剩下什么？最后的 del a 和 del a[:] 分别做什么？
# 标准答案：[1, 66.25, 1234.5]。del a 删除名称，del a[:] 清空列表。
# 解析：切片 [2:4] 删除这时处于索引 2 和 3 的两个 333，索引 4 保留。
