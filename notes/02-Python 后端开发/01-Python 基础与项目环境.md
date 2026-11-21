# Python 基础与项目环境

## macOS 环境

- [Python 官方下载（macOS）](https://www.python.org/downloads/macos/)。已有可用的 Python 3 时，先用 `python3 --version` 看版本。跟做项目时，按项目声明的 Python 版本配置。
- [虚拟环境 venv（中文）](https://docs.python.org/zh-cn/3/library/venv.html)。在练习目录创建独立环境，依赖装在该环境里。
- [uv 官方安装指南](https://docs.astral.sh/uv/getting-started/installation/)。等碰到使用 uv 的项目时再查。

```sh
python3 --version
python3 -m venv .venv
source .venv/bin/activate
python -m pip --version
```

## 官方教程

- [Python 3.13 官方中文教程](https://docs.python.org/zh-cn/3.13/tutorial/index.html)。按官方章节顺序学，熟悉的内容用一个小例子快速复习。
- [本地练习目录](<../../exercises/python/>)。按教程章节查找练习，官方链接和说明在各节文件顶部。
