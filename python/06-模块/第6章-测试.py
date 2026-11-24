# 第 6 章测试｜模块与包
# https://docs.python.org/zh-cn/3.13/tutorial/modules.html

import fibo as series
from fibo import fib2
from number_tools import fib_sum


# ----------------------------------------------------------------------
# 第 1 题｜导入模块与导入函数
print(series.fib2(4), fib2 is series.fib2)

# 题目：这行打印什么？两个函数名指向同一个对象吗？
# 标准答案：打印 [0, 1, 1, 2, 3] True，两个名字指向同一个函数对象。
# 解析：别名 series 指向 fibo 模块，from 导入直接把模块里的 fib2 绑定到本地名称。


# ----------------------------------------------------------------------
# 第 2 题｜模块作为程序入口
print(series.__name__, __name__)

# 题目：直接运行本脚本时这行打印什么？怎样运行 fibo 的入口？
# 标准答案：打印 fibo __main__。可从本目录运行 python -m fibo 4。
# 解析：作为程序入口运行的模块名为 __main__，普通导入保留原模块名。


# ----------------------------------------------------------------------
# 第 3 题｜包对外提供函数
print(fib_sum(4))

# 题目：输出什么？包内部哪个导入使用了相对路径？
# 标准答案：打印 7。number_tools/summary.py 用 from .series import fib2 导入。
# 解析：.series 代表同一包中的 series 模块。fib_sum 将小于 4 的数列求和。
