# 5.6 循环技巧｜官方教程要点
# https://docs.python.org/zh-cn/3.13/tutorial/datastructures.html#looping-techniques

# 知识点：循环技巧：items()、enumerate()、zip() 和按序遍历。
from math import isnan

knights = {"gallahad": "the pure", "robin": "the brave"}
for name, description in knights.items():
    print(name, description)

for index, value in enumerate(["tic", "tac", "toe"]):
    print(index, value)

questions = ["name", "quest", "favorite color"]
answers = ["lancelot", "the holy grail", "blue"]
for question, answer in zip(questions, answers):
    print(question, answer)

print(list(reversed(range(1, 10, 2))))
fruits = ["apple", "orange", "apple", "pear", "banana"]
print(sorted(fruits), sorted(set(fruits)))
raw_data = [56.2, float("NaN"), 51.7, float("NaN"), 47.8]
filtered_data = [value for value in raw_data if not isnan(value)]
print(filtered_data)

# 题目：enumerate() 和 zip() 分别给每轮循环什么？怎样保留原列表的顺序？
# 标准答案：前者给索引和值，后者把多个可迭代对象同一位置的元素配成元组。
# 解析：sorted() 和列表推导式都可产生新列表。上面的排序和筛选保留了原列表。
