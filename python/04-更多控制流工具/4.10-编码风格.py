# 4.10 小插曲：编码风格
# https://docs.python.org/zh-cn/3.13/tutorial/controlflow.html#intermezzo-coding-style


# ----------------------------------------------------------------------
# 示例 1：把教程列出的 PEP 8 约定用在一段可运行的代码上。
# 知识点：通常用 4 个空格缩进，代码行不超过 79 个字符。用空行分隔
# 函数、类和较大的代码块，注释尽量独立成行，函数的用途可写成文档字符串。
# 运算符两侧和逗号后留空格，括号内侧紧贴内容，如 a = f(1, 2) + g(3, 4)。
# 类名用 UpperCamelCase，函数和方法名用小写加下划线，实例方法首参用 self。
# 面向多人或多语言环境时使用 UTF-8 或 ASCII 编码，标识符尽量只用 ASCII。
def add_numbers(left, right):
    """Return the sum of two numbers."""
    return left + right


total = add_numbers(2, 3)
print(total)


# 题目：脚本打印什么？找出函数名、缩进和空格分别遵循了什么约定。
# 标准答案：打印 5。add_numbers 用小写和下划线，函数体缩进 4 个空格。
# 解析：赋值和加法运算符两侧留空格，逗号后留一格，括号内侧紧贴实参。
