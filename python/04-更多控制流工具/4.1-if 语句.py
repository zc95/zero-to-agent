# 4.1 if 语句｜交互练习
# https://docs.python.org/zh-cn/3.13/tutorial/controlflow.html#if-statements
# 可以选中单题运行，先写预测，再观察实际输出。

# 第 01 题｜预测输出并说出检查了哪些条件
score = 80

if score >= 90:
    print("优秀")
elif score >= 60:
    print("及格")
else:
    print("继续练习")

print("评分结束")

# 答案：依次打印「及格」「评分结束」，检查两个条件。
# 解析：80 >= 90 为假，继续检查 80 >= 60。第二个条件为真，
# 打印「及格」并跳过 else。最后一条 print 在条件语句外，照常执行。

# 第 02 题｜只改分数，预测输出并判断第二个条件是否会被检查
score = 95

if score >= 90:
    print("优秀")
elif score >= 60:
    print("及格")
else:
    print("继续练习")

print("评分结束")

# 答案：依次打印「优秀」「评分结束」。程序跳过第二个条件。
# 解析：95 >= 90 为真，先打印「优秀」。随后跳过 elif 和 else，
# 执行条件语句外的 print，打印「评分结束」。

# 第 03 题｜把 elif 改成独立的 if
# 按顺序预测输出，并判断 else 和哪个 if 配对。
score = 95

if score >= 90:
    print("优秀")

if score >= 60:
    print("及格")
else:
    print("继续练习")

print("评分结束")

# 答案：依次打印「优秀」「及格」「评分结束」。else 与第二个 if 配对。
# 解析：95 >= 90 为真，第一个 if 打印「优秀」。接着执行独立的第二个
# if，95 >= 60 也为真，因此打印「及格」并跳过对应的 else。最后打印
# 「评分结束」。
