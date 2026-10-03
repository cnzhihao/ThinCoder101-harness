# grill-me 技能包（ThinCoder 专栏实战篇专用）

本仓库是《AI 编程应用开发专栏》实战篇（第 6 篇）使用的技能包，内含两个配合使用的 Agent 技能：

- **grill-me**：需求拷问入口。你呼叫它，AI 就切换成"严苛产品总监"，连环追问你的需求。
- **grilling**：真正的访谈方法（拷问引擎）。grill-me 调用它干活，两者必须同时在场。

两个技能来自 Matt Pocock 的开源项目（github.com/mattpocock/skills，MIT 许可证），本仓库只做打包分发，未修改技能内容。

## 安装（一步到位）

在第 6 篇中你已经建好了自己的主工作目录（例如 my-workspace）。打开终端，进入这个目录：

    cd my-workspace

然后把本仓库下载进去（目录名叫 thincoder-skills）：

    git clone https://github.com/cnzhihao/thincoder-skills.git

最后，把仓库里的 .thincoder 文件夹复制到主工作目录（macOS 与 Windows 命令相同）：

    cp -R thincoder-skills/.thincoder .

完成。打开 ThinCoder（在 my-workspace 里输入 thincoder 回车），输入 /skills，你应该能看到 grill-me 和 grilling 两个技能。

> Windows 用户如果 cp -R 报错，可以直接用文件管理器：打开 thincoder-skills 文件夹，把里面的 .thincoder 文件夹复制、粘贴到 my-workspace 文件夹（注意：.thincoder 是以点开头的隐藏文件夹，Windows 资源管理器能看到它，直接复制即可）。

## 仓库结构

    thincoder-skills/
      README.md              ← 本文件
      .thincoder/            ← 复制这一个文件夹就够了
        skills/
          grill-me/SKILL.md  ← 需求拷问入口
          grilling/SKILL.md  ← 拷问引擎（grill-me 调用它）

## 更新

以后技能有更新，进入 thincoder-skills 目录执行 git pull，然后把 .thincoder 重新复制一次即可。
