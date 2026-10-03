---
name: project-init
description: 初始化一个新的产品子项目：建目录、放三件套（README/AGENTS.md/docs）、git init 第 0 号存档。当用户同意孵化一个新需求，或要求创建/初始化子项目时使用。
---

# 子项目初始化流程

访谈达成共识、用户确认需求文档无误后，主动向用户提议：「需求已经聊透了，要不要我现在初始化项目文件夹？」用户同意（或明确要求创建/初始化子项目）后，按以下流程全自动执行——用户不需要指挥任何步骤：

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

## 3. Git 第 0 号存档（必须先进入子项目目录）
先切换到子项目目录（cd projects/<产品名>），再用 pwd 确认当前路径确实在子项目里，然后才执行：
1. git init（在子项目目录内建立独立仓库）；
2. git add -A 并提交，提交信息：「第 0 号存档：需求与守则就位」。

边界（不可违反）：
- git init 只允许发生在子项目目录内——执行前后都用 git rev-parse --show-toplevel 自检，确认仓库根就是子项目目录；
- 严禁在主目录执行本项目的任何 git 操作：主目录已有自己的仓库（司令部仓库），projects/ 又被它的 .gitignore 忽略——在主目录 git add 只会把本项目完全漏掉，产生"看起来提交了其实什么都没有"的假存档；
- 初始化完成后回到主目录汇报时，不要带任何 git add/commit 动作。

## 4. 汇报
初始化完成后向用户汇报：目录路径、三件套清单、第 0 号存档的 commit 结果。然后引导交接：<br>「初始化完成。请退出当前 ThinCoder（Ctrl+C 或 /exit），打开 <子项目路径> 文件夹，在里面重新启动 thincoder——新会话会读取子项目的守则和需求文档，到时说一声"开始开发"就进入工程模式。」

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
