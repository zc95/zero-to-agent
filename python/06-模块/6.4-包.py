# 6.4 包｜官方教程要点
# https://docs.python.org/zh-cn/3.13/tutorial/modules.html#packages

# 6.4 普通包、相对导入和 __all__。
# 普通包有 __init__.py。命名空间包也可以没有它，并可分布在多个目录。
# 绝对导入从包名开始。包内的 . 表示当前包，.. 表示上一级包。
# __all__ 可控制 from package import * 的公开名称，平时优先显式导入。
from number_tools import fib_sum
from number_tools import series

print(fib_sum(10), series.fib2(10))

# 题目：fib_sum 通过哪个文件对外导出？包内的 from .series import fib2 从哪里导入？
# 标准答案：通过 number_tools/__init__.py 导出。从同一个包的 series.py 导入 fib2。
# 解析：__init__.py 初始化普通包。相对导入依赖包上下文，可通过包名导入或用 -m 运行模块。
