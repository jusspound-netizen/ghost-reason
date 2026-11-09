import cyclopts
from rich.console import Console
from rich.table import Table
from ghost_reason.tracer import ReasonTracer

app = cyclopts.App(help="Ghost Reason: Trace the reasoning, not just the actions.")
console = Console()

@app.command
def view(limit: int = 50, db: str = "ghost_reason.db"):
    """View the agent's reasoning timeline."""
    tracer = ReasonTracer(db)
    timeline = tracer.get_timeline(limit)

    if not timeline:
        console.print("[yellow]No reasoning steps found.[/yellow]")
        return

    table = Table(title="Ghost Reasoning Timeline")
    table.add_column("Step", style="bold")
    table.add_column("Content", style="cyan")
    table.add_column("Time", justify="right")

    for row in timeline:
        step_color = {
            "prompt": "blue",
            "thought": "yellow",
            "tool_call": "magenta",
            "tool_result": "green",
        }.get(row["step_type"], "white")
        
        table.add_row(
            f"[{step_color}]{row['step_type'].upper()}[/{step_color}]",
            row["content"][:80] + ("..." if len(row["content"]) > 80 else ""),
            f"{row['timestamp']:.2f}"
        )

    console.print(table)

@app.command
def clear(db: str = "ghost_reason.db"):
    """Clear the reasoning database."""
    tracer = ReasonTracer(db)
    tracer.clear()
    console.print("[green]Reasoning database cleared.[/green]")
