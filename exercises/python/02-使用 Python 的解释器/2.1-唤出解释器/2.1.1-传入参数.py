# [2.1.1. 传入参数](https://docs.python.org/zh-cn/3.13/tutorial/interpreter.html#argument-passing)
# sys.argv[0] 是脚本路径，后面的元素是传给脚本的参数。
# 在 exercises/python 的终端运行（已激活 .venv）：
# python "02-使用 Python 的解释器/2.1-唤出解释器/2.1.1-传入参数.py" "hello world"
# 去掉 hello world 外层的引号，再观察参数数量。

import sys

print(sys.argv)
