---
name: project-init
description: 初始化一个新的产品子项目：建目录、放三件套（README/AGENTS.md/docs）、git init 第 0 号存档。当用户同意孵化一个新需求，或要求创建/初始化子项目时使用。
---

# 子项目初始化流程

当用户同意孵化一个新需求（访谈达成共识），或明确要求创建/初始化一个子项目时，按以下流程执行：

## 1. 建目录
在主目录的 projects/ 下，用产品名新建文件夹（英文名优先，用中划线连接，如 projects/number-guess-game/）。名字与用户确认一次。

## 2. 生成三件套
在子项目里创建：

- **docs/requirements.md**：需求文档。内容来自访谈共识（已拍板决策、功能点清单、明确不做、验收标准）。若还没有访谈共识，先提示用户回到需求访谈，不要编造需求。
- **README.md**：子项目说明书。包含一句话定位、目录说明（docs/ 放需求文档）、如何本地运行（由后续开发补充）、当前状态（需求已归档，待开发）。
- **AGENTS.md**：子项目守则。包含：
  - 本目录是一个具体产品的开发工地，开发动作只发生在本目录内；
  - 开工前先读 docs/requirements.md，按需求文档行事，不扩大范围；
  - 每个开发批次前先列出要动的文件，完成后展示 diff 并报告结果；
  - 完成一个阶段后提醒用户做 Git 存档；
  - 删除/覆盖已有文件、安装依赖、联网部署、花钱操作，必须先请示。
  
  再把主目录 AGENTS.md 中的「部署规范」一节原样复制进来（如主目录没有该节则跳过并告知用户），并附加下方的「官方部署技能资源」一节。

## 3. Git 第 0 号存档
在子项目目录内执行 git init，将三件套全部提交，提交信息：「第 0 号存档：需求与守则就位」。注意：子项目仓库与主目录仓库相互独立，不要在主目录执行任何此项目的提交。

## 4. 汇报
初始化完成后向用户汇报：目录路径、三件套清单、第 0 号存档的 commit 结果，并提示下一步（进入子项目文件夹启动 ThinCoder，说「开始开发」进入工程模式）。

## 附加节：官方部署技能资源（复制进子项目 AGENTS.md）

部署相关的官方 Skill 清单（来源：EdgeOne Makers 官方技能包 edgeone-makers-tools，2026-10-03 核验）。部署场景优先使用这些官方技能，按需安装：

| Skill | 用途 |
| --- | --- |
| makers-deploy | 部署项目到 EdgeOne（部署主路径） |
| makers-cli | EdgeOne CLI 命令参考 |
| makers-recipes | 项目脚手架 |
| makers-agents | Agent 类项目开发 |
| makers-edge-functions | Edge Functions 开发 |
| makers-cloud-functions | Cloud Functions 开发 |
| makers-storage | KV / Blob 存储 |
| makers-middleware | 中间件 |
| makers-migration | 存量项目改造 |

安装方式：让 AI 执行「从 https://github.com/TencentEdgeOne/edgeone-makers-tools 安装 <技能名> 技能到当前项目」。

使用红线（守则级，不得违反）：
1. 部署命令必须带 -a overseas（海外节点、免备案），任何部署不得省略——官方 Skill 默认区域是 global（含大陆、触发备案），若 Skill 部署链不覆盖选区参数，必须改用 CLI 显式命令；
2. 部署动作执行前必须向用户确认；
3. 部署完成后把 Deploy URL 直接告诉用户。

## 边界
- 不写任何产品代码——初始化只交付文档和 Git 基线，开发留给工程模式。
- 不代替用户做需求决策——需求文档内容必须来自已确认的访谈共识。
