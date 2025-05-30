# 🧠 CLI Entry Point Explanation (`main.py`)

This file defines the command-line interface for the Todo CLI app using Python's built-in `argparse` module.

## 📂 Location

`src/todo_cli/main.py`

## ⚙️ Command Flow Overview

| Line / Code                                | Explanation                                                               |
|--------------------------------------------|---------------------------------------------------------------------------|
| `import argparse`                          | Standard library to handle command-line arguments                         |
| `from . import core`                       | Imports the task logic from `core.py`                                     |
| `argparse.ArgumentParser(...)`             | Creates the main parser                                                   |
| `subparsers = parser.add_subparsers(...)`  | Allows for multiple subcommands (add, list, etc.)                         |
| `add_parser = subparsers.add_parser(...)`  | Defines the `add` command                                                 |
| `add_parser.add_argument(...)`             | Adds a required task text argument                                        |
| `args = parser.parse_args()`              | Parses user input from the command line                                   |
| `if args.command == "add":`               | Checks which command is being called and dispatches to the right logic   |
| `print(...)`                              | CLI output/feedback to the user                                           |

---

## 📦 Available Commands

| Command              | Syntax                            | Description                                  |
|----------------------|------------------------------------|----------------------------------------------|
| `add`                | `todo add "task content"`          | Adds a new task                              |
| `list`               | `todo list [--done]`               | Lists all tasks (or only completed if `--done`) |
| `complete`           | `todo complete <id>`               | Marks a task as completed                    |
| `delete`             | `todo delete <id>`                 | Deletes a task by ID                         |
| `clear`              | `todo clear`                       | Removes all tasks                            |

---

## ✅ Examples

```bash
todo add "Read a book"
todo list
todo complete 1
todo list --done
todo delete 1
todo clear
```

## 🔍 Notes

- All commands are handled through argparse subparsers.
- New commands can be easily added by following the existing pattern.
- Help is available for each subcommand:

```bash
todo add --help
todo list --help
```

➡️ This modular approach keeps CLI parsing and business logic separated and clean.