# [2.2.1. 源文件的字符编码](https://docs.python.org/zh-cn/3.13/tutorial/interpreter.html#source-code-encoding)
# Python 默认用 UTF-8 读取源码。用 UTF-8 保存文件，就可以直接在字符串和注释里写中文。

print("你好，Python！")

# 官方示例中的编码声明和 shebang 写在源码开头。下面用缩进的注释展示它们。

# 编码声明的格式。把 encoding 换成实际使用的编码名，放在源码第一行。
#   # -*- coding: encoding -*-

# 例如，文件实际以 Windows-1252 保存时，第一行写成这样。
#   # -*- coding: cp1252 -*-

# 如果第一行是 shebang，编码声明可以放在第二行。
#   #!/usr/bin/env python3
#   # -*- coding: cp1252 -*-
