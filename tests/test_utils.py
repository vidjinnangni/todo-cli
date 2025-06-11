# ----------------------------------------------------------
# ✅ Unit Tests for utils.py (presentation layer)
# This module contains unit tests for the utility functions used in the Todo CLI,
# particularly those related to output formatting (e.g., format_task_table).
# It ensures that task tables are formatted as expected in a human-readable layout.
# ----------------------------------------------------------

from todo_cli.core import TaskDict
from todo_cli.utils import format_task_table

# -------------------------------
# 🧪 Mock Data
# -------------------------------
MOCK_TASKS: list[TaskDict] = [
    {
        "id": 1,
        "text": "Read docs",
        "done": True,
        "priority": "high",
        "created": "2024-01-01T10:00:00+00:00",
        "due": "2024-01-10",
        "tags": ["documentation", "reading"]
    },
    {
        "id": 2,
        "text": "Write tests",
        "done": False,
        "priority": "medium",
        "created": "2024-01-02T14:30:00+00:00",
        "due": None,
        "tags": []
    },
    {
        "id": 3,
        "text": "Fix bugs",
        "done": False,
        "priority": "low",
        "created": "2024-01-03T09:15:00+00:00",
        "due": None,
        "tags": None
    }
]

# -------------------------------
# 📋 Test: format_task_table() basic headers
# -------------------------------
def test_format_task_table_includes_headers():
    output = format_task_table(MOCK_TASKS, verbose=True)
    assert "ID" in output
    assert "Status" in output
    assert "Priority" in output
    assert "Task" in output
    assert "Due" in output
    assert "Created" in output
    assert "Tags" in output

# -------------------------------
# 📋 Test: format_task_table() renders data rows
# -------------------------------
def test_format_task_table_renders_rows():
    output = format_task_table(MOCK_TASKS, verbose=True)
    lines = output.splitlines()
    assert len(lines) >= 5  # Header + separator + at least 2 task rows
    assert "1" in lines[2]
    assert "Read docs" in output
    assert "✓" in output  # Completed symbol
    assert "✗" in output  # Not completed symbol
    assert "documentation, reading" in output
    assert "Tags" in lines[0]


# -------------------------------
# 📋 Test: format_task_table() ensures alignment
# -------------------------------
def test_format_task_table_alignment():
    output = format_task_table(MOCK_TASKS)
    lines = output.splitlines()
    content_lines = lines[2:]  # Skip header and separator
    widths = [len(line) for line in content_lines]
    assert len(set(widths)) == 1  # All lines should have the same width


# -------------------------------
# 📋 Test: format_task_table() handles empty task list
# -------------------------------
def test_format_task_table_with_empty_list():
    output = format_task_table([], verbose=True)
    assert "No tasks to display" in output