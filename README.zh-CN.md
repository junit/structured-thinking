# Structured Thinking (结构化思维工具包)

<p align="center">
  <a href="README.md">English</a> | <b>简体中文</b>
</p>

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/your-username/structured-thinking/pulls)
[![LLM/AI Skill](https://img.shields.io/badge/AI%20Agent-Skill-orange.svg)](SKILL.md)

Structured Thinking（结构化思维）是一个专门为 **AI Agent、AI 编程助手以及软件开发者** 设计的系统化沟通框架。它能将零散的日志、混杂的排查步骤和时间流水账，转化为以读者为中心、结论先行、极具决策价值的专业交付件。

---

## 📖 目录
- [为什么需要结构化思维？](#-为什么需要结构化思维)
- [前后对比示例](#-前后对比示例)
- [项目目录结构](#-项目目录结构)
- [五步方法论框架](#-五步方法论框架)
  - [第一步：定义问题 (5W2H & 5-Why)](#第一步定义问题-5w2h--5-why)
  - [第二步：确定目标与受众 (A→B 规则 & SCQA)](#第二步确定目标与受众-ab-规则--scqa)
  - [第三步：金字塔搭建 (金字塔原理)](#第三步金字塔搭建-金字塔原理)
  - [第四步：横向分类归纳 (MECE & 排序)](#第四步横向分类归纳-mece--排序)
  - [第五步：关系可视化](#第五步关系可视化)
- [如何与 AI Agent/编程工具集成](#-如何与-ai-agent编程工具集成)
  - [接入 Claude Code / Gemini CLI](#接入-claude-code--gemini-cli)
  - [接入 Cursor / Windsurf / VS Code](#接入-cursor--windsurf--vs-code)
  - [接入 LangChain 或自定义智能体框架](#接入-langchain-或自定义智能体框架)
- [开源协议](#-开源协议)

---

## 💡 为什么需要结构化思维？

AI Agent 和技术人员在汇报时经常陷入“流水账式沟通”。当被问及“发生了什么故障”或“下一步方案”时，往往习惯性地把整个排查过程、原始日志或是代码细节和盘托出。

这迫使团队 Leader、产品经理或业务主管必须花大量精力去阅读长篇大论，才能提炼出核心结论、损失影响和修复计划。

**Structured Thinking** 建立了一套严密的表达机制，确保结论第一、信息分组逻辑清晰、内容完全服务于受众的“下一步行动（决策/执行）”。

---

## 🔄 前后对比示例

### 流水账叙述（Before）
> 我们在 13:55 部署了一个变更。14:00 时，结账服务开始报错失败。数据库连接池满了。DBA 在 14:15 重启了数据库，但没有效果。在 14:30 我们开始关联部署记录。在 14:45 我们发现了连接泄漏 bug。15:00 我们进行了回滚，15:30 服务恢复了正常。

### 结构化与读者导向（After）
> **摘要**: 结账服务已于 15:30 恢复运行。本次故障系 13:55 回滚部署中引入的连接泄漏 bug 导致（总停机时间: 2小时，影响资损: 20万美元）。目前服务已回滚，后续我们将通过引入 ESLint 规则来彻底杜绝连接泄漏。
>
> **关键时间线**:
> 1. **回滚部署** (13:55) — 引入 Bug（代码中遗漏了 `finally` 块）。
> 2. **DB 重启** (14:15) — 尝试临时修复；连接池瞬间重新占满。
> 3. **代码回滚** (15:00–15:30) — 代码成功回滚，服务完全恢复。

---

## 📂 项目目录结构

本项目文件构成可直接供 LLM 学习或日常查阅：

```
.
├── SKILL.md                 # 核心 Agent Skill 指令定义与规则
└── references/              # 分步进阶指南
    ├── agent-workflow.md    # 思考路径（Mental Draft）与输出排版模版
    ├── step-1-5w2h.md       # 利用 5W2H 和 5-Why 彻底定位根本原因
    ├── step-2-scqa.md       # 依据 A→B 规则与 SCQA 故事框架吸引读者
    ├── step-3-pyramid.md    # 金字塔原理（自上而下，结论先行）
    ├── step-4-mece.md       # MECE 原则（相互独立，完全穷尽）
    └── step-5-visualize.md  # 关系可视化与图表类型匹配指南
```

---

## 🛠️ 五步方法论框架

### 第一步：定义问题 (5W2H & 5-Why)
在开始沟通或编写报告前，客观分析现状：
- 运用 **5W2H**（*What, When, Where, Why, Who, How, How much*）梳理并记录全部事实。
- 使用 **5-Why** 追问 5 次为什么，直达流程或系统层面的核心诱因，避免停留在表面症状或流于人身指责。
- *参考 [references/step-1-5w2h.md](references/step-1-5w2h.md) 查看具体范例。*

### 第二步：确定目标与受众 (A→B 规则 & SCQA)
以终为始，让沟通具有明确的目的性：
- **A→B（角色→行为）**: 明确谁是读者，期望他们读完后做出什么行为。砍掉所有不服务于该目标的冗余信息。
- **SCQA（情境-冲突-问题-回答）**: 快速构建故事弧线，引入背景。可根据受众习惯调整顺序以达到不同强调效果：
  - **ASCQ** (回答先行)：适合时间宝贵、缺乏耐心的技术主管或高管。
  - **QSCA** (问题先行)：适合对现状安于现状，需要痛点刺激的利益相关者。
- *参考 [references/step-2-scqa.md](references/step-2-scqa.md) 获取详细排版技巧。*

### 第三步：金字塔搭建 (金字塔原理)
层级化组织你的论点：
- **结论先行**：在金字塔的最顶端，开门见山陈述核心结论/行动建议。
- **自上而下**：下层分支作为上层分支的具体支撑。
- **中心明确**：确保金字塔里的每一个结论节点都有其清晰、可总结的目的和价值。
- *参考 [references/step-3-pyramid.md](references/step-3-pyramid.md) 查看垂直金字塔图示。*

### 第四步：横向分类归纳 (MECE & 排序)
确保同级观点在逻辑上无懈可击：
- **MECE**（*相互独立，完全穷尽*）：分类不重叠，覆盖无盲区。
- **经典分类维度**：**时间轴**（Temporal）、**结构空间**（Structural）、**定性特征**（Qualitative）以及**定量级别**（Quantitative）。
- **统一排序**：一个分支组内的元素需使用同一种排序逻辑（如按重要程度降序，或按时间先后升序），严禁中途混用。
- *参考 [references/step-4-mece.md](references/step-4-mece.md) 练习如何进行 MECE 分类。*

### 第五步：关系可视化
当单纯的文本叙述显得晦涩或低效时，引入图表：
- 用**流程图**或**泳道图**表示过程和流水线。
- 用**二维矩阵/表格**展示选项对比和优劣分析。
- 用**拓扑图/依赖图**展现组件和架构之间的依赖关系。
- 推荐在 markdown 中直接使用简便的 **Mermaid** 格式代码段。
- *参考 [references/step-5-visualize.md](references/step-5-visualize.md) 学习如何快速进行图表类型匹配。*

---

## 🤖 如何与 AI Agent/编程工具集成

本仓库的指令设计专门针对大语言模型（LLM）和 AI 代理进行优化。

### 接入 Claude Code / Gemini CLI
将 `SKILL.md` 的全部内容复制到您 AI 助手的系统提示词（System Prompt）或自定义 skills 配置文件中。这样在后续生成任务说明、Bug 分析或项目架构演进时，助手将自动应用此结构化思维。

### 接入 Cursor / Windsurf / VS Code
您可以在您的项目根目录下，新建或追加规则到 `.cursorrules` / `.windsurfrules` 中：

```json
{
  "rules": [
    "在解释复杂的 Bug 修复方案、架构提案或技术路径时，请严格遵守 SKILL.md 中定义的结构化思维原则。始终确保结论先行，并在开头提供 1-2 句的核心摘要。"
  ]
}
```

### 接入 LangChain 或自定义智能体框架
将 `SKILL.md` 作为系统背景加载，赋予您的智能体系统级表达模型：

```python
with open("path/to/SKILL.md", "r", encoding="utf-8") as f:
    system_prompt = f.read()

# 在初始化 Agent Executor 时传入 system_prompt
```

---

## 📄 开源协议

本项目基于 MIT 开源协议发布 - 详情请参阅 [LICENSE](LICENSE) 文件。
