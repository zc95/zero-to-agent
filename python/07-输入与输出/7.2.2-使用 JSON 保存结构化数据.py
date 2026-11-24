# 7.2.2 使用 JSON 保存结构化数据｜官方教程要点
# https://docs.python.org/zh-cn/3.13/tutorial/inputoutput.html#saving-structured-data-with-json

import json
from pathlib import Path
from tempfile import TemporaryDirectory

# 知识点：dump/load 写入和读取文件对象，dumps/loads 在 Python 对象与字符串间转换。
tasks = [{"title": "写查询", "done": False}]
with TemporaryDirectory() as directory:
    path = Path(directory) / "tasks.json"
    with path.open("w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False)
    with path.open(encoding="utf-8") as file:
        payload = json.load(file)
    print(payload[0]["title"], payload[0]["done"])

# 题目：json.load() 返回什么类型的对象？第一条任务的 done 是什么？
# 标准答案：返回列表，元素是字典。done 是 Python 的 False。
# 解析：JSON 数组读回为 list，对象读回为 dict，布尔值 false 读回为 False。
