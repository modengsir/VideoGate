# 生成工具和审核模型分工

| 环节 | 可选择工具 | VideoGate 职责 |
|---|---|---|
| 写剧本 | ChatGPT、Claude Code、Codex、其他 LLM | 提交文字给 Gate 1 |
| 生图 | ChatGPT Image、Nano Banana、其他工具 | 提交图片给 Gate 2 |
| 审剧本 | Ling-3.2-flash、自己的文本/多模态 Agent | 依据 G1 规则审查 |
| 审图片 | Ling 或其他**有实际图像访问能力**的 Agent | 依据 G2 规则审查 |
| 生成视频 | MiniMax H3、Google Flow 平台、Omni、Veo、Seedance 等 | **仅输出预审后的移交清单** |

Google Flow 是视频创作平台，不应把平台名称误写成基础模型；实际视频模式、时长、分辨率、参考图数量和可用模型随服务与账户而变化。VideoGate V0.1 不自动调用任何平台，也不保证它们拥有相同功能。相关官方说明需以用户使用时的平台最新文档为准。
