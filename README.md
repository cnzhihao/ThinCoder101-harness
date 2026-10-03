# thincoder-skills：《AI 编程应用开发专栏》实战篇技能包

本仓库是专栏实战篇（第 6 篇）随堂技能包的**发布仓**，内含两个配合使用的 ThinCoder 技能：

- **grill-me**：需求拷问入口。你呼叫它，AI 就切换成"严苛产品总监"，从宏观到细节连环追问你的需求。
- **grilling**：真正的访谈方法（拷问引擎）。grill-me 调用它干活，两者必须同时在场——本包已一次装齐，你不用操心。

技能来自 Matt Pocock 的开源项目（github.com/mattpocock/skills，MIT 许可证）。本包是**固定版本快照**：取自上游 commit d81f3a1（2026-10-03），内容未做任何修改。快照保证你学到的操作和教程永远一致；上游更新时，由专栏统一重新打包并通知，你不需要自己跟进。

## 安装（第 6 篇教程同步，三步）

> 不用 git clone：直接下载 ZIP，包里没有 .git 文件夹，不会在你主目录里塞进多余的东西。

1. 打开本仓库主页 → 绿色 Code 按钮 → **Download ZIP**；
2. 解压，得到 thincoder-skills-main 文件夹；
3. 打开终端，进入你的主工作目录（第 6 篇建的，例如 my-workspace），把包里的 .thincoder 文件夹复制进来：

       cd my-workspace
       cp -R ~/Downloads/thincoder-skills-main/.thincoder .

   Windows 用户（PowerShell）：

       cd my-workspace
       Copy-Item -Recurse $env:USERPROFILE\Downloads\thincoder-skills-main\.thincoder .

完成。在 my-workspace 里启动 ThinCoder，输入 /skills，能看到 grill-me 和 grilling 两个技能就装好了。

## 主目录安装后长这样

    my-workspace/            ← 你的总司令部（第 6 篇建立）
      AGENTS.md              ← 第 6 篇会教你写
      README.md              ← 同上
      .thincoder/            ← 本包复制进来的部分
        skills/
          grill-me/SKILL.md  ← 需求拷问入口
          grilling/SKILL.md  ← 拷问引擎

以后第 7 篇 grill-me 需求访谈、以及你孵化的每个子项目，都在这个主目录里进行。子项目（如 my-first-tool/）建在主目录里面，它们会有自己的 Git 仓库——和本技能包没有任何 Git 关系，互不干扰。

## 升级

本包升级由专栏统一发布：出新版时重复上面的三步（覆盖复制 .thincoder 即可）。不要自行从上游仓库同步——教程与快照版本绑定。
