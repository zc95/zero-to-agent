# 4.5 循环的 else 子句｜官方示例
# https://docs.python.org/zh-cn/3.13/tutorial/controlflow.html#else-clauses-on-loops

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # 循环到底未找到一个因数
        print(n, 'is a prime number')

# 解析：else 和内层 for 对齐，内层循环没有执行 break 就会进入 else。
# n 为 2 时，range(2, 2) 没有任何候选。内层循环执行零次就正常结束，
# 因此仍然进入 else，打印 2 is a prime number。
# n 为 3 时，唯一的候选 x 为 2，余数为 1。内层循环跑完后，
# 执行 else，打印 3 is a prime number。
# n 为 4 或 6 时，第一个候选 x 为 2，余数为 0。先打印乘积，
# 再用 break 退出内层循环，跳过后续候选和 else。n 为 6 时打印 6 equals 2 * 3。

# while 也可以带 else。条件变为假，循环正常结束时会执行 else。
# 如果 break、return 或异常使循环提前结束，就会跳过循环的 else。
