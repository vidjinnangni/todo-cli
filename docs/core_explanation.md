# 🧠 Core Logic Explanation (`core.py`)

This file contains the **business logic** for the Todo CLI application.  
All core operations like adding, listing, marking, and clearing tasks are defined here.

## 📄 Storage

- Tasks are stored in a file: `todo_data.json`
- The format is JSON, with a list of objects:

```json
[
  { "id": 1, "text": "Buy milk", "done": false, "priority": "medium" }
]
```

## Task structure

Each task is defined using a TypedDict for type safety and readability:

```python
{
class TaskDict(TypedDict):
    id: int
    text: str
    done: bool
    priority: Literal["low", "medium", "high"]
}
```

The default priority for new tasks is "medium".

## 🧩 Function Summary

| Function              | Description                                      |
|-----------------------|--------------------------------------------------|
| `load_tasks()`        | Load tasks from the JSON file                    |
| `save_tasks(tasks)`   | Save tasks to the JSON file                      |
| `add_task(text)`      | Create and add a new task (optional priority)    |
| `list_tasks()`        | Return all existing tasks                        |
| `complete_task(id)`   | Mark a task as done. Returns the task, or None if not found|
| `delete_task(id)`     | Delete a task by ID. Returns the task, or None if not found|
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

- Task IDs are incremental and persistent
- Invalid/missing file → fallback to empty list
- JSON output is UTF-8 and indented for readability
- Structure is ready for evolution toward:
  - Categories/tags
  - Dates
  - Rich output
  - Cloud sync or database backend
  