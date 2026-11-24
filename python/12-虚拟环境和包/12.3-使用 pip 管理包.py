# 12.3 使用 pip 管理包｜官方教程要点
# https://docs.python.org/zh-cn/3.13/tutorial/venv.html#managing-packages-with-pip

import subprocess
import sys

# 知识点：python -m pip 使用当前解释器对应的 pip。
# 以下命令按需要在练习环境中运行：
# python -m pip install 包名
# python -m pip show 包名
# python -m pip list
# python -m pip uninstall 包名
# python -m pip freeze > requirements.txt
# python -m pip install -r requirements.txt
subprocess.run([sys.executable, "-m", "pip", "--version"], check=True)

# 题目：怎样记录当前环境的第三方依赖，再在新环境安装？
# 标准答案：用 python -m pip freeze > requirements.txt 记录，
# 再用新环境的 python -m pip install -r requirements.txt 安装。
# 解析：freeze 输出已安装包的版本信息。使用 -m pip 可把包安装到所选解释器的环境。
