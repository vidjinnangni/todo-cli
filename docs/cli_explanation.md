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
| `argparse.ArgumentParser(...)`             | Initializes the main parser|
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

You can also run help for each subcommand:

```bash
todo add --help
todo list --help
```

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

## 🧪 Testing Your CLI

First, sync your environment with uv:

```bash
uv sync
```

Then, try some commands using uv run:

```bash
uv run todo add "Test the CLI"
uv run todo list
uv run todo complete 1
uv run todo delete 1
```

Or with environment activation:

```bash
source .venv/bin/activate
todo list
```

## 🔍 Notes

- All commands are handled through argparse subparsers.
- Each subcommand maps cleanly to logic defined in core.py.
- New commands can be added easily by repeating the add_parser pattern.
- The main() function acts as the dispatch layer, keeping your CLI modular and maintainable.

➡️ This design cleanly separates user interface from business logic, making your code easy to test and extend.