# ----------------------------------------
# Todo CLI - A simple command-line todo application
# This script provides a command-line interface for managing todo tasks.
# It allows users to add, list, complete, delete, and clear tasks.
# ----------------------------------------

import argparse
from . import core

def main():
    parser = argparse.ArgumentParser(
        description="Todo CLI - A simple command-line todo application"
    )

    subparsers = parser.add_subparsers(dest="command")

    # === add command ===
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("text", help="The content of the task to add")

    # === list command ===
    list_parser = subparsers.add_parser("list", help="List all tasks")
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
  • add "Task content"         ➜ Add a new task
  • list                       ➜ List all tasks
  • list --done                ➜ Show completed tasks only
  • list --undone              ➜ Show uncompleted tasks only
  • complete <id>              ➜ Mark a task as done
  • delete <id>                ➜ Delete a task by ID
  • clear                      ➜ Delete all tasks

ℹ️  Run `todo --help` for more details.
        """)
        return

    if args.command == "add":
        task = core.add_task(args.text)
        print(f'Task added: [{task["id"]}] {task["text"]}')

    elif args.command == "list":
        tasks = core.list_tasks()

        # Handle filtering
        if args.done and args.undone:
            print("⚠️ You can't use --done and --undone together.")
            return

        if args.done:
            tasks = [task for task in tasks if task["done"]]
        elif args.undone:
            tasks = [task for task in tasks if not task["done"]]

        if not tasks:
            print("No tasks found.")
        else:
            for task in tasks:
                status = "✓" if task["done"] else " "
                print(f"[{task['id']}] [{status}] {task['text']}")

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