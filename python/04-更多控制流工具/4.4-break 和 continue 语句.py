# 4.4 break 和 continue 语句｜官方示例
# https://docs.python.org/zh-cn/3.13/tutorial/controlflow.html#break-and-continue-statements

# 示例 1：找到因数后，用 break 结束内层循环。
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} equals {x} * {n//x}")
            break

# 输出依次为：
# 4 equals 2 * 2
# 6 equals 2 * 3
# 8 equals 2 * 4
# 9 equals 3 * 3
# 解析：n 为 4 时，先试 x 为 2。4 % 2 等于 0，打印后执行 break，
# 跳出内层循环，跳过 x 为 3 的检查。外层循环继续取下一个 n，也就是 5。

# 示例 2：遇到偶数时，用 continue 跳到下一轮。
for num in range(2, 10):
    if num % 2 == 0:
        print(f"Found an even number {num}")
        continue
    print(f"Found an odd number {num}")

# 前两轮依次输出：
# Found an even number 2
# Found an odd number 3
# 解析：num 为 2 时，打印后遇到 continue，跳过本轮最后的 print。
# 下一轮 num 为 3，if 条件为假，直接执行最后的 print。
# 其余各轮遵循同样的规则，每个数只打印一行。
