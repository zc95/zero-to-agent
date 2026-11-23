# 4.3 range() 函数｜官方示例
# https://docs.python.org/zh-cn/3.13/tutorial/controlflow.html#the-range-function

# 示例 1：用 range() 生成循环中的整数。
for i in range(5):
    print(i)

# 答案：依次输出 0、1、2、3、4，每个数字占一行。
# 解析：range(5) 默认从 0 开始，每次加 1，终止值 5 不包含在内。

# 示例 2：指定起点、终止值和步长。
# 官方教程在交互解释器中直接输入表达式，这里用 print 显示结果。
print(list(range(5, 10)))
print(list(range(0, 10, 3)))
print(list(range(-10, -100, -30)))

# 答案：[5, 6, 7, 8, 9]、[0, 3, 6, 9]、[-10, -40, -70]。
# 解析：第一行从 5 开始每次加 1，第二行从 0 开始每次加 3。
# 第三行从 -10 开始每次减 30。下一步正好到 -100，终止值不包含在内。

# 示例 3：用 range() 和 len() 遍历列表索引。
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

# 答案：最后一轮 i 为 4，打印 4 lamb。
# 解析：列表有 5 项，range(len(a)) 依次产生索引 0 到 4。
# 最后一轮取出 a[4]，也就是第五个元素 lamb。
# 教程也提到 enumerate() 可以同时拿到索引和元素，第 5.6 节会讲到。

# 示例 4：直接显示 range 对象，再把 range 交给 sum()。
print(range(10))
print(sum(range(4)))

# 答案：第一行打印 range(0, 10)，第二行打印 6。
# 解析：直接打印 range 会显示对象的表示形式。sum() 遍历 range(4)，
# 依次取出 0、1、2、3，相加得到 6。
