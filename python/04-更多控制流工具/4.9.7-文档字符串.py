# 4.9.7 文档字符串｜官方示例
# https://docs.python.org/zh-cn/3.13/tutorial/controlflow.html#documentation-strings


# ----------------------------------------------------------------------
# 示例 1：定义多行文档字符串，用 __doc__ 读取。
# 知识点：函数体的第一条语句可以是文档字符串。首行简要说明用途，
# 英文摘要以大写字母开头，以句点结束。多行文档用空行分隔摘要和详情。
def my_function():
    """Do nothing, but document it.

    No, really, it doesn't do anything:

        >>> my_function()
        >>>
    """
    pass


print(my_function.__doc__)


# 题目：这行 print() 显示什么？它会调用 my_function() 吗？
# 标准答案：显示三引号里的文档字符串，首行是 Do nothing, but document it.
# 解析：my_function.__doc__ 读取函数对象上的属性。文档里面的交互示例是文字，
# 会随文档一起显示。整个过程没有调用 my_function()。
