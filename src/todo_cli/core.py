# ----------------------------------------
# 📝 Todo CLI X Core Module
# This module contains the core logic for the Todo CLI application.
# It handles task management including creation, listing, updating, and deletion.
# It uses a JSON file to persist tasks across sessions.
# ----------------------------------------

import json
import os
from datetime import datetime, timezone
from typing import List, Literal, TypedDict, Optional

# ----------------------------------------
# 📦 TypedDict for tasks with priority
# ----------------------------------------

Priority = Literal["low", "medium", "high"]

class TaskDict(TypedDict):
    id: int
    text: str
    done: bool
    priority: Priority
    created: str
    due: Optional[str]

Task = TaskDict

# Allowed priority values
VALID_PRIORITIES: tuple[Priority, ...] = ("low", "medium", "high")

# ----------------------------------------
# 📁 Data file
# ----------------------------------------
# File where tasks will be stored
DATA_FILE = "todo_data.json"

# ---------------------------
# 🔄 File operations
# ---------------------------

def load_tasks() -> List[Task]:
    """
    Load the task list from the JSON file.
    If the file does not exist or is invalid, return an empty list.
    """
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        try:
            tasks = json.load(f)
            for task in tasks:
                if "created" not in task:
                    task["created"] = ""
                if "due" not in task:
                    task["due"] = ""
            return tasks
        except json.JSONDecodeError:
            return []

def save_tasks(tasks: List[Task]) -> None:
    """
    Save the task list to the JSON file.
    Tasks are stored with indentation and Unicode support.
    """
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2, ensure_ascii=False)

# ---------------------------
# ➕ Task creation
# ---------------------------

def add_task(text: str, priority: Priority = "medium", due: Optional[str] = None) -> Task:
    """
    Create a new task and save it.
    - Automatically assigns an ID based on the last task.
    - Sets the 'done' field to False by default.
    """
    if priority not in VALID_PRIORITIES:
        raise ValueError(f"Invalid priority: {priority}. Must be one of {VALID_PRIORITIES}.")
        
    # Load existing tasks to determine the next ID
    tasks = load_tasks()
    last_id = tasks[-1]["id"] if tasks else 0
    new_id = last_id + 1

    # Create the new task with the next ID
    task: Task = {
        "id": new_id,
        "text": text,
        "done": False,
        "priority": priority,
        "created": datetime.now(timezone.utc).isoformat(timespec="seconds"), # Store creation time in ISO format
        "due": due or "",
    }

    tasks.append(task)
    save_tasks(tasks)
    return task

# ---------------------------
# 📄 Task reading
# ---------------------------

def list_tasks() -> List[Task]:
    """
    Return all saved tasks.
    """
    tasks = load_tasks()
    for task in tasks:
        if "created" not in task:
            task["created"] = ""
    return tasks

# ---------------------------
# ✅ Task completion
# ---------------------------

def complete_task(task_id: int) -> Task | None:
    """
    Mark a task as completed by its ID.
    Returns the updated task if found and updated, None otherwise.
    """
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            save_tasks(tasks)
            return task
    return None

# ---------------------------
# ❌ Task deletion
# ---------------------------

def clear_tasks() -> None:
    """
    Delete all tasks by saving an empty list.
    """
    save_tasks([])

def delete_task(task_id: int) -> Task | None:
    """
    Delete a task by its ID.
    Returns the deleted task if found and removed, None otherwise.
    """
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            save_tasks(tasks)
            return task
    return None