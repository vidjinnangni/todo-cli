# 🧠 Core Logic Explanation (`core.py`)

This file contains the **business logic** for the Todo CLI application.  
All core operations like adding, listing, marking, and clearing tasks are defined here.

## 📄 Storage

- Tasks are stored in a file: `todo_data.json`
- The format is JSON, with a list of objects:

```json
[
  {
    "id": 1,
    "text": "Buy milk",
    "done": false,
    "priority": "medium",
    "created": "2025-06-01T10:00:00+00:00",
    "due": "2025-06-10"
  }
]
```

## Task structure

Each task is defined using a TypedDict for type safety and readability:

```python
class TaskDict(TypedDict):
  id: int
  text: str
  done: bool
  priority: Literal["low", "medium", "high"]
  created: str            # ISO 8601 timestamp
  due: Optional[str]      # Optional due date (YYYY-MM-DD)
```

- The default priority for new tasks is "medium".
- The created field is always generated automatically.
- The due field is optional and can be left blank.

## 🧩 Function Summary

| Function              | Description                                      |
|-----------------------|--------------------------------------------------|
| `load_tasks()`        | Load tasks from the JSON file                    |
| `save_tasks(tasks)`   | Save tasks to the JSON file                      |
| `add_task(text)`      | Add a new task with optional priority and due date   |
| `list_tasks()`        | Return all existing tasks                        |
| `complete_task(id)`   | Mark a task as completed by ID                   |
| `delete_task(id)`     | Delete a task by ID                              |
| `clear_tasks()`       | Remove all tasks from the list                   |

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

- Task IDs are incremented automatically.
- If the storage file is missing or invalid, an empty list is returned.
- All tasks are stored in JSON with indent=2 and ensure_ascii=False.
- The design is modular and easy to extend to:
  - Tags or categories
  - Date reminders or recurring tasks
  - Database or cloud backends
  