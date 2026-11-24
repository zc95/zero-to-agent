# 8.4 触发异常｜官方教程要点
# https://docs.python.org/zh-cn/3.13/tutorial/errors.html#raising-exceptions

# 知识点：raise 主动抛出异常。except 里单独写 raise 可以重新抛出当前异常。
def validate_limit(limit):
    if limit < 1:
        raise ValueError("limit 至少为 1")
    return limit


try:
    validate_limit(0)
except ValueError as error:
    print(error)

# 题目：validate_limit(0) 返回了什么？error 绑定了什么？
# 标准答案：函数抛出 ValueError，error 是这个异常对象，打印其消息。
# 解析：raise 中断函数的正常流程，执行直接跳到能处理该异常的 except。
