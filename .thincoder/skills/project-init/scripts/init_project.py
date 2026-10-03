#!/usr/bin/env python3
"""ThinCoder101-harness 子项目初始化脚本。

由 project-init 技能调用。Agent 只负责两件事：
  1. 把访谈共识写成需求文档草稿（任意临时位置）；
  2. 执行本脚本：python3 init_project.py <项目名> --requirements <草稿路径>
其余全部由本脚本确定性完成：建目录、生成三件套、复制部署规范、git init 第 0 号存档。
任何一步失败都会以非零码退出并打印中文错误说明，Agent 读输出向用户汇报即可。
"""
import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path

COMMIT_MSG = "第 0 号存档：需求与守则就位"
PARENT_MARKER = "主目录工作守则"  # 主目录 AGENTS.md 的标志串


def fail(msg: str) -> "None":
    print(f"[init-project 失败] {msg}")
    sys.exit(1)


def run_git(args: list, cwd: Path) -> str:
    r = subprocess.run(["git"] + args, cwd=cwd, capture_output=True, text=True, encoding="utf-8")
    if r.returncode != 0:
        fail(f"git {' '.join(args)} 执行失败：{r.stderr.strip() or r.stdout.strip()}\n"
             f"（若提示未设置 user.name/user.email，请先完成第 5 篇的 Git 报到配置）")
    return (r.stdout or "").strip()


def extract_section(parent_agents: Path, heading: str) -> str:
    """从主目录 AGENTS.md 中提取 `## <heading>` 小节（到下一个 `## ` 为止）。"""
    text = parent_agents.read_text(encoding="utf-8")
    pattern = re.compile(rf"(?ms)^## {re.escape(heading)}\s*\n(.*?)(?=^## |\Z)")
    m = pattern.search(text)
    return m.group(1).strip() if m else ""


CHILD_AGENTS_TEMPLATE = """# {name} · 子项目守则

## 本目录的身份
这里是产品「{name}」的开发工地。开发动作只发生在本目录内；开工前先读 docs/requirements.md，按需求文档行事，不扩大范围。

## 工作规矩
1. 每个开发批次开始前，先列出要动的文件；完成后展示 diff 并报告结果。
2. 完成一个阶段后，提醒用户做 Git 存档。
3. 删除/覆盖已有文件、安装依赖、联网部署、花钱操作，必须先请示。

{deploy_section}

{skills_section}
"""

SKILLS_SECTION = """## 官方部署技能资源

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

部署红线（守则级，不得违反）：
1. 部署命令必须带 -a overseas（海外节点、免备案），任何部署不得省略——官方 Skill 默认区域是 global（含大陆、触发备案），若 Skill 部署链不覆盖选区参数，必须改用 CLI 显式命令；
2. 部署动作执行前必须向用户确认；
3. 部署完成后把 Deploy URL 直接告诉用户。"""

README_TEMPLATE = """# {name}

> 一句话定位：（待补充——来自需求文档）

## 目录说明
- docs/requirements.md：需求文档（访谈共识，当前版本的唯一开工依据）
- AGENTS.md：本项目的 AI 守则

## 如何本地运行
（开发阶段补充）

## 当前状态
需求已归档，第 0 号存档已建立；等待进入工程模式开发。
"""


def main() -> None:
    ap = argparse.ArgumentParser(description="ThinCoder101-harness 子项目初始化")
    ap.add_argument("name", help="产品名（英文优先，中划线连接，如 number-guess-game）")
    ap.add_argument("--requirements", required=True,
                    help="需求文档草稿路径（Agent 先把访谈共识写成文件，再传给本脚本）")
    ap.add_argument("--parent", default=".", help="主目录路径（默认当前目录）")
    args = ap.parse_args()

    name = args.name.strip()
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]*", name):
        fail(f"项目名「{name}」不合法：只允许英文字母/数字/中划线/下划线，且以字母或数字开头。")

    parent = Path(args.parent).resolve()
    parent_agents = parent / "AGENTS.md"
    if not parent_agents.exists() or PARENT_MARKER not in parent_agents.read_text(encoding="utf-8"):
        fail(f"当前目录（{parent}）不是主工作目录：未找到含「{PARENT_MARKER}」的 AGENTS.md。"
             f"请回到主目录再执行本脚本——子项目必须建在主目录的 projects/ 下。")

    req_src = Path(args.requirements).resolve()
    if not req_src.is_file():
        fail(f"需求文档草稿不存在：{req_src}")

    proj = parent / "projects" / name
    if proj.exists():
        fail(f"projects/{name} 已存在。换个名字，或删除旧目录后重试。")

    # ---- 结构 ----
    (proj / "docs").mkdir(parents=True)
    shutil.copyfile(req_src, proj / "docs" / "requirements.md")
    (proj / "README.md").write_text(README_TEMPLATE.format(name=name), encoding="utf-8")

    deploy_section = extract_section(parent_agents, "部署规范")
    deploy_block = ("## 部署规范\n" + deploy_section + "\n") if deploy_section else \
                   "## 部署规范\n（主目录守则暂无此节，跳过复制。）\n"
    (proj / "AGENTS.md").write_text(
        CHILD_AGENTS_TEMPLATE.format(name=name, deploy_section=deploy_block, skills_section=SKILLS_SECTION),
        encoding="utf-8")

    # ---- Git 第 0 号存档（在子项目目录内）----
    run_git(["init"], cwd=proj)
    run_git(["add", "-A"], cwd=proj)
    run_git(["commit", "-m", COMMIT_MSG], cwd=proj)

    # ---- 自检：仓库根必须是子项目目录 ----
    toplevel = Path(run_git(["rev-parse", "--show-toplevel"], cwd=proj)).resolve()
    if toplevel != proj:
        fail(f"自检失败：仓库根是 {toplevel}，不是子项目目录 {proj}。请检查并删除误建的 .git。")

    commit = run_git(["log", "--oneline", "-1"], cwd=proj)
    print("[init-project 完成]")
    print(f"  项目目录：projects/{name}")
    print(f"  三件套：docs/requirements.md、README.md、AGENTS.md（含部署规范与官方技能资源）")
    print(f"  第 0 号存档：{commit}")
    print(f"  下一步：请用户退出当前 ThinCoder，打开 projects/{name} 文件夹，"
          f"在其中重新启动 thincoder，说「开始开发」进入工程模式。")


if __name__ == "__main__":
    main()
