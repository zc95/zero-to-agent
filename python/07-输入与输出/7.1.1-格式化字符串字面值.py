# 7.1.1 格式化字符串字面值｜官方教程要点
# https://docs.python.org/zh-cn/3.13/tutorial/inputoutput.html#formatted-string-literals

from math import pi

# 知识点：f-string 用花括号插入表达式的值，冒号后可指定格式。
print(f"{pi:.3f}")

# 题目：这行打印什么？.3f 的作用是什么？
# 标准答案：打印 3.142。按定点小数格式输出，保留小数点后三位。
# 解析：pi 的原值参与格式化，实际显示的是舍入后的文本。
