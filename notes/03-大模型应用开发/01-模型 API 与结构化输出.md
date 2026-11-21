# 模型 API 与结构化输出

## 知识点

- 大语言模型（large language model，LLM）、Token、上下文窗口
- 模型 API、消息角色、结构化输出（Structured Outputs）
- 提示词模板与版本管理，用固定样例检查改动前后的输出

## 官方资料

这里用 OpenAI API 的文档作示例。跟做其他模型服务的项目时，用该服务的官方 SDK 文档。

- [OpenAI API 关键概念（官方中文）](https://developers.openai.com/zh-Hans/api/docs/concepts)
- [OpenAI API 快速入门（官方中文）](https://developers.openai.com/zh-Hans/api/docs/quickstart) · [英文原文](https://developers.openai.com/api/docs/quickstart)。看 Python SDK 的安装和一次最小请求。
- [OpenAI 结构化输出（官方中文）](https://developers.openai.com/zh-Hans/api/docs/guides/structured-outputs) · [英文原文](https://developers.openai.com/api/docs/guides/structured-outputs)。练习为输入文本提取固定字段，理解 JSON Schema 如何约束输出。
