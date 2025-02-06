class TodoList:
    def __init__(self):
        self.todos = []

    def add_task(self, task):
        self.todos.append(task)
        print(f"Task added: {task}")

    def remove_task(self, task_number):
        if 0 <= task_number < len(self.todos):
            removed = self.todos.pop(task_number)
            print(f"Task removed: {removed}")
        else:
            print("Invalid task number.")

    def list_tasks(self):
        if not self.todos:
            print("No tasks in the list.")
        else:
            for i, task in enumerate(self.todos, 1):
                print(f"{i}. {task}")

def main():
    todo_list = TodoList()
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. List Tasks")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            try:
                task_number = int(input("Enter task number to remove: ")) - 1
                todo_list.remove_task(task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '3':
            todo_list.list_tasks()
        elif choice == '4':
            print("Exiting the application.")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()




class TodoList:
    def __init__(self):
        self.todos = []

    def add_task(self, task):
        self.todos.append(task)
        print(f"Task added: {task}")

    def remove_task(self, task_number):
        if 0 <= task_number < len(self.todos):
            removed = self.todos.pop(task_number)
            print(f"Task removed: {removed}")
        else:
            print("Invalid task number.")

    def list_tasks(self):
        if not self.todos:
            print("No tasks in the list.")
        else:
            for i, task in enumerate(self.todos, 1):
                print(f"{i}. {task}")

def main():
    todo_list = TodoList()
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. List Tasks")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            try:
                task_number = int(input("Enter task number to remove: ")) - 1
                todo_list.remove_task(task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '3':
            todo_list.list_tasks()
        elif choice == '4':
            print("Exiting the application.")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()



class TodoList:
    def __init__(self):
        self.todos = []

    def add_task(self, task):
        self.todos.append(task)
        print(f"Task added: {task}")

    def remove_task(self, task_number):
        if 0 <= task_number < len(self.todos):
            removed = self.todos.pop(task_number)
            print(f"Task removed: {removed}")
        else:
            print("Invalid task number.")

    def list_tasks(self):
        if not self.todos:
            print("No tasks in the list.")
        else:
            for i, task in enumerate(self.todos, 1):
                print(f"{i}. {task}")

def main():
    todo_list = TodoList()
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. List Tasks")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            try:
                task_number = int(input("Enter task number to remove: ")) - 1
                todo_list.remove_task(task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '3':
            todo_list.list_tasks()
        elif choice == '4':
            print("Exiting the application.")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
