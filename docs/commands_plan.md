# 🚀 Commands Plan (`todo` CLI)

This document describes all available (and planned) commands for the Todo CLI.

## 📚 Command Overview

This table summarizes the available commands for the Todo CLI application.

| Command            | Syntax                             | Description                                  |
|--------------------|-------------------------------------|----------------------------------------------|
| `add`              | `todo add "task content"`           | Add a new task with the given text           |
| `list`             | `todo list`                         | List all tasks (completed + not completed)   |
| `list --done`      | `todo list --done`                  | Show only completed tasks                    |
| `list --undone`    | `todo list --undone`                | Show only uncompleted tasks                  |
| `complete`         | `todo complete <id>`                | Mark a task as completed                     |
| `delete`           | `todo delete <id>`                  | Delete a task by its ID                      |
| `clear`            | `todo clear`                        | Delete all tasks                             |

⚠️ **Note:** `--done` and `--undone` are mutually exclusive. You should not use them together.

---

## ✅ Examples

```bash
todo add "Learn Python"
todo list
todo list --done
todo complete 1
todo delete 1
todo clear
```

## 🛠️ Notes

- All commands are subcommands defined with argparse in main.py
- Each command maps to a function in core.py
- The CLI is easily extensible: just add a parser and a corresponding function call