import json
import os
from typing import List, Dict, cast

# File where tasks will be stored
DATA_FILE = "todo_data.json"

# Define a type alias for better readability
Task = Dict[str, object]

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
            return json.load(f)
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

def add_task(text: str) -> Task:
    """
    Create a new task and save it.
    - Automatically assigns an ID based on the last task.
    - Sets the 'done' field to False by default.
    """
    tasks = load_tasks()
    last_id = cast(int, tasks[-1]["id"]) if tasks else 0
    new_id = last_id + 1

    task: Task = {
        "id": new_id,
        "text": text,
        "done": False
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
    return load_tasks()

# ---------------------------
# ✅ Task updates
# ---------------------------

def complete_task(task_id: int) -> bool:
    """
    Mark a task as completed by its ID.
    Returns True if the task was found and updated, False otherwise.
    """
    tasks = load_tasks()
    found = False

    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            found = True
            break

    if found:
        save_tasks(tasks)
        return True
    return False

# ---------------------------
# ❌ Task deletion
# ---------------------------

def clear_tasks() -> None:
    """
    Delete all tasks by saving an empty list.
    """
    save_tasks([])

def delete_task(task_id: int) -> bool:
    """
    Delete a task by its ID.
    Returns True if the task was deleted, False if not found.
    """
    tasks = load_tasks()
    new_tasks = [task for task in tasks if task["id"] != task_id]

    if len(new_tasks) == len(tasks):
        return False

    save_tasks(new_tasks)
    return True