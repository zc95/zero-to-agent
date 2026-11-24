# 8.7 定义清理操作｜官方教程要点
# https://docs.python.org/zh-cn/3.13/tutorial/errors.html#defining-clean-up-actions

# 知识点：finally 无论成功还是出现异常都会执行。支持 with 的资源优先用 with 管理。
def divide(a, b):
    try:
        return a / b
    finally:
        print("清理完成")


for denominator in (2, 0):
    try:
        print(divide(6, denominator))
    except ZeroDivisionError:
        print("不能除以 0")

# 题目：finally 在哪两次执行？正常调用的两行输出先后是什么？
# 标准答案：两次都执行。正常调用先打印 清理完成，再打印 3.0。
# 解析：除法结果准备返回时，先执行 finally。除零时先执行 finally，再传递异常。
