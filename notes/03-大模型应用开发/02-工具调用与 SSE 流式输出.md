# 工具调用与 SSE 流式输出

OpenAI API 文档也把工具调用称为函数调用（function calling）。SSE 是 Server-Sent Events，即服务器发送事件。

## AI 交互练习

- 用熟悉的前端框架接收 SSE，分别展示回答文本、工作流节点状态和错误。
- 练习处理流结束和前端取消请求。Demo 展示检索、字段提取、证据核对等应用执行步骤，并让用户打开对应来源。

## 官方资料

- [OpenAI 函数调用（官方中文）](https://developers.openai.com/zh-Hans/api/docs/guides/function-calling) · [英文原文](https://developers.openai.com/api/docs/guides/function-calling)。看应用如何定义工具、执行模型返回的调用请求，以及如何把结果回传给模型。
- [FastAPI 服务器发送事件 SSE（官方中文）](https://fastapi.tiangolo.com/zh/tutorial/server-sent-events/) · [英文原文](https://fastapi.tiangolo.com/tutorial/server-sent-events/)。先练后端分批发送几条事件，再把模型输出或工具状态接进事件流。
