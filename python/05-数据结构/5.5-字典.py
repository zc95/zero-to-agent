# 5.5 字典｜官方教程要点
# https://docs.python.org/zh-cn/3.13/tutorial/datastructures.html#dictionaries

# 知识点：字典：使用可哈希的键查值，保持键的插入顺序。缺失键可用 get() 处理。
tel = {"jack": 4098, "sape": 4139}
tel["guido"] = 4127
del tel["sape"]
tel["irv"] = 4127
print(tel["jack"], list(tel), sorted(tel), tel.get("sape"))
print("guido" in tel, "jack" not in tel)
print(dict([("sape", 4139), ("guido", 4127), ("jack", 4098)]))
print({number: number**2 for number in (2, 4, 6)})
print(dict(sape=4139, guido=4127, jack=4098))

# 题目：list(tel) 的元素是什么？tel.get("sape") 返回什么？直接用 [] 呢？
# 标准答案：list(tel) 得到 ['jack', 'guido', 'irv']。get() 返回 None，直接索引报 KeyError。
# 解析：遍历字典默认取键。get() 可以给缺失键指定默认值，未指定时用 None。
