import file_handler

def add_task(task):
    """Add a new task to the list."""
    tasks = file_handler.read_tasks()
    tasks.append(task)
    file_handler.write_tasks(tasks)
    print("Task added successfully.")

def remove_task(task_index):
    """Remove a task by its index."""
    tasks = file_handler.read_tasks()
    try:
        removed = tasks.pop(task_index)
        file_handler.write_tasks(tasks)
        print(f"Task '{removed}' removed successfully.")
    except IndexError:
        print("Error: Task number is out of range.")

def update_task(task_index, new_task):
    """Update an existing task with a new description."""
    tasks = file_handler.read_tasks()
    try:
        old_task = tasks[task_index]
        tasks[task_index] = new_task
        file_handler.write_tasks(tasks)
        print(f"Task updated from '{old_task}' to '{new_task}'.")
    except IndexError:
        print("Error: Task number is out of range.")

def view_tasks():
    """Display all current tasks."""
    tasks = file_handler.read_tasks()
    if not tasks:
        print("No tasks found.")
    else:
        for idx, task in enumerate(tasks):
            print(f"{idx}: {task}")
