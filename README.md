# 📝 To-Do List (Console-based)

A simple **Python console-based To-Do List Application** that lets you add, view, and remove tasks.  
Tasks are saved in a text file so they persist even after restarting the program.  

---

## 🚀 Features
- 📋 **View tasks** – See all your saved tasks.  
- ➕ **Add task** – Add a new task to your list.  
- ❌ **Remove task** – Remove a task by its number.  
- 💾 **Persistent storage** – Tasks are stored in `tasks.txt`.  

---

## ⚙️ Functions & Use Cases
- `load_task()` → Loads tasks from `tasks.txt` when the program starts.
- `save_task(tasks)` → Saves the updated task list into `tasks.txt`.
- `view_task(tasks)` → Displays all tasks with numbering.
- `add_task(tasks)` → Adds a new task entered by the user.
- `remove_task(tasks)` → Removes a task by its task number.
- `main()` → Runs the main program loop with menu options.
