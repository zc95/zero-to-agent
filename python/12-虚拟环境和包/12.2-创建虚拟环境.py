# 12.2 创建虚拟环境｜官方教程要点
# https://docs.python.org/zh-cn/3.13/tutorial/venv.html#creating-virtual-environments

import sys

# 知识点：虚拟环境有独立解释器入口和第三方包安装位置。
# 在新练习目录中运行 python3 -m venv .venv。macOS/Linux 可执行
# source .venv/bin/activate，结束后执行 deactivate。
# 激活是修改当前 shell 的 PATH。也可直接运行 .venv/bin/python。
print(sys.prefix != sys.base_prefix)

# 题目：用本仓库的 python/.venv/bin/python 运行时，结果是什么？
# 标准答案：True，当前解释器在虚拟环境中。
# 解析：sys.prefix 指向环境，sys.base_prefix 指向创建它的基础 Python。
