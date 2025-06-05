# ----------------------------------------------------------
# ✅ Unit Tests for core.py (Todo CLI logic)
# This module contains unit tests for the core functionality of the Todo CLI application.
# It tests task management operations such as adding, listing, completing, deleting, and clearing tasks.
# It uses pytest for testing and a separate test data file to avoid conflicts with production data.
# ----------------------------------------------------------

import os
import pytest
from todo_cli import core
from typing import List
from todo_cli.core import TaskDict

# -------------------------------
# 🔧 Use test-specific data file
# -------------------------------
core.DATA_FILE = "test_todo_data.json"

# -------------------------------
# 🧹 Test isolation fixture
# Automatically run before & after each test to clean the test data file
# -------------------------------
@pytest.fixture(autouse=True)
def cleanup_test_file():
    if os.path.exists(core.DATA_FILE):
        os.remove(core.DATA_FILE)
    yield
    if os.path.exists(core.DATA_FILE):
        os.remove(core.DATA_FILE)

# -------------------------------
# ➕ Test: add_task()
# -------------------------------
# This test checks if a new task is created correctly with default values.
def test_add_task_creates_new_task():
    task: TaskDict = core.add_task("Write unit tests")
    assert task == {
        "id": 1, # Assuming this is the first task, ID should be 1
        "text": "Write unit tests", # Task text
        "done": False, # New task should not be done
        "priority": "medium", # Default priority
        "created": task["created"],  # Ensure created date is set
        "due": ""  # Default due date is empty
    }

# This test checks if a new task can be added with a specific priority.
def test_add_task_with_custom_priority():
    task: TaskDict = core.add_task("Urgent fix", priority="high")
    assert task["priority"] == "high"

# -------------------------------
# 📄 Test: list_tasks()
# -------------------------------
def test_list_tasks_returns_all_added_tasks():
    core.add_task("Task 1")
    core.add_task("Task 2", priority="low")
    tasks: List[TaskDict] = core.list_tasks()
    assert len(tasks) == 2
    assert tasks[0]["text"] == "Task 1"
    assert tasks[0]["priority"] == "medium"
    assert tasks[1]["text"] == "Task 2"
    assert tasks[1]["priority"] == "low"

# -------------------------------
# ✅ Test: complete_task()
# -------------------------------
def test_complete_task_marks_as_done():
    task = core.add_task("Complete this task")
    result = core.complete_task(task["id"])
    assert result is not None
    assert result["done"] is True

def test_complete_task_fails_for_nonexistent_id():
    result = core.complete_task(999)
    assert result is None

# -------------------------------
# ❌ Test: clear_tasks()
# -------------------------------
def test_clear_tasks_deletes_all():
    core.add_task("Task 1")
    core.add_task("Task 2")
    core.clear_tasks()
    tasks: List[TaskDict] = core.list_tasks()
    assert tasks == []

# -------------------------------
# ❌ Test: delete_task()
# -------------------------------
def test_delete_task_removes_specific_task():
    t1 = core.add_task("Keep me")
    core.add_task("Delete me")
    result = core.delete_task(t1["id"])
    assert result is not None
    tasks = core.list_tasks()
    assert len(tasks) == 1
    assert tasks[0]["text"] == "Delete me"

def test_delete_task_fails_for_nonexistent_id():
    result = core.delete_task(12345)
    assert result is None

# -------------------------------
# 🧪 Sorting & Filtering (core logic-based)
# -------------------------------
def test_tasks_sorted_by_priority():
    core.add_task("Low priority", priority="low")
    core.add_task("High priority", priority="high")
    core.add_task("Medium priority", priority="medium")
    tasks = sorted(core.list_tasks(), key=lambda t: ("high", "medium", "low").index(t["priority"]))
    priorities = [task["priority"] for task in tasks]
    assert priorities == ["high", "medium", "low"]

def test_tasks_filtered_by_priority():
    core.add_task("Important", priority="high")
    core.add_task("Trivial", priority="low")
    filtered = [t for t in core.list_tasks() if t["priority"] == "high"]
    assert len(filtered) == 1
    assert filtered[0]["text"] == "Important"
    assert filtered[0]["priority"] == "high"
