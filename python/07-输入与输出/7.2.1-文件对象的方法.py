# 7.2.1 文件对象的方法｜官方教程要点
# https://docs.python.org/zh-cn/3.13/tutorial/inputoutput.html#methods-of-file-objects

from pathlib import Path
from tempfile import TemporaryDirectory

# 知识点：w 写入并覆盖，a 追加，r 读取。with 退出时关闭文件。
with TemporaryDirectory() as directory:
    path = Path(directory) / "tasks.txt"
    with path.open("w", encoding="utf-8") as file:
        file.write("建表\n")
    with path.open("a", encoding="utf-8") as file:
        file.write("写查询\n")
    with path.open(encoding="utf-8") as file:
        print([line.rstrip("\n") for line in file])
    print(file.closed)

# 题目：为什么读到两行？最后一行打印什么？
# 标准答案：a 把第二行追加到末尾。读取打印 ['建表', '写查询']，最后打印 True。
# 解析：迭代文本文件逐行读取。退出 with 后，文件对象仍存在，但已经关闭。
