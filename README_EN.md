# VideoGate — Two pre-generation quality gates for AI video

**Review before you render.** A model-agnostic, open-source Agent Skill by ModengSir.

**Gate 1** checks scripts, dialogue, storyboard timelines, actions, scene logic and prompt consistency. **Gate 2** checks identity anchors, image references, framing, props, hands and lighting. VideoGate **does not generate video or review finished video**.

## Quick start

```bash
git clone https://github.com/modengsir/VideoGate.git
cd VideoGate
python3 scripts/install.py --agent codex --scope user
```

Supported installation targets: `claude-code`, `codex`, `cursor`, `gemini-cli`, `opencode`, `copilot`, `kiro` (actual support varies with product version). Read [agent-specific installation steps](docs/agents.md) first. Without installation, paste the [universal prompt](prompts/universal-reviewer.md) into a custom assistant, then supply the [Gate 1](prompts/gate1.md) or [Gate 2](prompts/gate2.md) instructions.

A text-only assistant can handle Gate 1, but **cannot inspect images**. Report image-content checks as `UNVERIFIED` when actual pixels are unavailable. Every error must cite evidence and a minimal fix. `P0` means blocker; `P1` needs resolution/verification; `P2` is advisory. The creator approves progression. No measured savings are implied by identified issues.

[Workflow](docs/workflow.md) · [Custom agents](docs/custom-agent.md) · [Output schema](schemas/review-result.schema.json) · [Real case](examples/childhood-self/README.md) · [Tests](CONTRIBUTING.md) · [MIT](LICENSE).
