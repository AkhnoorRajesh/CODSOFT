import json
import os

class TodoList:
    def __init__(self, filename='todos.json'):
        self.filename = filename
        self.todos = []
        self.load_todos()

    def load_todos(self):
        """Load todos from the JSON file."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                self.todos = json.load(file)

    def save_todos(self):
        """Save todos to the JSON file."""
        with open(self.filename, 'w') as file:
            json.dump(self.todos, file, indent=4)

    def add_task(self, task):
        """Add a new task to the todo list."""
        self.todos.append({'task': task, 'completed': False})
        self.save_todos()
        print(f'Task "{task}" added!')

    def update_task(self, index, task):
        """Update an existing task."""
        if 0 <= index < len(self.todos):
            self.todos[index]['task'] = task
            self.save_todos()
            print(f'Task updated to "{task}".')
        else:
            print("Task not found.")

    def complete_task(self, index):
        """Mark a task as completed."""
        if 0 <= index < len(self.todos):
            self.todos[index]['completed'] = True
            self.save_todos()
            print(f'Task "{self.todos[index]["task"]}" completed!')
        else:
            print("Task not found.")

    def delete_task(self, index):
        """Delete a task from the todo list."""
        if 0 <= index < len(self.todos):
            removed_task = self.todos.pop(index)
            self.save_todos()
            print(f'Task "{removed_task["task"]}" deleted!')
        else:
            print("Task not found.")

    def display_tasks(self):
        """Display all tasks in the todo list."""
        if not self.todos:
            print("No tasks found.")
        else:
            for index, todo in enumerate(self.todos):
                status = "✔️" if todo['completed'] else "❌"
                print(f"{index + 1}. [{status}] {todo['task']}")

def main():
    todo_list = TodoList()

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Update Task")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. View Tasks")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.display_tasks()
            index = int(input("Enter task number to update: ")) - 1
            task = input("Enter the updated task: ")
            todo_list.update_task(index, task)
        elif choice == '3':
            todo_list.display_tasks()
            index = int(input("Enter task number to complete: ")) - 1
            todo_list.complete_task(index)
        elif choice == '4':
            todo_list.display_tasks()
            index = int(input("Enter task number to delete: ")) - 1
            todo_list.delete_task(index)
        elif choice == '5':
            todo_list.display_tasks()
        elif choice == '6':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == '__main__':
    main()
