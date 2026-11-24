# 第 4 章测试｜更多控制流工具
# https://docs.python.org/zh-cn/3.13/tutorial/controlflow.html
# 每题附标准答案和解析。可以运行整个文件，也可以选中单题运行。


# ----------------------------------------------------------------------
# 第 1 题｜if、range()、continue、break 和循环 else
def show_first_positive(values):
    for value in values:
        if value <= 0:
            continue
        print(value)
        break
    else:
        print("无正数")


show_first_positive([-2, 0, 3, 4])
show_first_positive(range(-2, 0))

# 题目：两次调用分别打印什么？哪一次执行 for 的 else？
# 标准答案：依次打印 3 和 无正数。第二次调用执行 else。
# 解析：第一次跳过 -2、0，打印 3 后 break，跳过 else，也不会检查 4。
# 第二次只遍历 -2、-1，两轮都 continue，循环正常结束后执行 else。


# ----------------------------------------------------------------------
# 第 2 题｜match 的变量绑定和守卫
point = (0, 5)
match point:
    case (0, y) if y > 0:
        print("正半轴", y)
    case (0, _):
        print("其余纵轴点")
    case _:
        print("其余点")

# 题目：当前坐标打印什么？如果第二项改成 -1，会命中哪个分支？
# 标准答案：当前打印 正半轴 5。改成 -1 时命中 case (0, _)。
# 解析：先匹配第一项 0 并绑定 y，再检查 y > 0。守卫为假时继续下一分支。


# ----------------------------------------------------------------------
# 第 3 题｜pass、函数别名与隐式返回
def pending():
    pass


run_later = pending
print(run_later())

# 题目：哪一行调用了函数？为什么输出是 None？
# 标准答案：print(run_later()) 的内层调用执行函数，外层打印 None。
# 解析：赋值让两个名字指向同一个函数。pass 不做任何操作，函数走到末尾
# 时隐式返回 None，外层 print() 将其显示。


# ----------------------------------------------------------------------
# 第 4 题｜默认值与列表的创建时机
def collect(value, items=None):
    if items is None:
        items = []
    items.append(value)
    return items


print(collect("a"))
print(collect("b"))

# 题目：两行分别打印什么？如果用 items=[] 作为默认参数，会有什么变化？
# 标准答案：当前打印 ['a'] 和 ['b']。换成默认列表后第二行会打印 ['a', 'b']。
# 解析：None 会让每次省略 items 的调用新建列表。默认列表在 def 执行时只创建
# 一次，后续省略 items 的调用共享它。


# ----------------------------------------------------------------------
# 第 5 题｜仅位置参数、仅关键字参数、收集与展开实参
def describe(first, /, *items, title, **options):
    return first, items, title, options


values = ["a", "b", "c"]
settings = {"title": "demo", "visible": True}
print(describe(*values, **settings))

# 题目：四个形参各是什么值？first 和 title 各允许哪种传法？
# 标准答案：first = 'a'，items = ('b', 'c')，title = 'demo'，
# options = {'visible': True}。first 只接受位置实参，title 只接受关键字实参。
# 解析：调用里的 * 和 ** 分别展开列表和字典。定义里的 *items 与 **options
# 分别收集剩余的位置实参和关键字实参。


# ----------------------------------------------------------------------
# 第 6 题｜lambda 作为排序依据
labels = [(3, "beta"), (1, "alpha"), (2, "gamma")]
labels.sort(key=lambda item: item[1])
print(labels)

# 题目：排序后输出什么？
# 标准答案：[(1, 'alpha'), (3, 'beta'), (2, 'gamma')]。
# 解析：key 函数返回每个元组的第二项，排序依据是字符串，整个元组一起移动。


# ----------------------------------------------------------------------
# 第 7 题｜文档字符串、函数注解与编码风格
def double_value(value: int) -> int:
    """Return twice the given value."""
    return value * 2


print(double_value(3))

# 题目：调用打印什么？在哪里读取文档字符串和类型注解？
# 标准答案：打印 6。文档从 double_value.__doc__ 读取，注解从
# double_value.__annotations__ 读取。
# 解析：函数用 return 传回结果，调用方用 print() 显示。docstring 说明用途，
# int 注解记录预期类型。函数名、四空格缩进和运算符间距遵循 PEP 8 的常见约定。
