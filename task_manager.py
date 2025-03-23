import task_operations

def display_menu():
    """Display the main menu options."""
    print("\nTask Manager")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Update Task")
    print("4. View Tasks")
    print("5. Exit")

def main():
    """Main loop for the CLI."""
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            task = input("Enter the task: ")
            task_operations.add_task(task)
        elif choice == '2':
            try:
                task_index = int(input("Enter the task number to remove: "))
                task_operations.remove_task(task_index)
            except ValueError:
                print("Invalid input. Please enter an integer.")
        elif choice == '3':
            try:
                task_index = int(input("Enter the task number to update: "))
                new_task = input("Enter the new task: ")
                task_operations.update_task(task_index, new_task)
            except ValueError:
                print("Invalid input. Please enter an integer.")
        elif choice == '4':
            task_operations.view_tasks()
        elif choice == '5':
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
