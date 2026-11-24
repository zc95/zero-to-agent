# 第 7 章测试｜输入与输出
# https://docs.python.org/zh-cn/3.13/tutorial/inputoutput.html

import json
from io import StringIO


# ----------------------------------------------------------------------
# 第 1 题｜格式化文本
name, count = "任务", 3
print(f"{name}: {count:02d}")

# 题目：打印什么？02d 是什么作用？
# 标准答案：打印 任务: 03。02d 按十进制显示整数，最少两位，左边补零。
# 解析：花括号先读取变量，再按冒号后面的格式说明符格式化。


# ----------------------------------------------------------------------
# 第 2 题｜JSON 与文件对象
with StringIO() as file:
    json.dump({"ids": [1, 2]}, file)
    file.seek(0)
    print(json.load(file)["ids"])

# 题目：输出什么？为什么要调用 seek(0)？
# 标准答案：输出 [1, 2]。写入后的位置在末尾，seek(0) 把读写位置移回开头。
# 解析：StringIO 像文本文件一样保存内容。json.load() 从当前位置读取。
