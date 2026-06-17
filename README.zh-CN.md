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
- [适用行业与场景](#-适用行业与场景)
- [前后对比示例](#-前后对比示例)
- [项目目录结构](#-项目目录结构)
- [五步方法论框架](#-五步方法论框架)
  - [第一步：定义问题 (Cynefin 复杂度、5-Why、鱼骨图、系统动力学)](#第一步定义问题-cynefin-复杂度5-why鱼骨图系统动力学)
  - [第二步：确定目标与受众 (A→B 规则、SCQA、福格模型)](#第二步确定目标与受众-ab-规则scqa福格模型)
  - [第三步：决策架构 (第一性原理、奥卡姆剃刀、KT 决策矩阵、Pre-Mortem)](#第三步决策架构-第一性原理奥卡姆剃刀kt-决策矩阵pre-mortem)
  - [第四步：MECE 分类归纳 (MECE、MoSCoW、帕累托法则、三的法则、艾森豪威尔)](#第四步mece-分类归纳-mecemoscow帕累托法则三的法则艾森豪威尔)
  - [第五步：关系可视化与选项比选 (关系图表匹配、KT 决策矩阵)](#第五步关系可视化与选项比选-关系图表匹配kt-决策矩阵)
- [如何与 AI Agent/编程工具集成](#-如何与-ai-agent编程工具集成)
- [开源协议](#-开源协议)

---

## 💡 为什么需要结构化思维？

AI Agent 和技术人员在汇报时经常陷入“流水账式沟通”。当被问及“发生了什么故障”或“下一步方案”时，往往习惯性地把整个排查过程、原始日志或是代码细节和盘托出。

这迫使团队 Leader、产品经理或业务主管必须花大量精力去阅读长篇大论，才能提炼出核心结论、损失影响和修复计划。

**Structured Thinking** 建立了一套严密的表达机制，确保结论第一、信息分组逻辑清晰、内容完全服务于受众的“下一步行动（决策/执行）”。

---

## 🎯 适用行业与场景

虽然本工具包最初主要服务于 **软件研发与 IT 技术行业**，但其底层原则适用于任何**高知识密度、强跨团队协作和高决策成本**的专业领域。

### 1. 适用行业
- **软件研发与系统运维**（核心）：AI 编程助手（如 Claude Code、Cursor 等）、软件工程师、架构师、SRE/运维工程师及 DBA。
- **高科技与硬件研发**：需要处理复杂软硬件系统调试与多方案对比的研发团队。
- **互联网与数字化企业**：产品经理 (PM)、数据分析师、敏捷教练 (Scrum Master) 撰写需求文档 (PRD) 或阶段性报告。
- **专业咨询与技术顾问**：需频繁向客户或高管交付“系统评估”、“云迁移方案”等重决策报告的咨询团队。

### 2. 典型应用场景
- **线上故障复盘与归因**：在线上发生事故后，使用 [references/step-1-problem-diagnosis.md](references/step-1-problem-diagnosis.md) 的 **5-Why**、**鱼骨图**与**系统动力学**对诱因进行 MECE 分类与环路分析，产出高质量的 Postmortem。
- **技术选型与架构决策**：在面临多方案选型争议时，使用 [references/step-3-vertical-structure.md](references/step-3-vertical-structure.md) 的**第一性原理**从物理限制出发论证，并用 **KT 决策矩阵**进行量化比选。
- **需求优先级划分与排期**：在版本迭代或紧急重构时，使用 [references/step-4-horizontal-structure.md](references/step-4-horizontal-structure.md) 的 **MoSCoW 方法**与**艾森豪威尔矩阵**对任务进行象限化归类，杜绝范围蔓延。
- **本地调试与排错纪律**：在遇到本地编译或测试报错时，调用 [references/agent-workflow.md](references/agent-workflow.md) 启动 **OODA 循环**与 **Save Point（单变量回滚）纪律**，杜绝无秩序的堆积修改。

### 3. 解决的核心问题
- **消灭流水账式汇报**：将“排查流水账”提炼为“结论先行 + 3个分类桶 + 明确行动”，使管理层决策效率提升数倍。
- **杜绝盲目猜测与非理性决策**：复杂问题强制前置“探针”收集数据，方案选择强制使用物理极限与量化矩阵，用理性数据取代“直觉和跟风”。
- **防范发布逻辑漏洞与范围蔓延**：通过 **Pre-Mortem（事前剖析）** 前置假设系统彻底失败以挖掘安全防御任务，确保系统交付稳健。

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
    ├── agent-workflow.md    # 思考模型与响应模板 (含 OODA 调试循环与 Save Point 规则)
    ├── step-1-problem-diagnosis.md     # 定义问题 (Cynefin 复杂度、5-Why、鱼骨图、系统动力学)
    ├── step-2-goal-audience.md         # 确定目标与受众 (A→B、SCQA、福格模型 B=MAP)
    ├── step-3-vertical-structure.md    # 决策架构 (第一性原理、奥卡姆剃刀、Pre-Mortem、KT 决策矩阵)
    ├── step-4-horizontal-structure.md  # MECE 分类归纳 (MECE、MoSCoW、帕累托法则、三的法则、艾森豪威尔)
    └── step-5-visualize.md  # 关系可视化与选项比选 (关系图表匹配、KT 决策矩阵)
```

---

## 🛠️ 五步方法论框架

### 第一步：定义问题 (Cynefin 复杂度、5-Why、鱼骨图、系统动力学)
在开始沟通或编写报告前，客观分析现状：
- **Cynefin 复杂度域**：划分问题属性（简单、繁杂、复杂、混乱）。针对 *Complex* 复杂域（如偶发竞态），**必须先设计探测（Probe）**（日志或实验），严禁盲目猜测。
- **5-Why 追问**：追问 5 次为什么，直达流程或系统层面的核心诱因，避免推诿和表面化。
- **鱼骨图分类**：将导致故障的多种假设原因进行 MECE 分类（如：基础设施、应用代码、客户端行为、开发流程）。
- **系统动力学**：分析系统中的存量（Stocks）与流量（Flows），画出**非线性反馈回路**，利用熔断、限流或退避机制打破“重试风暴”等恶性循环。
- *参考 [references/step-1-problem-diagnosis.md](references/step-1-problem-diagnosis.md) 查看具体范例。*

### 第二步：确定目标与受众 (A→B 规则、SCQA、福格模型)
以终为始，让沟通具有明确的目的性：
- **A→B 规则**: 明确谁是读者，期望他们读完后做出什么行为，裁剪无用噪音。
- **SCQA 架构**: 快速构建故事背景（Scenario, Complication, Question, Answer），根据受众调整排版顺序（如对高管使用 *ASCQ* 结论先行）。
- **福格行为模型 (B=MAP)**: 融合动力（M）、简化操作（A）和精准触发（P）来设计集成步骤，确保开发人员能执行成功。
- *参考 [references/step-2-goal-audience.md](references/step-2-goal-audience.md) 获取详细排版技巧。*

### 第三步：决策架构 (第一性原理、奥卡姆剃刀、KT 决策矩阵、Pre-Mortem)
层级化组织你的论点：
- **第一性原理**：从计算机底层的物理限制（CPU、网络 RTT, 内存）出发进行架构设计与方案论证，代替简单的类比方案。
- **奥卡姆剃刀**：在满足需求的方案中强制选择“最简单、移动实体最少”的方案，防止过度设计。
- **KT 决策矩阵**：建立包含 MUSTs 门槛判断、WANTs 加权打分以及 Risk 乘积评估的比选模型，将技术选型争议转化为可量化的理性共识。
- **Pre-Mortem（事前剖析）**：预先假设项目在生产中彻底失败，反向推导死因，在开发计划中前置安全防御任务。
- *参考 [references/step-3-vertical-structure.md](references/step-3-vertical-structure.md) 查看垂直金字塔与决策模板。*

### 第四步：MECE 分类归纳 (MECE、MoSCoW、帕累托法则、三的法则、艾森豪威尔)
确保同级观点在逻辑上无懈可击：
- **MECE 归类**：同层级分类相互独立、完全穷尽（不重叠、无遗漏）。
- **帕累托 80/20 法则**：分类中只聚焦前 20% 的核心矛盾，长尾因素折叠。
- **三的法则 (Rule of 3)**：列表项强制限制在 3 个（±1）左右，强迫模型脑力脱水，防止用户认知疲劳。
- **艾森豪威尔矩阵**：利用重要-紧急四象限拆解任务，专注象限 1（核心交付），剔除象限 4。
- **MoSCoW 优先级**：划分需求边界（Must 必须、Should 应该、Could 可以、Won't 不做）。
- *参考 [references/step-4-horizontal-structure.md](references/step-4-horizontal-structure.md) 练习如何进行 MECE 分类。*

### 第五步：关系可视化与选项比选 (关系图表匹配、KT 决策矩阵)
当单纯的文本叙述显得晦涩或低效时，引入图表与决策矩阵：
- **关系图表匹配**：在 markdown 中用 **Mermaid** 将逻辑关系翻译为合适的图表（流 $\rightarrow$ *流程图/泳道*，依赖 $\rightarrow$ *拓扑图*，循环 $\rightarrow$ *周期图*）。
- **Kepner-Tregoe (KT) 决策矩阵**：建立加权比选模型，评估备选方案。
- *参考 [references/step-5-visualize.md](references/step-5-visualize.md) 学习图表与矩阵模板。*

---

## 🤖 如何与 AI Agent/编程工具集成

本仓库的指令设计专门针对大语言模型（LLM）和 AI 代理进行优化。

### 接入 Claude Code / Gemini CLI
将 `SKILL.md` 的全部内容复制到您 AI 助手的系统提示词（System Prompt）或自定义 skills 配置文件中。这样在后续生成任务说明、Bug 分析或项目架构演进时，助手将自动应用此结构化思维，并在终端调试时使用 **OODA 循环**（观察、定位、决策、行动）防错。

### 接入 Cursor / Windsurf / VS Code
在项目根目录创建或追加到 `.cursorrules` (Cursor)、`.windsurfrules` (Windsurf) 或 `.github/copilot-instructions.md` (GitHub Copilot) 文件。这些是纯文本/Markdown 格式的指令文件，而非 JSON：

```text
Follow the structured-thinking principles from SKILL.md when writing bug reports,
postmortems, refactoring proposals, design docs, or any response where the user
needs to make a decision. Specifically:
- Open with a 1-2 sentence conclusion (decision/impact/recommendation).
- Group evidence into 3 (+/-1) buckets with conclusion-style headers.
- End with an explicit ask (Decisions Requested / Next Action / Open Questions).
- For active debugging, use the OODA loop with one hypothesis per cycle.
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
