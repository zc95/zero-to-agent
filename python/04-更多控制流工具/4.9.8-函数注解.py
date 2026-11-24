# 4.9.8 函数注解｜官方示例
# https://docs.python.org/zh-cn/3.13/tutorial/controlflow.html#function-annotations


# ----------------------------------------------------------------------
# 示例 1：给参数和返回值添加类型注解。
# 知识点：参数名后的 : str 标注预期类型，-> str 标注预期返回类型。
# 注解保存在 __annotations__ 中。注解本身不会在调用时检查或转换实参。
def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs


# 教程在交互解释器中显示返回值，这里用 print() 显示。
print(f('spam'))


# 题目：f('spam') 中的 eggs 用什么值？函数返回什么？注解记录了哪些类型？
# 标准答案：eggs 用默认值 'eggs'，返回 'spam and eggs'。
# ham、eggs 和 return 对应的注解都是 str。
# 解析：只传了一个位置实参，'spam' 给 ham。eggs 的注解是 str，默认值由 = 指定。
# 函数体先显示注解和参数，再拼接字符串并返回，最后由外层的 print() 显示结果。
