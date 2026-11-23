# 4.2 for 语句｜官方示例
# https://docs.python.org/zh-cn/3.13/tutorial/controlflow.html#for-statements

# 示例 1：逐个打印单词和它的长度。
words = ["cat", "window", "defenestrate"]
for w in words:
    print(w, len(w))

# 循环执行三次，依次打印 cat 3、window 6、defenestrate 12。
# 第二次取到的是列表中的第二个元素 window，len(w) 为 6。

# 示例 2：遍历字典副本，从原字典移除不活跃的用户。
users = {"Hans": "active", "Éléonore": "inactive", "景太郎": "active"}

for user, status in users.copy().items():
    if status == "inactive":
        del users[user]

# copy() 创建外层字典的浅副本。items() 返回这个副本的键值对视图，
# 每轮把一对 (键, 值) 拆给 user 和 status。遇到 inactive 时，
# del 从原字典删掉 Éléonore，副本仍有三个条目，遍历可以继续。
# 循环结束后，原字典 users 只剩 Hans 和景太郎。

# 示例 2 的另一种写法：新建字典，只收集活跃用户。
# 重新初始化 users，让这段可以用同一份初始数据单独运行。
users = {"Hans": "active", "Éléonore": "inactive", "景太郎": "active"}

active_users = {}
for user, status in users.items():
    if status == "active":
        active_users[user] = status

# 这一段直接遍历原字典的键值对，写入的是另一个字典 active_users。
# active_users 收集 Hans 和景太郎，原字典 users 仍保留三个用户。

# 补充 demo 1：修改原字典后，比较原字典和副本。
demo_users = {"Hans": "active", "Éléonore": "inactive"}
snapshot = demo_users.copy()

demo_users["Hans"] = "inactive"
del demo_users["Éléonore"]

print(demo_users)
print(snapshot)

# demo_users 打印 {'Hans': 'inactive'}。
# snapshot 打印 {'Hans': 'active', 'Éléonore': 'inactive'}。
# 修改 Hans 的值和删除 Éléonore 都发生在原字典，副本保留原来的条目。

# 补充 demo 2：用 items() 逐对读取姓名和状态。
demo_users = {"Hans": "active", "Éléonore": "inactive"}

for name, status in demo_users.items():
    print(name, status)

# 标准答案：依次输出两行。
# Hans active
# Éléonore inactive
# 解析：items() 每轮给出一对 (键, 值)，分别赋给 name 和 status。
# 第一轮 name 是 Hans，status 是 active；第二轮是 Éléonore 和 inactive。
# print(name, status) 用一个空格隔开两个值，每轮输出一行。

# 补充 demo 3：比较来自原字典和副本的视图。
demo_users = {"Hans": "active"}
live_items = demo_users.items()
copied_items = demo_users.copy().items()

demo_users["Éléonore"] = "inactive"

print(list(live_items))
print(list(copied_items))

# 标准答案：依次输出两行。
# [('Hans', 'active'), ('Éléonore', 'inactive')]
# [('Hans', 'active')]
# 解析：live_items 是原字典的视图。添加 Éléonore 后，再把视图转成列表，
# 就能看到两个条目。copied_items 是副本的视图，副本只保留复制时的 Hans。
