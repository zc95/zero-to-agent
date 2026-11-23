# 4.4 break 和 continue 语句｜官方示例
# https://docs.python.org/zh-cn/3.13/tutorial/controlflow.html#break-and-continue-statements

# 示例 1：找到因数后，用 break 结束内层循环。
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} equals {x} * {n//x}")
            break
