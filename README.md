# Ghost Reason

Trace your AI agent's reasoning, not just its tool calls.

Ghost Reason is a local-first Python package that logs the full reasoning timeline of an AI agent. It writes everything to a SQLite database and gives you a clean CLI to view the chain of decisions.

## Why use it?

Ghost Tracer shows you *what* the agent did. Ghost Reason shows you *why*.

## Installation

```bash
pip install ghost-reason
```

## Usage

```python
from ghost_reason import ReasonTracer
tracer = ReasonTracer()
tracer.log("prompt", user_input)
tracer.log("thought", model_response.content)
tracer.log("tool_call", f"{tool_name}({tool_args})")
tracer.log("tool_result", str(result))
```

## View the timeline

```bash
ghost-reason view
```

## License

MIT
---

### 🛠️ Ready-to-use Agent Skills
Reasoning traces are great for debugging, but they also reveal where your agent is wasting tokens. Use the **Agent Cost Auditor** skill on Agensi to analyze your `ghost-reason` logs and get a quantified savings report.
👉 **[Get Agent Cost Auditor on Agensi](https://www.agensi.io/r/CONTEXTBRIDGE?to=/skills/agent-cost-auditor)**