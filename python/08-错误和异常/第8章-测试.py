# 第 8 章测试｜错误和异常
# https://docs.python.org/zh-cn/3.13/tutorial/errors.html


# ----------------------------------------------------------------------
# 第 1 题｜选择处理分支
try:
    print(int("oops"))
except ValueError:
    print("格式错误")
else:
    print("转换成功")
finally:
    print("结束")

# 题目：输出哪两行？为什么没有执行 else？
# 标准答案：格式错误、结束。
# 解析：int() 抛出 ValueError，进入 except。else 只在 try 正常结束时执行。


# ----------------------------------------------------------------------
# 第 2 题｜主动抛出与传播
def require_name(name):
    if not name:
        raise ValueError("缺少名称")
    return name


try:
    require_name("")
except ValueError as error:
    print(error)

# 题目：空字符串触发什么异常？由谁处理？
# 标准答案：触发 ValueError，由调用方的 except 处理，打印 缺少名称。
# 解析：异常沿调用链向外传播，直到遇到能匹配它的处理器。
