# 第 12 章测试｜虚拟环境和包
# https://docs.python.org/zh-cn/3.13/tutorial/venv.html

import subprocess
import sys


# ----------------------------------------------------------------------
# 第 1 题｜确认当前解释器
print(sys.prefix != sys.base_prefix, flush=True)

# 题目：用项目虚拟环境运行时结果是什么？不激活能运行吗？
# 标准答案：True。可以直接执行 python/.venv/bin/python。
# 解析：使用哪个解释器取决于实际执行路径。激活只是方便 shell 找到环境里的命令。


# ----------------------------------------------------------------------
# 第 2 题｜在当前环境查看已安装的包
subprocess.run([sys.executable, "-m", "pip", "list", "--disable-pip-version-check"], check=True)

# 题目：为什么用 sys.executable 而不是直接运行 pip 命令？
# 标准答案：它指向当前解释器，可以用这个解释器执行对应的 pip。
# 解析：shell 中的 pip 可能来自另一个环境。使用当前解释器避免混用。
