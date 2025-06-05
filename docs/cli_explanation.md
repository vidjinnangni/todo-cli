# 🧠 CLI Entry Point (`main.py`)

This module defines the command-line interface for the Todo CLI app using Python's built-in `argparse` module.

- Located at: `src/todo_cli/main.py`
- Responsible for parsing user commands and calling the appropriate logic from `core.py`
- Uses `argparse` subparsers for clean and extendable command dispatching

## 📂 Location

`src/todo_cli/main.py`

## ⚙️ Command Flow Overview

| Line / Code                                | Explanation                                                               |
|--------------------------------------------|---------------------------------------------------------------------------|
| `import argparse`                          | Standard library to handle command-line arguments                         |
| `from . import core`                       | Imports the task logic from `core.py`                                     |
| `argparse.ArgumentParser(...)`             | Initializes the main parser                                               |
| `subparsers = parser.add_subparsers(...)`  | Allows for multiple subcommands (add, list, etc.)                         |
| `add_parser = subparsers.add_parser(...)`  | Defines the `add` command                                                 |
| `add_parser.add_argument(...)`             | Adds a required task text argument                                        |
| `args = parser.parse_args()`               | Parses user input from the command line                                   |
| `if args.command == "add":`                | Checks which command is being called and dispatches to the right logic    |
| `print(...)`                               | CLI output/feedback to the user                                           |

---

## 📦 Available Commands

| Command   | Syntax                                                                | Description                           |
|-----------|-----------------------------------------------------------------------|---------------------------------------|
| `add`     | `todo add "Task" [--priority low/medium/high] [--due YYYY-MM-DD]`     | Add a new task with priority and due  |
| `list`    | `todo list [--done] [--undone] [--priority LEVEL] [--sort priority] [--verbose]` | List tasks with filters, sort or full details |
| `complete`| `todo complete <id>`                                                  | Mark a task as completed              |
| `delete`  | `todo delete <id> [id ...]`                                           | Delete one or more tasks by ID        |
| `clear`   | `todo clear`                                                          | Delete all tasks                      |

You can also run help for each subcommand:

```bash
todo add --help
todo list --help
```

---

## ✅ Examples

```bash
todo add "Submit report" --priority high --due 2025-06-10

todo list
todo list --verbose
todo list --priority high
todo list --sort priority
todo list --done

todo complete 1
todo delete 1
todo delete 2 3 4
todo clear
```

## 🏷️ Flags & Filters

| Flag        | Description                                |
|-------------|--------------------------------------------|
| `--priority`| Filter by or assign priority               |
| `--due`     | Add a due date to a task (YYYY-MM-DD)      |
| `--done`    | Show only completed tasks                  |
| `--undone`  | Show only uncompleted tasks                |
| `--sort`    | Sort tasks (currently only by priority)    |
| `--verbose` | Show detailed task info including `created`|

## 🧪 Testing Your CLI

First, sync your environment with uv:

```bash
uv sync
```

Then, try some commands using uv run:

```bash
uv run todo add "Submit report" --priority high --due 2025-06-10
uv run todo list
```

Or with environment activation:

```bash
source .venv/bin/activate
todo add "Submit report" --priority high --due 2025-06-10
```

## 🔍 Notes

- All commands are handled through argparse subparsers.
- Each subcommand maps cleanly to logic defined in core.py.
- New commands can be added easily by repeating the add_parser pattern.
- The main() function acts as the dispatch layer, keeping CLI modular and maintainable.

➡️ This design makes the CLI clean, extensible, and aligned with best practices.
