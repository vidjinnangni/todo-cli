# 🧠 Core Logic Explanation (`core.py`)

This file contains the **business logic** for the Todo CLI application.  
All core operations like adding, listing, marking, and clearing tasks are defined here.

## 📄 Storage

- Tasks are stored in a file: `todo_data.json`
- The format is JSON, with a list of objects:

```json
[
  { "id": 1, "text": "Buy milk", "done": false }
]
```

## Task Type

A task is represented as:

```json
{
  "id": int,
  "text": str,
  "done": bool
}
```
The type alias Task = Dict[str, object] is used in core.py for readability.


## 🧩 Function Summary

| Function              | Description                                      |
|-----------------------|--------------------------------------------------|
| `load_tasks()`        | Load tasks from the JSON file                    |
| `save_tasks(tasks)`   | Save tasks to the JSON file                      |
| `add_task(text)`      | Create and add a new task                        |
| `list_tasks()`        | Return all existing tasks                        |
| `complete_task(id)`   | Mark a task as completed by its ID               |
| `clear_tasks()`       | Delete all tasks from the list                   |

## 🗂️ File Organization (`core.py`)

To make the code more maintainable, functions in core.py are grouped by responsibility.

| Section                 | Responsibility                                   | Functions                   |
|--------------------------|--------------------------------------------------|------------------------------|
| 🔄 File operations       | Load and save task data in JSON format           | `load_tasks`, `save_tasks`   |
| ➕ Task creation         | Add new tasks with automatic ID and status       | `add_task`                   |
| 📄 Task reading          | Read and return task data                        | `list_tasks`                 |
| ✅ Task updates          | Modify the status of tasks                       | `complete_task`              |
| ❌ Task deletion         | Remove tasks individually or all at once         | `delete_task`, `clear_tasks` |

---

## 📚 Notes

- If the file is missing or contains invalid JSON, the app falls back to an empty list.
- Task IDs are automatically incremented based on the highest existing ID.
- Tasks are saved immediately after any change.
- This structure can be refactored later to support other backends like SQLite, CSV, or an API.