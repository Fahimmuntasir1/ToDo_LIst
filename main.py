# ----Project of ToDo List----

# add a variable
Tasks = []

if __name__ == "main":
    # to run this app create a loop
    while True:
        print("\n")
        print("Select a option to do a operation >>")
        print("Select 1 to add a task")
        print("Select 2 to delete/remove a task")
        print("Select 3 to get all the tasks")
        print("Select 4 for EXIT")

        # get user choice
        choice = input("Input your selected option below:")
        if choice == 1:
            addTask()
        elif choice == 2:
            removeTask()
        elif choice == 3:
            getAllTasks()
        elif choice == 4:
            break
        else:
            print("Please enter a valid number around 1,2,3,4")

print("Application running......")
