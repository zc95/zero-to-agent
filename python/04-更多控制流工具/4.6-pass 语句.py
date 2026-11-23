# 4.6 pass 语句｜官方示例
# https://docs.python.org/zh-cn/3.13/tutorial/controlflow.html#pass-statements

# 示例 1：循环体只包含 pass。
# 以下代码会持续运行。可以单独在 Python 交互解释器中运行，按 Ctrl+C 停止。
# while True:
#     pass

# 解析：pass 不执行任何操作。执行完后回到 while 检查条件，
# True 始终为真，所以循环会继续，也不会打印任何内容。

# 示例 2：定义一个暂时没有内容的类。
class MyEmptyClass:
    pass

# 解析：类定义需要一个缩进的类体，pass 可以充当其中的一条语句。
# 只保留 class MyEmptyClass: 会因为缺少缩进的类体而报 IndentationError。

# 示例 3：给还没实现的函数占位。
def initlog(*args):
    pass   # 记得实现这个！

# 标准答案：调用 initlog() 时，屏幕上没有输出。
# 解析：函数体只有 pass，执行到这里不做任何操作，随后函数结束。

# 教程也提到可以用 ... 占位。它是省略号字面值，常被单独写在未实现的函数体中。
