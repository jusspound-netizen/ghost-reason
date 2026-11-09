# Ghost Reason

Trace your AI agent's reasoning, not just its tool calls.

Ghost Reason is a local-first Python package that logs the full reasoning timeline of an AI agent: the prompt, the thought process, the tool call, and the result. It writes everything to a SQLite database and gives you a clean CLI to view the chain of decisions.

## Why use it?

Ghost Tracer shows you *what* the agent did. Ghost Reason shows you *why*.

When an agent drifts, loops, or hallucinates, the tool-call log tells you which tool failed. The reasoning log tells you why the agent chose that tool in the first place.

## Installation

pip install ghost-reason

## Usage

1. Wrap your agent's reasoning:

from ghost_reason import ReasonTracer
tracer = ReasonTracer()
tracer.log("prompt", user_input)
tracer.log("thought", model_response.content)
tracer.log("tool_call", f"{tool_name}({tool_args})")
tracer.log("tool_result", str(result))

2. View the timeline:

ghost-reason view

## License
MIT
