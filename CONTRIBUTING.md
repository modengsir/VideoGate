# Contributing

欢迎提交：具有可复现证据的 Gate 1/2 错误案例、对不同 Agent 的真实安装记录、文档翻译、标准化报告测试用例。

请不要把个人面部素材、商单保密图片、API 密钥、私密链接或未经授权的第三方数据提交到 Issues/PR。问题案例用匿名化文本或经授权素材。修改规则时同步更新对应 Prompt、Schema 和测试。

## 本地检查

```bash
python3 -m unittest discover -s tests -v
python3 scripts/install.py --agent codex --scope project --target /tmp/test-videogate --dry-run
```

测试仅证明安装脚本、文件格式与本地约束；不能替代真实 LLM/多模态模型视觉能力或 Agent 客户端版本的端到端验收。项目遵循 [MIT License](LICENSE)。
