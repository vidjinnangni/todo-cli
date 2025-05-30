# 🗺️ Roadmap – Todo CLI

This roadmap outlines upcoming features and improvements planned for the Todo CLI project. Each section is organized by functionality and potential future milestones.

---

## ✅ Completed

- Core commands: `add`, `list`, `complete`, `delete`, `clear`
- Data persistence via JSON
- Test suite with `pytest`
- CLI distribution via `pyproject.toml`
- TypedDict for task structure
- Initial CI setup (Gitea)
- Installation and usage docs

---

## 🔜 In Progress / Next Steps

- [x] Welcome message on launch
- [x] Add uninstall instructions to README
- [x] Improve test coverage with `TypedDict`-aware assertions
- [ ] Docker usage support

---

## 🧱 Core Features to Add

### ✅ Task Organization & Priority

- [ ] Add support for priority: `high`, `medium`, `low`
- [ ] Sort tasks by priority (`--sort priority`)
- [ ] Filter tasks by priority (`--priority high`)

### 📅 Dates & Reminders

- [ ] Add due dates (`--due 2025-06-01`)
- [ ] Filter tasks due today / overdue
- [ ] Optional: Reminders (via cron or external trigger)

### 🏷️ Categories & Tags

- [ ] Support `--tags work,urgent` when adding tasks
- [ ] Filter by tag: `todo list --tag urgent`

### 🔍 Search

- [ ] Add full-text search: `todo search "groceries"`

### 📊 Statistics

- [ ] Command: `todo stats`
- [ ] Show task completion % and totals by tag/priority

---

## 🎨 User Interface Enhancements

- [ ] Add colors and formatting using [`rich`](https://github.com/Textualize/rich)
- [ ] Display tasks in a table view
- [ ] `--verbose` flag to show more task details

---

## ☁️ Backup & Sync

- [ ] Backup JSON file locally (`.backup.json`)
- [ ] Explore sync with remote (Dropbox, WebDAV, etc.)

---

## ✨ Advanced Commands

- [ ] Edit tasks: `todo edit 3 --text "..." --priority low`
- [ ] Add notes to tasks
- [ ] Support nested subtasks

---

## ⚙️ Configuration

- [ ] Create `~/.config/todo-cli/config.toml`
- [ ] Let users customize defaults (colors, sort, verbosity)

---

## 🔐 Validation & Safety

- [ ] Validate dates, priorities, and flags
- [ ] Confirmation prompt for destructive actions (e.g. `clear`)

---

## 🙌 Contributions Welcome

Feel free to open issues or contribute to any roadmap item. This roadmap is open and evolving based on feedback and needs.