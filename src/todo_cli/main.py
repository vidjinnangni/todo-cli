# ----------------------------------------
# Todo CLI - A simple command-line todo application
# This script provides a command-line interface for managing todo tasks.
# It allows users to add, list, complete, delete, and clear tasks.
# ----------------------------------------

import argparse
from . import core

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

    if args.command == "add":
        task = core.add_task(args.text, priority=args.priority)
        print(f'Task added: [{task["id"]}] {task["text"]} (Priority: {task["priority"]})')

    elif args.command == "list":
        tasks = core.list_tasks()

        # Validate and apply --done / --undone
        if args.done and args.undone:
            print("⚠️ You can't use --done and --undone together.")
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
            tasks.sort(key=lambda t: priority_order.get(t["priority"], 99))

        if not tasks:
            print("No tasks found.")
        else:
            for task in tasks:
                    status = "✓" if task["done"] else " "
                    priority = task.get("priority", "medium")  # Default fallback
                    print(f"[{task['id']}] [{status}] {task['text']} (priority: {priority})")

    elif args.command == "complete":
        success = core.complete_task(args.id)
        if success:
            print(f"Task {args.id} marked as completed.")
        else:
            print(f"Task {args.id} not found.")

    elif args.command == "clear":
        core.clear_tasks()
        print("All tasks cleared.")

    elif args.command == "delete":
        success = core.delete_task(args.id)
        if success:
            print(f"Task {args.id} deleted.")
        else:
            print(f"Task {args.id} not found.")

    else:
        print("Unknown command. Use `todo --help` to see available commands.")