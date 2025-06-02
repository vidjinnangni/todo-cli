# 🚀 Commands Plan (`todo` CLI)

This document describes all available (and planned) commands for the Todo CLI.

---

## 📚 Command Overview

This table summarizes the available commands for the Todo CLI application.

| Command            | Syntax                                                             | Description                                                |
|--------------------|---------------------------------------------------------------------|------------------------------------------------------------|
| `add`              | `todo add "task content" [--priority low|medium|high]`             | Add a new task with optional priority (default: medium)    |
| `list`             | `todo list`                                                        | List all tasks (completed + not completed)                 |
| `list --done`      | `todo list --done`                                                 | Show only completed tasks                                  |
| `list --undone`    | `todo list --undone`                                               | Show only uncompleted tasks                                |
| `list --priority`  | `todo list --priority high`                                        | Show tasks filtered by priority                            |
| `list --sort`      | `todo list --sort priority`                                        | Sort tasks by priority (high > medium > low)               |
| `complete`         | `todo complete <id>`                                               | Mark a task as completed                                   |
| `delete`           | `todo delete <id>`                                                 | Delete a task by its ID                                    |
| `clear`            | `todo clear`                                                       | Delete all tasks                                           |

⚠️ **Notes:**
- `--done` and `--undone` are mutually exclusive.
- You can combine `--priority` and `--sort`, but they are optional.
- Priority values are: `low`, `medium`, and `high`.

---

## ✅ Examples

```bash
todo add "Read a book"
todo add "Fix bug" --priority high
todo list
todo list --done
todo list --priority high
todo list --sort priority
todo complete 2
todo delete 1
todo clear
```

## 🛠️ Notes

- All commands are subcommands defined with argparse in main.py
- Each command maps to a function in core.py
- The CLI is easily extensible: just add a parser and a corresponding function call