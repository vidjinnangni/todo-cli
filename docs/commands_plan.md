# 🚀 Commands Plan (`todo` CLI)

This document describes all available (and planned) commands for the Todo CLI.

---

## 📚 Command Overview

This table summarizes the available commands for the Todo CLI application.

| Command              | Syntax                                                                 | Description                                                |
|----------------------|------------------------------------------------------------------------|------------------------------------------------------------|
| `add`                | `todo add "task content" [--priority low\|medium\|high] [--due YYYY-MM-DD]` | Add a new task with optional priority and due date    |
| `list`               | `todo list`                                                            | List all tasks (completed + not completed)                 |
| `list --done`        | `todo list --done`                                                     | Show only completed tasks                                  |
| `list --undone`      | `todo list --undone`                                                   | Show only uncompleted tasks                                |
| `list --priority`    | `todo list --priority [low\|medium\|high]`                             | Filter tasks by priority                                   |
| `list --sort`        | `todo list --sort priority`                                            | Sort tasks by priority (high > medium > low)               |
| `list --verbose`     | `todo list --verbose`                                                  | Show detailed task info (includes creation date)           |
| `complete`           | `todo complete <id>`                                                   | Mark a task as completed                                   |
| `delete`             | `todo delete <id1> <id2> ...`                                          | Delete one or more tasks by ID                             |
| `clear`              | `todo clear`                                                           | Delete all tasks                                           |

⚠️ **Notes:**

- `--done` and `--undone` cannot be used together.
- `--priority` and `--sort` can be combined or used independently.
- Valid priority levels are: `low`, `medium`, and `high` (default: `medium`).

---

## ✅ Examples

```bash
todo add "Prepare slides" --priority high --due 2025-07-01
  todo add "Renew passport" --due 2025-06-10 # Default priority: medium
todo list
todo list --verbose
todo list --done
todo list --priority high
todo list --sort priority
todo complete 2
todo delete 1
todo delete 2 3
todo clear
```

## 🛠️ Notes

- All commands are subcommands defined with argparse in main.py
- Each command maps to a function in core.py
- The CLI is easily extensible: just add a parser and a corresponding function call.
