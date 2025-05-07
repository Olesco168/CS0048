def main():
    tasks = []
    print("To do list")

    while True:
        print("1.) Add Task")
        print("2.) Remove Task")
        print("3.) View Tasks")
        print("4.) Exit")

        choice = input("\nInput your Choice (1-4): ")

        try:
            if choice == '4':
                print("Exiting")
                break
            if choice not in ['1', '2', '3', '4']:
                print("Invalid Input")
                continue

            if choice == '1':
                task = input("Enter task: ")
                task.append(task)
            elif choice == '2':
                if not tasks:
                    print("No tasks to remove.")
                else:
                    print ("\nTasks:")
                    for i in enumerate(tasks, 1):
                        print(f"{i}. {task}")
                    
                    try:

            elif choice == '3':
                

        except ValueError:
            print("Invalid Input: Value Error")

if __name__ == "__main__":
    main()