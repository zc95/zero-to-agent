# 从零开始学 AI Agent

从 Python 入门到 AI Agent 开发，记录学习路线、技术笔记和代码示例。涵盖 FastAPI、LLM、RAG、LangChain 和 LangGraph。

## 关键文件指引

- [Python 基础与项目环境](<notes/02-Python 后端开发/01-Python 基础与项目环境.md>) — macOS 环境配置和 Python 官方教程入口。
- [Python 练习](exercises/python/) — 按 Python 官方教程章节整理的代码示例和测试。
- [技术笔记](notes/) — Python 后端、大模型应用、Agent 开发、RAG 和工程化资料。

## 学习规划

### Python 基础与 HTTP

- [x] 第 1 章「课前甜点」笔记
- [x] 第 2 章「使用 Python 的解释器」笔记与示例
- [x] 第 3 章「Python 速览」示例与测试（33/33）
- [ ] 第 4 章控制流、函数与类型标注
- [ ] 第 5 章数据结构（已有列表推导式练习）
- [ ] 模块、异常、虚拟环境与依赖管理
- [ ] 文件与 JSON 读写、HTTP 请求与超时处理

### 大模型应用开发

- [ ] Transformer、自注意力、Token 与上下文窗口
- [ ] 模型 API 与结构化输出
- [ ] Prompt（提示词）设计、版本管理与评测
- [ ] Function Calling（函数调用）：工具定义、执行与结果回传

### 单 Agent

- [ ] 用 Python 实现 ReAct 循环，练习参数校验、工具异常与停止条件
- [ ] 用 LangChain 的 `create_agent` 构建单 Agent

### 检索增强生成（RAG）

- [ ] PDF 解析、文档切分、向量嵌入与检索
- [ ] 给 Agent 接入检索工具，练习原文引用与证据不足时的处理

### LangGraph 工作流与 MCP

- [ ] LangGraph 的状态、节点与条件分支
- [ ] 检查点、人工确认与断点恢复
- [ ] MCP 工具的封装与调用

### 工程化与部署

- [ ] FastAPI、Pydantic、异步 I/O 与 SSE 流式输出
- [ ] PostgreSQL 查询、表连接与事务
- [ ] pytest 回归测试、Agent 评测与执行日志
- [ ] Git、Docker 与项目文档

### 后续项目与选学

- [ ] 跑通一个完整 Agent 项目并独立实现一项功能
- [ ] Hermes Agent 的长期记忆、Skills 和工具调用（选学）
- [ ] 多 Agent 协作与效果评估（选学）
- [ ] LoRA 微调与效果对比（选学）
