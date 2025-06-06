# ----------------------------------------
# 🧰 Utils Module for Todo CLI X
# Contains reusable helpers for printing messages and formatting output.
# ----------------------------------------

from typing import List
from .core import TaskDict

# -------------------------------
# 🎨 Message display utility
# -------------------------------

def print_message(kind: str, message: str) -> None:
    """
    Print a message with a contextual icon prefix.
    Supported kinds: success, delete, error, warning, info
    """
    icons = {
        "success": "✅",
        "delete": "🗑️",
        "error": "❌",
        "warning": "⚠️",
        "info": "ℹ️",
    }
    prefix = icons.get(kind, "")
    print(f"{prefix}  {message.lstrip()}")  # Extra space for better UX


# -------------------------------
# 📋 Task table formatter
# -------------------------------

def format_task_table(tasks: List[TaskDict], verbose: bool = False) -> str:
    """
    Return a formatted string displaying tasks in a table layout.
    Columns: ID | Status | Priority | Task [| Created]
    """
    if not tasks:
        return "⚠️  No tasks to display."

    headers = ["ID", "Status", "Priority", "Task", "Due"]
    if verbose:
        headers.append("Created")

    rows: List[List[str]] = []
    for task in tasks:
        done = "✓" if task["done"] else "✗"
        row: List[str] = [
            str(task["id"]),
            done,
            task["priority"],
            task["text"],
            task.get("due") or ""  # Use empty string if 'due' is not set
        ]
        if verbose:
            row.append(task.get("created", ""))  # fallback for retrocompatibility
        rows.append(row)

    # Determine column widths
    columns = list(zip(*([headers] + rows)))
    col_widths: List[int] = [max(len(str(cell)) for cell in col) for col in columns]

    # Build table lines
    table_lines: List[str] = []

    header_line = "  ".join(h.ljust(w) for h, w in zip(headers, col_widths))
    table_lines.append(header_line)

    separator = "  ".join("─" * w for w in col_widths)
    table_lines.append(separator)

    for row in rows:
        line = "  ".join(str(cell).ljust(w) for cell, w in zip(row, col_widths))
        table_lines.append(line)

    return "\n".join(table_lines)

# -------------------------------
# 📊 Task summary printer
# -------------------------------

def print_task_summary(tasks: List[TaskDict]) -> None:
    """
    Print a summary of task statistics: total, completed, and remaining.
    """
    total = len(tasks)
    done = sum(1 for t in tasks if t["done"])
    left = total - done
    plural = "s" if total != 1 else ""

    if total == 0:
        print_message("info", "No tasks available.")
        return

    # Spacing for readability
    print()
    print_message("info", f"{total} task{plural} — {done} completed, {left} remaining")