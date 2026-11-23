# 4.7 match 语句｜官方示例
# https://docs.python.org/zh-cn/3.13/tutorial/controlflow.html#match-statements
# 本节 12 道题均已核对。每个示例下方附有题目、标准答案和解析。


# ----------------------------------------------------------------------
# 示例 1：按 HTTP 状态码匹配对应的消息。
# 知识点：match 只执行第一个匹配的 case。_ 是不绑定变量的通配模式。
# 如果没有任何分支匹配，match 结束后继续执行后面的代码。
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"


# 题目：http_error(404) 和 http_error(500) 分别命中哪个 case，返回什么？
# 答：404 命中 case 404，返回 Not found。500 命中 case _，返回
#     Something's wrong with the internet。
# 解析：match 只执行第一个匹配的分支。500 与前三个状态码都不等，
#       由最后的通配模式接住。


# ----------------------------------------------------------------------
# 示例 2：用 | 把多个字面值放进同一个 case。
# 知识点：| 连接多个备选模式，匹配其中任意一个即可进入同一分支。
# 教程只给出了 case 片段。这里补上函数和 match，方便单独调用。
def http_error_grouped(status):
    match status:
        case 401 | 403 | 404:
            return "Not allowed"


# 题目：http_error_grouped() 分别接收 401、403 和 404，会返回什么？
# 答：三个调用都返回 Not allowed。
# 解析：| 把三个备选值放进同一个 case，任意一个匹配就执行该分支。


# ----------------------------------------------------------------------
# 示例 3：在匹配坐标时，把元组里的值绑定到变量。
# 知识点：数字按值匹配，单独的变量名捕获对应位置的值。
# 教程给出的是匹配片段，这里先给 point 一个值，方便运行。
point = (0, 5)
match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")


# 题目：示例 3 的 (0, 5) 会命中哪个 case？打印什么？
# 答：命中 case (0, y)，打印 Y=5。
# 解析：case (0, 0) 的第二项不匹配。下一个模式将第二项 5 绑定给 y，
#       命中后跳过其余分支，包括 case (x, y)。


# ----------------------------------------------------------------------
# 示例 4：用类模式匹配 Point 对象的属性。
# 知识点：Point(x=0, y=y) 先检查对象类型，再匹配属性。y= 左边是属性名，
# 右边的 y 是接收属性值的变量。Point() 只检查对象类型。
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")


# 调用示例，便于直接观察匹配结果。
where_is(Point(0, 7))


# 题目：where_is(Point(0, 7)) 会命中哪个 case？打印什么？
# 答：命中 case Point(x=0, y=y)，打印 Y=7。
# 解析：对象的 y 属性为 7，跳过要求 y 为 0 的第一个分支。
#       第二个分支要求 x 为 0，并把 y 属性值绑定给变量 y。


# ----------------------------------------------------------------------
# 示例 5：比较官方教程列出的四种等价类模式。
# 知识点：__match_args__ 指定类模式的位置参数对应哪些属性。
# 只有 var 这样的单独名称会捕获值。Point、x= 和 y= 分别用来指定类和属性。
# 带点号的名称也不捕获值。有些类（如按默认方式定义的 dataclass）已有属性顺序。
# 这里给前面的 Point 补上属性顺序，让四个模式可以分别运行。
Point.__match_args__ = ("x", "y")
point = Point(1, 7)

match point:
    case Point(1, var):
        print(var)

match point:
    case Point(1, y=var):
        print(var)

match point:
    case Point(x=1, y=var):
        print(var)

match point:
    case Point(y=var, x=1):
        print(var)


# 题目：Point(1, 7) 用 Point(1, var) 匹配时，1 检查哪个属性？var 是多少？
# 答：1 检查 x 属性，var 得到 7。
# 解析：__match_args__ 指定位置顺序为 ("x", "y")，所以 Point(1, var)
#       等同于 Point(x=1, y=var)。x 的值匹配到 1，y 的值 7 被绑定给 var。


# ----------------------------------------------------------------------
# 示例 6：在序列模式里嵌入类模式。
# 知识点：外层检查序列的元素个数，内层匹配各元素的类型和属性。
# 沿用已设置 __match_args__ 的 Point，补上 points 供运行。
points = [Point(0, 2), Point(0, 5)]
match points:
    case []:
        print("No points")
    case [Point(0, 0)]:
        print("The origin")
    case [Point(x, y)]:
        print(f"Single point {x}, {y}")
    case [Point(0, y1), Point(0, y2)]:
        print(f"Two on the Y axis at {y1}, {y2}")
    case _:
        print("Something else")


# 题目：示例 6 的 points 命中哪个 case？y1 和 y2 是多少？
# 答：命中 case [Point(0, y1), Point(0, y2)]，y1 为 2，y2 为 5。
# 解析：列表有两个元素，跳过前面要求零个或一个元素的模式。两个 Point 的
#       x 都为 0，各自的 y 依次绑定给 y1、y2，打印 Two on the Y axis at 2, 5。


# ----------------------------------------------------------------------
# 示例 7：用 if 给模式加守卫。
# 知识点：先匹配并绑定变量，再检查守卫。守卫为假时继续尝试下一分支。
point = Point(2, 5)
match point:
    case Point(x, y) if x == y:
        print(f"Y=X at {x}")
    case Point(x, y):
        print(f"Not on the diagonal")


# 题目：示例 7 的 Point(2, 5) 命中哪个 case？为什么？
# 答：执行第二个 case Point(x, y)，打印 Not on the diagonal。
# 解析：第一个模式匹配成功，先绑定 x = 2、y = 5。守卫 x == y 为假，
#       因此跳过第一个分支的代码。第二个模式匹配成功，直接执行分支。


# ----------------------------------------------------------------------
# 示例 8：序列模式与扩展解包（把教程里的模式放进可运行的 match）。
# 知识点：模式用方括号或圆括号写都可以匹配列表和元组。字符串和迭代器
# 不参加这种序列匹配。*rest 用列表收集余下的元素，*_ 忽略余下的元素。
values = [10, 20, 30, 40]
match values:
    case [x, y, *rest]:
        print(x, y, rest)

match values:
    case (x, y, *rest):
        print(x, y, rest)

match values:
    case (x, y, *_):
        print(x, y)


# 题目：示例 8 的前三个变量 x、y、rest 分别是什么？*_ 忽略了哪些值？
# 答：x = 10，y = 20，rest = [30, 40]。*_ 忽略 30 和 40。
# 解析：x 和 y 分别接收前两项。*rest 把余下的项收集为列表并绑定给 rest。
#       *_ 允许后面有任意多项，并跳过这些项的绑定。


# ----------------------------------------------------------------------
# 示例 9：用映射模式从字典里取值（由教程中的模式补成可运行示例）。
# 知识点：模式列出的键必须存在，其他键可以忽略，也可以用 **rest 收集。
# **_ 不合法。想忽略其他键时，省略 **rest 就行。
connection = {"bandwidth": 100, "latency": 20, "region": "east"}
match connection:
    case {"bandwidth": b, "latency": l}:
        print(b, l)

match connection:
    case {"bandwidth": b, "latency": l, **rest}:
        print(b, l, rest)


# 题目：示例 9 的 b、l、rest 分别是什么？
# 答：b = 100，l = 20，rest = {"region": "east"}。
# 解析：两个模式都从 bandwidth 和 latency 键取值，分别绑定给 b 和 l。
#       第一个模式忽略额外的 region 键。第二个模式用 **rest 将剩余键值对
#       收集到一个新字典，再绑定给 rest。


# ----------------------------------------------------------------------
# 示例 10：用 as 捕获整个子模式的匹配对象。
# 知识点：as 左边照常匹配并捕获属性，右边的 p2 绑定匹配到的整个对象。
# 教程用 ... 留空分支体。这里打印坐标，方便核对 p2 指向哪个点。
points = (Point(1, 2), Point(3, 4))
match points:
    case (Point(x1, y1), Point(x2, y2) as p2):
        print(p2.x, p2.y)


# 题目：示例 10 的 p2 是第几个 Point？它的坐标是什么？
# 答：p2 是第二个 Point，坐标为 (3, 4)。最后打印 3 4。
# 解析：Point(x2, y2) 匹配第二个元素，分别把 3 和 4 绑定给 x2 和 y2。
#       as p2 同时把这个 Point 对象绑定给 p2，所以可以读取 p2.x 和 p2.y。


# ----------------------------------------------------------------------
# 示例 11：检查字面值的匹配方式（给教程中的规则加一段验证代码）。
# 知识点：大多数字面值按相等比较，True、False 和 None 按对象身份匹配。
value = 1
match value:
    case True:
        print("Matched True")
    case 1:
        print("Matched 1")


# 题目：示例 11 的整数 1 命中 case True 还是 case 1？
# 答：命中 case 1，打印 Matched 1。
# 解析：case True 按对象身份匹配，整数 1 与 True 是不同对象，跳过该分支。
#       case 1 按值比较，整数 1 等于模式中的 1，因此匹配成功。


# ----------------------------------------------------------------------
# 示例 12：用带点号的枚举成员匹配常量。
# 知识点：Color.BLUE 是值模式。单写 BLUE 会被当成接收匹配值的变量名。
from enum import Enum


class Color(Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"


# 单独调用 choose_color() 来试官方的交互示例。整文件运行时跳过输入。
def choose_color():
    color = Color(input("Enter your choice of 'red', 'blue' or 'green': "))

    match color:
        case Color.RED:
            print("I see red!")
        case Color.GREEN:
            print("Grass is green")
        case Color.BLUE:
            print("I'm feeling the blues :(")


# 题目：调用 choose_color() 并输入 blue，命中哪个 case？
# 答：命中 case Color.BLUE，打印 "I'm feeling the blues :("。
# 解析：input() 读到字符串 "blue"，Color("blue") 得到枚举成员 Color.BLUE。
#       match 将这个枚举成员与各分支的枚举成员比较，命中 Color.BLUE。
