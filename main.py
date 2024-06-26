# ----Project of ToDo List----
print("Application is running......")

# add a variable to store al task
tasks = []


# create addTask function to add tasks
def addTask():
    task = input("Add your task : ")
    tasks.append(task)
    print(f"Your {task} task has been added successfully")


# create removeTask function to delete an existing task
def removeTask():
    # call getAllTasks to view tasks
    getAllTasks()

    try:
        removeTask = int(input("Enter the task index to remove: "))
        if removeTask >= 0 and removeTask < len(tasks):
            tasks.pop(removeTask)
            print(f"The task {removeTask} has been removed.")
        else:
            print(f"The task #{removeTask} was not found.")
    except:
        print("Invalid input. Please try with valid input")


# create getAllTasks function to view all the tasks
def getAllTasks():
    if not tasks:
        print("There are no tasks currently.")
    # to indexing tasks using built-in enumarate function
    enumerateTasks = enumerate(tasks)
    print(list(enumerateTasks))


while True:
    print("\n")
    print("Select a option to do a operation >>")
    print("Select 1 to Add a task")
    print("Select 2 to Delete/Remove a task")
    print("Select 3 to Get all the tasks")
    print("Select 4 for EXIT")
    # get user choice
    choice = input("Input your selected option : ")
    if choice == "1":
        print("Selected 1")
        addTask()
    elif choice == "2":
        print("Selected 2")
        removeTask()
    elif choice == "3":
        print("Selected 3")
        getAllTasks()
    elif choice == "4":
        break
    else:
        print("Please enter a valid number around 1,2,3,4")
        break

print("Thanks for using :) ")
