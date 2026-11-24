# 4.9.4 任意实参列表｜官方示例
# https://docs.python.org/zh-cn/3.13/tutorial/controlflow.html#arbitrary-argument-lists

from io import StringIO


# 示例 1：普通形参可以放在 *args 前面。
def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))


# StringIO 可以像文件一样接收文本。getvalue() 取出写入的内容。
output = StringIO()
write_multiple_items(output, ", ", "earth", "mars", "venus")
print(output.getvalue())  # earth, mars, venus
# 前两个位置实参分别给 file 和 separator。
# 剩下的三个字符串被收进 args，组成元组 ("earth", "mars", "venus")。


# 示例 2：*args 后面的 sep 要按名字传，省略时用默认值 "/"。
def concat(*args, sep="/"):
    return sep.join(args)


print(concat("earth", "mars", "venus"))  # earth/mars/venus
print(concat("earth", "mars", "venus", sep="."))  # earth.mars.venus
# sep.join(args) 把 sep 放在相邻字符串之间，再拼成一个字符串。

# 题目：下面这次调用中，args 和 sep 分别是什么？会打印什么？
# print(concat("earth", "mars", "."))
# 标准答案：args = ("earth", "mars", ".")，sep = "/"，打印 earth/mars/.。
# 解析：三个值都按位置传入，因此全被 *args 收进元组。sep 在 *args 后面，
# 只能按名字传。这次省略了 sep，join() 就用默认的 "/" 连接这三个字符串。
