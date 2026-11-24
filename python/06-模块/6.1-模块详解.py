# 6.1 模块详解｜官方教程要点
# https://docs.python.org/zh-cn/3.13/tutorial/modules.html#more-on-modules

import sys


# 6.1 导入模块、导入成员和别名。每个模块有自己的命名空间。
import fibo
import fibo as fibonacci
from fibo import fib2 as fibonacci_list

print(fibo.fib2(10), fibonacci is fibo, fibonacci_list is fibo.fib2)

# 题目：两种 import 会各执行一遍 fibo.py 吗？怎样用别名调用函数？
# 标准答案：普通重复导入复用已加载的模块。可用 fibonacci.fib2(10) 调用。
# 解析：Python 在 sys.modules 中缓存模块对象。as 只改变当前文件里的绑定名。


# ----------------------------------------------------------------------
# 6.1.1–6.1.3 执行方式、搜索路径和字节码缓存。
# 导入时模块的 __name__ 是模块名，作为程序入口运行时是 '__main__'。
# 在本目录运行 python -m fibo 10，也可以运行 python fibo.py 10。
# 导入通常从内置模块和 sys.path 查找。脚本所在目录（或交互时当前目录）、
# PYTHONPATH 与安装相关目录都可能在搜索路径上。
# Python 通常将导入模块的字节码缓存到 __pycache__，用于加快后续加载。
print(fibo.__name__, __name__)
print(fibo is sys.modules["fibo"])

# 题目：直接运行本例时，两处 __name__ 分别是什么？导入 fibo 时会打印数列吗？
# 标准答案：分别是 fibo 和 __main__。导入时不会运行 fibo.py 的命令行入口。
# 解析：fibo.py 的入口由 if __name__ == '__main__' 保护，只有作为入口时才执行。
