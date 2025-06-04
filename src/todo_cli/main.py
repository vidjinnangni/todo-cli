# ----------------------------------------
# Todo CLI - A simple command-line todo application
# This script provides a command-line interface for managing todo tasks.
# It allows users to add, list, complete, delete, and clear tasks.
# ----------------------------------------

import argparse
from . import core

def print_message(kind: str, message: str) -> None:
    icons = {
        "success": "✅",
        "delete": "🗑️",
        "error": "❌",
        "warning": "⚠️",
        "info": "ℹ️",
    }
    prefix = icons.get(kind, "")
    print(f"{prefix} {message}")

def main():
    parser = argparse.ArgumentParser(
        description="📝 Todo CLI – A simple and minimalist command-line todo manager.",
        epilog="🔎 Use 'todo <command> --help' to get more details about a specific command."
    )

    subparsers = parser.add_subparsers(dest="command", title="Available commands", metavar="")

    # === add command ===
    add_parser = subparsers.add_parser("add", help="Add a new task", description="Add a new task to your todo list with optional priority.")
    add_parser.add_argument("text", help="The content of the task to add")
    add_parser.add_argument(
        "--priority",
        choices=["low", "medium", "high"],
        default="medium",
        help="Set task priority (default: medium)"
    )

    # === list command ===
    list_parser = subparsers.add_parser("list", help="List all tasks", description="List all tasks in your todo list with optional filters and sorting.")
    list_parser.add_argument(
        "--done",
        action="store_true",
        help="Show only completed tasks"
    )
    list_parser.add_argument(
        "--undone",
        action="store_true",
        help="Show only uncompleted tasks"
    )
    list_parser.add_argument(
        "--priority",
        choices=["low", "medium", "high"],
        help="Filter tasks by priority"
    )
    list_parser.add_argument(
        "--sort",
        choices=["priority"],
        help="Sort tasks by field (currently only 'priority' is supported)"
    )

    # === complete command ===
    complete_parser = subparsers.add_parser("complete", help="Mark a task as completed")
    complete_parser.add_argument("id", type=int, help="ID of the task to complete")

    # === clear command ===
    subparsers.add_parser("clear", help="Delete all tasks")

    # === delete command ===
    delete_parser = subparsers.add_parser("delete", help="Delete a task by its ID")
    delete_parser.add_argument("id", type=int, help="ID of the task to delete")

    args = parser.parse_args()

    if not args.command:
        print("""
👋 Welcome to todo-cli!

This is a simple and minimalist command-line todo manager.

📦 Available commands:
• todo add "Task content" [--priority low|medium|high]               ➜ Add a new task with optional priority (default: medium)
• todo list [--done | --undone] [--priority ...] [--sort priority]   ➜ List tasks with optional filters and sorting
• todo complete <id>                                                 ➜ Mark a task as completed by ID
• todo delete <id>                                                   ➜ Delete a task by ID
• todo clear                                                         ➜ Delete all tasks

ℹ️  Run `todo --help` for more details.
        """)
        return

    # Add command handling
    if args.command == "add":
        task = core.add_task(args.text, priority=args.priority)
        print_message("success", f'Task added: [{task["id"]}] {task["text"]} (priority: {task["priority"]})')
        print_message("info", "You can now list your tasks with `todo list`.")

    # List command handling
    elif args.command == "list":
        tasks = core.list_tasks()

        # Validate and apply --done / --undone
        if args.done and args.undone:
            print_message("warning", "You can't use --done and --undone together.")
            print_message("info", "Please choose one of them to filter tasks.")
            return
        
        if args.done:
            tasks = [task for task in tasks if task["done"]]
        elif args.undone:
            tasks = [task for task in tasks if not task["done"]]

        # Filter by priority
        if args.priority:
            tasks = [t for t in tasks if t["priority"] == args.priority]

        # Sort by priority if needed
        if args.sort == "priority":
            priority_order = {"high": 0, "medium": 1, "low": 2}
            tasks.sort(key=lambda t: priority_order.get(t["priority"], 1))

        if not tasks:
            print_message("info", "No tasks found.")
        else:
            for task in tasks:
                    status = "✓" if task["done"] else " "
                    priority = task.get("priority", "medium")  # Default fallback
                    print(f"[{task['id']}] [{status}] {task['text']} (priority: {priority})")

    # Complete command handling
    elif args.command == "complete":
        task = core.complete_task(args.id)
        if task:
            print_message("success", f'Task [{task["id"]}] "{task["text"]}" marked as done!')
        else:
            print_message("error", f"Sorry, task [{args.id}] not found.")

    # Clear command handling
    elif args.command == "clear":
        core.clear_tasks()
        print_message("info", "All tasks cleared.")

    # Delete command handling   
    elif args.command == "delete":
        task = core.delete_task(args.id)
        if task:
            print_message("delete", f'Task [{task["id"]}] "{task["text"]}" deleted.')
        else:
            print_message("error", f"Sorry, task [{args.id}] not found.")

    # Handle unknown commands
    else:
        print_message("error", "Unknown command. Use `todo --help` to see available commands.")