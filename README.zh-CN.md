# Structured Thinking (结构化思维工具包)

<p align="center">
  <a href="README.md">English</a> | <b>简体中文</b>
</p>

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/junit/structured-thinking/pulls)
[![LLM/AI Skill](https://img.shields.io/badge/AI%20Agent-Skill-orange.svg)](SKILL.md)

Structured Thinking（结构化思维）是一个专门为 **AI Agent、AI 编程助手以及软件开发者** 设计的系统化沟通框架。它能将零散的日志、混杂的排查步骤和时间流水账，转化为以读者为中心、结论先行、极具决策价值的专业交付件。

---

## 📖 目录
- [为什么需要结构化思维？](#-为什么需要结构化思维)
- [前后对比示例](#-前后对比示例)
- [项目目录结构](#-项目目录结构)
- [五步方法论框架](#-五步方法论框架)
  - [第一步：定义问题 (5W2H、5-Why、Cynefin 复杂度、系统动力学)](#第一步定义问题-5w2h-5-why-cynefin-复杂度系统动力学)
  - [第二步：确定目标与受众 (A→B 规则、SCQA、STAR 框架、SMART 原则、Pre-Mortem、黄金圈、费曼技巧、福格模型)](#第二步确定目标与受众-ab-规则scqa-star-框架smart-原则pre-mortem黄金圈费曼技巧福格模型)
  - [第三步：金字塔搭建 (金字塔原理、第一性原理、奥卡姆剃刀、归纳逻辑)](#第三步金字塔搭建-金字塔原理第一性原理奥卡姆剃刀归纳逻辑)
  - [第四步：横向分类归纳 (MECE、MoSCoW/Kano、DDD/康威定律/通用语言、帕累托法则、三的法则、艾森豪威尔)](#第四步横向分类归纳-mecemoscowkanoddd康威定律通用语言帕累托法则三的法则艾森豪威尔)
  - [第五步：关系可视化与选项比选 (关系图表匹配、KT 决策矩阵)](#第五步关系可视化与选项比选-关系图表匹配kt-决策矩阵)
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
    ├── agent-workflow.md    # 思考路径（Mental Draft）与输出排版模版 (含 OODA 调试循环)
    ├── step-1-problem-diagnosis.md     # 定义问题 (5W2H, 5-Why, Cynefin, 系统动力学)
    ├── step-2-goal-audience.md         # 确定目标 (A→B, SCQA, STAR, SMART, Pre-Mortem, 黄金圈, 费曼, 福格)
    ├── step-3-vertical-structure.md    # 搭建金字塔 (金字塔原理, 第一性原理, 奥卡姆剃刀, 归纳逻辑)
    ├── step-4-horizontal-structure.md  # 横向分类 (MECE, MoSCoW/Kano, DDD/康威/通用语言, 80/20, Rule of 3, 艾森豪威尔)
    └── step-5-visualize.md  # 关系可视化与选项比选 (Mermaid 图表, KT 决策矩阵)
```

---

## 🛠️ 五步方法论框架

### 第一步：定义问题 (5W2H、5-Why、Cynefin 复杂度、系统动力学)
在开始沟通或编写报告前，客观分析现状：
- **5W2H 分析**：梳理并记录全部事实（What, When, Where, Why, Who, How, How much）。
- **5-Why 追问**：追问 5 次为什么，直达流程或系统层面的核心诱因，避免推诿和表面化。
- **Cynefin 复杂度域**：划分问题属性（简单、繁杂、复杂、混乱）。针对 *Complex* 复杂域（如偶发竞态），**必须先设计探测（Probe）**（日志或实验），严禁盲目猜测。
- **系统动力学**：分析系统中的存量（Stocks）与流量（Flows），画出**非线性反馈回路**，利用熔断、限流或退避机制打破“重试风暴”等恶性循环。
- *参考 [references/step-1-problem-diagnosis.md](references/step-1-problem-diagnosis.md) 查看具体范例。*

### 第二步：确定目标与受众 (A→B 规则、SCQA、STAR 框架、SMART 原则、Pre-Mortem、黄金圈、费曼技巧、福格模型)
以终为始，让沟通具有明确的目的性：
- **A→B 规则**: 明确谁是读者，期望他们读完后做出什么行为，裁剪无用噪音。
- **SCQA 架构**: 快速构建故事背景（Scenario, Complication, Question, Answer），根据受众调整排版顺序（如对高管使用 *ASCQ* 结论先行）。
- **STAR 框架**: 将事件执行过程结构化包装（情境 S、任务 T、行动 A、结果 R）。
- **SMART 原则**: 确保目标具体（S）、可衡量（M）、可达到（A）、相关性（R）、有时限（T）。
- **Pre-Mortem（事前剖析）**: 预先假设项目在生产中彻底失败，反向推导死因，在开发计划中前置安全防御任务。
- **黄金圈法则**: 按照 **Why $\rightarrow$ How $\rightarrow$ What** 的顺序解释改动。
- **费曼技巧**: 用十岁小孩能听懂的大白话和生活化类比翻译技术名词，杜绝过度黑话。
- **福格行为模型 (B=MAP)**: 融合动力（M）、简化操作（A）和精准触发（P）来设计集成步骤，确保开发人员能执行成功。
- *参考 [references/step-2-goal-audience.md](references/step-2-goal-audience.md) 获取详细排版技巧。*

### 第三步：金字塔搭建 (金字塔原理、第一性原理、奥卡姆剃刀、归纳逻辑)
层级化组织你的论点：
- **金字塔原理**：结论第一，下层作为上层的支撑，底层为客观数据事实。
- **第一性原理**：从计算机底层的物理限制（CPU、网络 RTT、内存）出发进行架构设计与方案论证，代替简单的类比方案。
- **奥卡姆剃刀**：在满足需求的方案中强制选择“最简单、移动实体最少”的方案，防止过度设计。
- **归纳逻辑优于演绎逻辑**：强制结论在前，后接并列事实。避免冗长的演绎推导链。
- *参考 [references/step-3-vertical-structure.md](references/step-3-vertical-structure.md) 查看垂直金字塔图示。*

### 第四步：横向分类归纳 (MECE、MoSCoW/Kano、DDD/康威定律/通用语言、帕累托法则、三的法则、艾森豪威尔)
确保同级观点在逻辑上无懈可击：
- **MECE 归类**：同层级分类相互独立、完全穷尽（不重叠、无遗漏）。
- **MoSCoW 与卡诺模型 (Kano)**：划分需求边界（Must/Basic 基础型、Should/Performance 期望型、Could/Excitement 兴奋型、Won't/Indifferent 无差异型）。
- **DDD 限界上下文 & 通用语言**：按业务边界进行 MECE 系统解耦，且在代码和文档里保持术语完全一致，确保语义 MECE。
- **康威定律约束**：架构设计（如微服务拆分）必须与团队的组织沟通带宽对齐。
- **帕累托 80/20 法则**：分类中只聚焦前 20% 的核心矛盾，长尾因素折叠。
- **三的法则 (Rule of 3)**：列表项强制限制在 3 个（±1）左右，强迫模型脑力脱水，防止用户认知疲劳。
- **艾森豪威尔矩阵**：利用重要-紧急四象限拆解任务，专注象限 1（核心交付），剔除象限 4。
- *参考 [references/step-4-horizontal-structure.md](references/step-4-horizontal-structure.md) 练习如何进行 MECE 分类。*

### 第五步：关系可视化与选项比选 (关系图表匹配、KT 决策矩阵)
当单纯的文本叙述显得晦涩或低效时，引入图表与决策矩阵：
- **关系图表匹配**：在 markdown 中用 **Mermaid** 将逻辑关系翻译为合适的图表（流 $\rightarrow$ *流程图/泳道*，依赖 $\rightarrow$ *拓扑图*，循环 $\rightarrow$ *周期图*）。
- **Kepner-Tregoe (KT) 决策矩阵**：建立包含 MUSTs 门槛判断、WANTs 加权打分以及 Risk 乘积评估的比选模型，将技术选型争议转化为可量化的理性共识。
- *参考 [references/step-5-visualize.md](references/step-5-visualize.md) 学习图表与矩阵模板。*

---

## 🤖 如何与 AI Agent/编程工具集成

本仓库的指令设计专门针对大语言模型（LLM）和 AI 代理进行优化。

### 接入 Claude Code / Gemini CLI
将 `SKILL.md` 的全部内容复制到您 AI 助手的系统提示词（System Prompt）或自定义 skills 配置文件中。这样在后续生成任务说明、Bug 分析或项目架构演进时，助手将自动应用此结构化思维，并在终端调试时使用 **OODA 循环**（观察、定位、决策、行动）防错。

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
