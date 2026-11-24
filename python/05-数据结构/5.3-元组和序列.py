# 5.3 元组和序列｜官方教程要点
# https://docs.python.org/zh-cn/3.13/tutorial/datastructures.html#tuples-and-sequences

# 知识点：元组和序列：元组固定位置不能重新赋值，里面的可变对象仍可修改。
point = (12345, 54321, "hello!")
first, second, greeting = point
print(first, second, greeting)
empty = ()
singleton = ("hello",)
coordinates = (point, (1, 2, 3))
mutable_items = ([1, 2], [3, 4])
mutable_items[0].append(5)
print(empty, singleton, coordinates, mutable_items)

# 题目：("hello") 和 ("hello",) 的类型一样吗？为什么元组里的列表能 append()？
# 标准答案：前者是字符串，后者是单元素元组。append() 修改的是元组引用的列表。
# 解析：创建单元素元组靠逗号。列表内容改变时，元组对应位置仍然指向原列表。
