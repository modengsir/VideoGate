# Agent 安装与使用指南（V0.1）

VideoGate 使用可移植 `SKILL.md`，不要求付费 API。不同客户端的 Skill 发现机制可能随版本变化；如果当前版本不识别，使用 `prompts/universal-reviewer.md` + Gate 指令手动审核。

## 通用安装（Python 3.9+）

```bash
python3 scripts/install.py --agent codex --scope user
python3 scripts/install.py --agent claude-code --scope project --target .
python3 scripts/install.py --agent gemini-cli --scope project --target . --dry-run
python3 scripts/install.py --agent cursor --scope project --target .
python3 scripts/install.py --agent opencode --scope project --target .
python3 scripts/install.py --agent copilot --scope project --target .
python3 scripts/install.py --agent kiro --scope project --target .
```

选项：`--scope user|project`；`--target` 表示指定项目的绝对/相对路径；`--dry-run` 只预览；`--force` 覆盖前创建备份；`--uninstall` 只删除目标的 `video-gate` 技能文件夹。

| Agent | 项目级目标位置 | 用户级位置 | 启动示例 |
|---|---|---|---|
| Claude Code | `.claude/skills/video-gate/` | `~/.claude/skills/video-gate/` | “使用 video-gate，执行 Gate 1” 或 `/video-gate`（若客户端支持） |
| Codex | `.agents/skills/video-gate/` | `~/.agents/skills/video-gate/` | “使用 $video-gate 质检这份分镜” |
| Cursor | `.cursor/skills/video-gate/` | `~/.cursor/skills/video-gate/` | “使用 video-gate Skill 执行 Gate 2” |
| Gemini CLI | `.gemini/skills/video-gate/` | `~/.gemini/skills/video-gate/` | 在 Gemini CLI 中选择/激活 Skill，再请求 Gate 1 |
| OpenCode | `.opencode/skills/video-gate/` | `~/.config/opencode/skills/video-gate/` | “按 video-gate 规则审分镜” |
| GitHub Copilot | `.github/skills/video-gate/` | `~/.copilot/skills/video-gate/`（版本相关） | Agent mode 请求使用 video-gate |
| Kiro | `.kiro/skills/video-gate/`（实验性） | `~/.kiro/skills/video-gate/`（实验性） | 若版本可加载 Skill 则请求 Gate 1，否则用 Prompt |

> **兼容声明**：以上路径为第一版目标适配方案，并非声称已在所有平台版本上实机验证。Kiro 的原生 Skill 支持及个人级路径尤其需要按具体版本确认；安装器复制成功不等于 Agent 已成功载入。Kiro 可用自定义 Agent 指令或提示词作为稳定回退。

## Claude Code

安装：`python3 scripts/install.py --agent claude-code --scope user`。在项目里打开 Claude Code，输入“使用 video-gate 审核 storyboard.md 的 Gate 1”。当 Gate 1 完成后，要求写入 `templates/review-report.md` 格式的报告；修改后再审。第二关确保可以打开图片。

## Codex

安装：`python3 scripts/install.py --agent codex --scope project --target .`。在项目中用 `$video-gate` 加上分镜文本触发；如自动发现失败，明确让 Agent 读取 `.agents/skills/video-gate/SKILL.md`。

## Cursor

安装项目级 `.cursor/skills/video-gate/`；在 Cursor Agent 打开包含分镜的目录，要求读取 `video-gate` 并执行 Gate 1/2。请确认当前客户端支持项目 Skills，图片审核需提供图像文件或可视输入。

## Gemini CLI

安装 `.gemini/skills/video-gate/`，根据你使用的 CLI 版本使用 `/skills` 查看/激活技能，再提供审核材料。无原生 Skills 的版本，复制统一 Prompt。

## OpenCode

安装 `.opencode/skills/video-gate/`，要求 Agent 加载 `video-gate` 规则并审查项目文件。若使用用户级，目标为配置目录下的 `skills`。严格检查模型是否实际拥有视觉能力。

## GitHub Copilot

安装 `.github/skills/video-gate/`，在支持 Agent Skills 的编辑器/CLI 中激活或自然语言请求。用户级路径随具体产品形态可能不同；先采用项目级安装，若版本不兼容则直接引用通用 Prompt。

## Kiro

由于不同版本对 Skill 的支持存在差异，本仓库将 Kiro 原生目录适配标记为**实验性**；安装后需要自行确认是否发现 `SKILL.md`。可靠回退方式是把 `prompts/universal-reviewer.md` 放入所用 Kiro Agent 的自定义规则中，结合 `prompts/gate1.md`/`prompts/gate2.md` 使用。

## 升级、卸载与安全

```bash
python3 scripts/install.py --agent codex --scope user --force
python3 scripts/install.py --agent codex --scope user --uninstall
```

`--force` 会备份现有同名技能目录，而不会清理同级其他 Skills。安装器不调用网络，使用本地仓库源码；不要在不信任的仓库里执行脚本。
