# Hermes Agent

Hermes Agent 是 Nous Research 开发的开源智能体项目。官方将它描述为开源智能体平台和 agent harness，提供持久记忆、技能系统和工具调用。

## 相关概念

Agent harness 指围绕模型调用循环的运行机制。以 LangChain 文档为例，它包括提示词、工具和中间件。阅读 Hermes Agent 时，可以观察这些机制在实际项目中如何实现。

- 阅读 Hermes Agent 文档时，重点看持久记忆（persistent memory）、技能（skills）和工具（tools）。
- 学习 agent harness 时，可结合上下文管理、工具权限、超时与重试、执行追踪和回归评估。

## 官方资料

- [Hermes Agent 官方文档](https://hermes-agent.nousresearch.com/docs)
- [Hermes Agent 官方项目介绍](https://hermes-agent.nousresearch.com/ai-agent-platform)
- [Hermes Agent 源码](https://github.com/NousResearch/hermes-agent)
- [LangChain Agents](https://docs.langchain.com/oss/python/langchain/agents)
- [LangChain Deep Agents](https://docs.langchain.com/oss/python/deepagents/overview)
- [Anthropic 的长任务 Harness 实践](https://www.anthropic.com/research/effective-harnesses-for-long-running-agents)

## 中文参考

- [LangChain 智能体（中文镜像）](https://docs.langchain.org.cn/oss/python/langchain/agents)。读「配置 Harness」一节。
- [Deep Agents 概述（中文镜像）](https://docs.langchain.org.cn/oss/python/deepagents/overview)。按需查上下文管理、工具权限和人工干预。
