import os

FILE_NAME = "tasks.txt"

def ensure_file_exists():
    """Ensure the tasks file exists; if not, create it."""
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'w') as f:
            pass  # Create an empty file

def read_tasks():
    """Read tasks from the file and return a list of tasks."""
    ensure_file_exists()
    tasks = []
    try:
        with open(FILE_NAME, 'r') as f:
            tasks = [line.strip() for line in f if line.strip()]
    except Exception as e:
        print(f"Error reading file: {e}")
    return tasks

def write_tasks(tasks):
    """Write the list of tasks to the file."""
    try:
        with open(FILE_NAME, 'w') as f:
            for task in tasks:
                f.write(task + "\n")
    except Exception as e:
        print(f"Error writing to file: {e}")
