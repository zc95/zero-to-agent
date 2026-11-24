# 8.3 异常的处理｜官方教程要点
# https://docs.python.org/zh-cn/3.13/tutorial/errors.html#handling-exceptions

# 知识点：try 里放可能失败的操作。except 捕获指定异常，else 在 try 成功时执行。
for raw in ("12", "bad"):
    try:
        number = int(raw)
    except ValueError:
        print("请输入整数")
    else:
        print(number + 1)

# 题目：两轮各打印什么？为什么用 except ValueError？
# 标准答案：先打印 13，再打印 请输入整数。
# 解析：第一轮转换成功，进入 else。第二轮转换抛出 ValueError，只运行对应的 except。
# 捕获具体类型会让其他意外异常继续向上传播。
