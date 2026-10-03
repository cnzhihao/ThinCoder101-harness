# ThinCoder101-harness：《AI 编程应用开发专栏》实战篇 Harness 底座

这是专栏第 6 篇的随堂底座仓：**一个仓库装齐司令部的全部家当**——AI 员工守则、工作台说明书、三个技能（需求访谈 + 子项目初始化）。读者不需要手抄任何模板，一条提示词让 AI 把整套 Harness 装进自己的工作目录。

## 仓库结构

    ThinCoder101-harness/
    ├── AGENTS.md                       ← AI 员工守则（身份/目录规矩/开工自检/新需求访谈/部署规范/Git 规矩/请示红线）
    ├── README.md                       ← 工作台说明书（给人看：目录分工/工作动线/版本管理）
    ├── .gitignore                      ← 内容一行：projects/（子项目区不归主仓库管，防仓库套仓库）
    ├── VERSION                         ← 版本锚点：AI 靠它自动判断要不要升级
    └── .thincoder/
        └── skills/
            ├── grilling/SKILL.md       ← 访谈引擎：AI 一轮一轮把需求问透（经守则主动提议使用）
            ├── project-init/SKILL.md   ← 子项目初始化：建目录、生成三件套、复制部署规范、Git 第 0 号存档
            └── grill-me/SKILL.md       ← 备用快捷入口：用户点名时直接开拷

技能部分来自 Matt Pocock 的开源项目（github.com/mattpocock/skills，MIT 许可证），锁定在上游 commit d81f3a1（2026-10-03）——固定版本快照，教程与版本绑定；上游更新由专栏统一重新打包。守则内置「部署规范」（EdgeOne Pages 一键部署）与官方 EdgeOne Makers 技能清单，初始化子项目时自动复制进子项目守则。

## 安装：一条提示词（读者唯一要做的动作）

建好（或选中）自己的工作文件夹，在里面启动 ThinCoder，把下面这段话粘贴给 AI，权限弹窗点批准，十几秒装完：

    请把 https://github.com/cnzhihao/ThinCoder101-harness 这个仓库完整安装到当前目录，
    作为我的工作司令部：
    ① 把仓库里的 AGENTS.md、README.md、.gitignore 复制到当前目录（已存在的同名文件先征求我的意见）；
    ② 把 .thincoder/skills/ 下的技能合并进当前目录的 .thincoder/skills/；
    ③ 记住 VERSION 文件的内容作为当前版本记录；
    ④ 装完后执行 git init 和首次提交（提交信息：司令部建档）；
    ⑤ 运行 /skills 确认 grill-me、grilling、project-init 三个技能已就位，
    然后向我汇报安装结果和开工自检情况。

装完**重启 ThinCoder**（退出再输入 thincoder），新守则生效——之后的一切（环境自检、技能升级、需求访谈提议、子项目初始化）都由 AGENTS.md 的守则自动驱动，你只管聊天。

## 升级：全自动

升级逻辑写在守则的「开工自检」里：AI 每天首次启动对比本仓 VERSION 与本地记录，有新版就告知并经同意自动更新。你永远不需要手动升级。

## 日常使用

- **有新想法**：直接说出来，AI 会主动问你要不要开始需求访谈（grilling 引擎一轮一轮问透）；
- **需求聊透要开工**：AI 用 project-init 技能初始化子项目——在 projects/ 下建目录、生成需求文档/README/子守则三件套、把部署规范复制进子守则、完成 Git 第 0 号存档；
- **要上线**：说「部署上线」，Agent 按内置部署规范自己装 CLI、带 -a overseas、部署完把网址递给你；
- **想跳过访谈提议直接开拷**：点名 grill-me 即可。

## 子项目

以后孵化的每个产品（如 projects/my-first-tool/）建在主目录里面，各自独立 git init——和本仓库没有任何 Git 嵌套关系（主仓库的 .gitignore 已把 projects/ 挡住）。
