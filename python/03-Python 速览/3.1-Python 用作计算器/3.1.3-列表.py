# [3.1.3. 列表](https://docs.python.org/zh-cn/3.13/tutorial/introduction.html#lists)
# 按官方顺序练习。脚本用 print() 显示每组示例的结果。

# 方括号定义列表。索引取一个元素，切片返回一个新列表。
squares = [1, 4, 9, 16, 25]
print(squares)  # [1, 4, 9, 16, 25]
print(squares[0])  # 1，第一个元素
print(squares[-1])  # 25，最后一个元素
print(squares[-3:])  # [9, 16, 25]，取最后三个元素

# + 把两个列表拼成一个新列表。
print(squares + [36, 49, 64, 81, 100])  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 列表可以原地修改。索引 3 指向第四个元素。
cubes = [1, 8, 27, 65, 125]
print(4 ** 3)  # 64
cubes[3] = 64
print(cubes)  # [1, 8, 27, 64, 125]

# append() 在末尾添加一个元素，类似 JS 数组的 push()。
cubes.append(216)
cubes.append(7 ** 3)
print(cubes)  # [1, 8, 27, 64, 125, 216, 343]

# 赋值后两个变量引用同一个列表。通过 rgba 添加元素，rgb 也能看到。
rgb = ["Red", "Green", "Blue"]
rgba = rgb
print(id(rgb) == id(rgba))  # True，两个变量引用同一个对象
rgba.append("Alph")
print(rgb)  # ['Red', 'Green', 'Blue', 'Alph']

# [:] 创建一个新的外层列表。这叫浅拷贝，列表中的对象仍然共享。
correct_rgba = rgba[:]
correct_rgba[-1] = "Alpha"
print(correct_rgba)  # ['Red', 'Green', 'Blue', 'Alpha']
print(rgba)  # ['Red', 'Green', 'Blue', 'Alph']，原列表的最后一项保留

# 切片赋值会原地替换一段元素，包含起点，排除终点。
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)  # ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters[2:5] = ['C', 'D', 'E']
print(letters)  # ['a', 'b', 'C', 'D', 'E', 'f', 'g']
letters[2:5] = []  # 删除索引 2、3、4 上的元素
print(letters)  # ['a', 'b', 'f', 'g']
letters[:] = []  # 清空原列表
print(letters)  # []

# len() 返回元素数量。
letters = ['a', 'b', 'c', 'd']
print(len(letters))  # 4

# 列表的元素也可以是列表。先取外层，再取内层。
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)  # [['a', 'b', 'c'], [1, 2, 3]]
print(x[0])  # ['a', 'b', 'c']
print(x[0][1])  # b，取第一个子列表的第二个元素
