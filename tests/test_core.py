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
def test_add_task_creates_new_task():
    task: TaskDict = core.add_task("Write unit tests")
    assert task == {"id": 1, "text": "Write unit tests", "done": False}

# -------------------------------
# 📄 Test: list_tasks()
# -------------------------------
def test_list_tasks_returns_all_added_tasks():
    core.add_task("Task 1")
    core.add_task("Task 2")
    tasks: List[TaskDict] = core.list_tasks()
    assert len(tasks) == 2
    assert tasks[0]["text"] == "Task 1"
    assert tasks[1]["text"] == "Task 2"

# -------------------------------
# ✅ Test: complete_task()
# -------------------------------
def test_complete_task_marks_as_done():
    task = core.add_task("Complete this task")
    result: bool = core.complete_task(task["id"])
    assert result is True
    tasks = core.list_tasks()
    assert tasks[0]["done"] is True

def test_complete_task_fails_for_nonexistent_id():
    result: bool = core.complete_task(999)
    assert result is False

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
    result: bool = core.delete_task(t1["id"])
    assert result is True
    tasks = core.list_tasks()
    assert len(tasks) == 1
    assert tasks[0]["text"] == "Delete me"

def test_delete_task_fails_for_nonexistent_id():
    result: bool = core.delete_task(12345)
    assert result is False