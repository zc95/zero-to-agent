# [3.1.2. 文本](https://docs.python.org/zh-cn/3.13/tutorial/introduction.html#text)
# 按官方示例的顺序练习。用 print() 显示表达式的结果，便于直接运行脚本。

# 字符串的类型是 str。单引号和双引号都可以定义字符串。
# 引号内出现同类引号时，可以用反斜杠转义，也可以换一种外层引号。
print('spam eggs')  # spam eggs
print("Paris rabbit got your back :)! Yay!")  # Paris rabbit got your back :)! Yay!
print('1975')  # 1975（这是字符串）

print('doesn\'t')  # doesn't
print("doesn't")  # doesn't
print('"Yes," they said.')  # "Yes," they said.
print("\"Yes,\" they said.")  # "Yes," they said.
print('"Isn\'t," they said.')  # "Isn't," they said.

# 交互模式下直接输入 s 会看到转义写法，print(s) 会显示实际的换行。
s = 'First line.\n Second line.'
# 在 >>> 提示符下输入 s，可以看到字符串的表示形式。
print(s)
# 输出两行：First line.
# 下一行是 Second line.，开头有一个空格。

# 普通字符串中的 \t 是制表符，\n 是换行。
# 原始字符串会保留 \t 和 \n 的反斜杠。末尾连续的反斜杠不能是奇数个。
print('C:\t his\n ame')  # 第一行是 C:、制表符和 his，第二行是 ame。
print(r'C:\this\name')  # C:\this\name，整行原样显示

# 三引号保留多行。开头的反斜杠去掉第一个换行。
# 输出从 Usage 起的三行帮助文本，末尾还有一个空行。
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

# * 重复字符串，+ 拼接字符串。紧挨着的字符串字面值会自动拼接。
print(3 * 'un' + 'ium')  # unununium
print('Py' 'thon')  # Python

text = ('Put several strings within parentheses '
        'to have them joined together.')
print(text)  # Put several strings within parentheses to have them joined together.

prefix = 'Py'

# 自动拼接适用于相邻字面值。变量或计算结果要用 + 来拼接。
# 这里用 compile() 演示两条语法错误，每条都输出 SyntaxError: invalid syntax。
for source in ("prefix 'thon'", "('un' * 3) 'ium'"):
    try:
        compile(source, '<示例>', 'exec')
    except SyntaxError as error:
        print(f"SyntaxError: {error.msg}")

print(prefix + 'thon')  # Python

# 索引每次取一个字符。正向从 0 开始，倒着数从 -1 开始。
# -0 和 0 相同，都表示第一个字符。
word = 'Python'
print(word[0])  # P，第一个字符
print(word[5])  # n，索引 5 是第六个字符
print(word[-1])  # n，最后一个字符
print(word[-2])  # o，倒数第二个字符
print(word[-6])  # P，倒数第六个字符

# 切片用 word[起点:终点] 取一段字符串，包含起点，终点在切片之外。
# 省略起点就从开头取，省略终点就取到末尾。
print(word[0:2])  # Py，取索引 0 和 1
print(word[2:5])  # tho，取索引 2、3 和 4
print(word[:2])  # Py，从开头取到索引 2 之前
print(word[4:])  # on，从索引 4 取到末尾
print(word[-2:])  # on，从倒数第二个字符取到末尾

print(word[:2] + word[2:])  # Python，在索引 2 处分开，再拼回去
print(word[:4] + word[4:])  # Python，在索引 4 处分开，再拼回去

# 切片边界可以理解为字符之间的位置。例如 0 到 2 之间是 Py。
#  0   1   2   3   4   5   6
#    P   y   t   h   o   n
# -6  -5  -4  -3  -2  -1

# 索引越界会报错，切片会把边界限制在字符串范围内。
try:
    print(word[42])  # 触发 IndexError: string index out of range
except IndexError as error:
    print(f"IndexError: {error}")

print(word[4:42])  # on，终点超出范围时取到末尾
print(word[42:])  # 空字符串，print() 会输出一个空行

# 字符串不可变。给单个索引或一段切片赋值都会触发 TypeError。
# 两次的错误信息都是 'str' object does not support item assignment。
try:
    word[0] = 'J'  # pyright: ignore[reportIndexIssue]
except TypeError as error:
    print(f"TypeError: {error}")

try:
    word[2:] = 'py'  # pyright: ignore[reportIndexIssue]
except TypeError as error:
    print(f"TypeError: {error}")

# 可以用切片拼出新的字符串。
print('J' + word[1:])  # Jython
print(word[:2] + 'py')  # Pypy

s = 'supercalifragilisticexpialidocious'
print(len(s))  # 34，字符串的字符数
