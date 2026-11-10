# 标准使用流程（两关）

## 0. 准备

填写 `templates/project-brief.md`、分镜表与项目画幅/时长，按角色和镜头命名文件。分别保存 v1、v2 等版本，避免丢失原始测试记录。

## 1. 剧本创作

使用 ChatGPT 或 Claude Code / Codex 等工具组织分镜、台词、Prompt。Claude Code 用户可把分镜存成 `storyboard.md`，并在本地项目中保留 Git 版本；其他聊天模型用户复制文本即可。

## 2. Gate 1 审核

复制 `prompts/universal-reviewer.md` 与 `prompts/gate1.md`，贴入分镜/故事。若使用支持 Skill 的 Agent，要求“使用 video-gate 进行 Gate 1，不改写内容”。检查八项、记录证据，优先修复 P0，再复审。P0 解除后由创作者明确决定是否生图。

## 3. 生图与编号

选 Image、Nano Banana 或任意有权限使用的生图工具。先固定 1–2 张人物身份图，再做场景、分屏和关键帧。图片编号应与最终 Prompt 对应，注意实际平台的 `@Image` 编号可能不同。

## 4. Gate 2 审核

提交身份锚点、关键帧及关联分镜。审核模型必须能实际查看图像；只有文本输入时所有视觉项标记 UNVERIFIED。上传入口只能传一张图，可按 `prompts/single-image.md` 的拼版方案执行；尺寸/清晰度不足时补原图，不猜测。

## 5. 最小修改与复审

针对一个失败项局部修文字或图片，标注变更范围，复审相关项目与依赖。检查报告和修改前/后证据都保存。P0 仍存在时不建议进入生成。

## 6. 移交视频平台与人工验收

根据对应平台的能力和约束，把合格的 Prompt、身份图和关键帧交给 MiniMax、Flow、Omni、Veo、Seedance 等平台。**VideoGate 不执行视频生成、不审核生成后视频。** 创作者自己负责看片、听音、确认授权并发布。

## 日志规范

费用与次数只有平台实际记录才填入 `templates/cost-log.csv`。不得将质检发现问题数直接换算为节省的生成次数。
