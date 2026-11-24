# 5.4 集合｜官方教程要点
# https://docs.python.org/zh-cn/3.13/tutorial/datastructures.html#sets

# 知识点：集合：元素不重复，适合成员测试和集合运算。空集合写成 set()。
basket = {"apple", "orange", "apple", "pear", "orange", "banana"}
print("orange" in basket, "crabgrass" in basket)
a = set("abracadabra")
b = set("alacazam")
print(sorted(a - b), sorted(a | b), sorted(a & b), sorted(a ^ b))
print(sorted({letter for letter in "abracadabra" if letter not in "abc"}))

# 题目：a & b 和 a ^ b 有什么区别？为什么显示前用了 sorted()？
# 标准答案：& 保留共有元素，^ 保留只属于其中一边的元素。sorted() 让展示顺序固定。
# 解析：集合按成员关系工作，不能用索引读取。本例排序后输出列表，方便核对。
