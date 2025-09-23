def main():
    todos = []
    while True:
        print("\n1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            task = input("Enter task: ")
            todos.append(task)
        elif choice == "2":
            for i, task in enumerate(todos, 1):
                print(f"{i}. {task}")
            idx = int(input("Enter task number to remove: "))
            if 0 < idx <= len(todos):
                todos.pop(idx - 1)
        elif choice == "3":
            if not todos:
                print("No tasks available")
            else:
                for i, task in enumerate(todos, 1):
                    print(f"{i}. {task}")
        elif choice == "4":
            break

if __name__ == "__main__":
    main()
