tasks=[] #listof tasks

def addTask():
    task=input("Enter your task: ")
    tasks.append(task)
    print("Task added")

def updateTask():
    listTask()
    try:
        taskupdate = int(input("Enter the task number you want to update: "))
        if 0 <= taskupdate < len(tasks):
            print("What would you like to do?")
            print("1. Replace the selected task")
            print("2. Add a new task (at the end)")
            option = input("Enter 1 or 2: ")

            if option == "1":
                newtask = input("Enter the new task description: ")
                curtask = tasks[taskupdate]
                confirm = input(f"Are you sure you want to replace '{curtask}' with '{newtask}'? (yes/no): ").strip().lower()
                if confirm == "yes":
                    tasks[taskupdate] = newtask
                    print("Task replaced successfully.")
                else:
                    print("Update canceled.")

            elif option == "2":
                newtask = input("Enter the new task to add: ")
                confirm = input(f"Are you sure you want to add '{newtask}' as a new task? (yes/no): ").strip().lower()
                if confirm == "yes":
                    tasks.append(newtask)
                    print("New task added at the end.")
                else:
                    print("Addition canceled.")
            else:
                print("Invalid option")
        else:
            print("Invalid task number")
    except ValueError:
        print("Please enter a valid number")
        
def listTask():
    if not tasks:
        print("there are no tasks ")
    else:
        print("current tasks ")
        for index, task in enumerate(tasks):
            print(f"Task {index}. {task}")
            
def deleteTask():
    listTask()
    try:
        taskdel=int(input("enter what you want to delete: "))
        if taskdel>=0 and taskdel<len(tasks):
            confirm=input("are you sure: ")
            if confirm=="yes":
                tasks.pop(taskdel)
                print("task deleted")
            else:
                print("deletion canceled")
        else:
            print("Invalid")
    except:
        print("invalid option")

if __name__=="__main__":
    print("welcome, Excited to plan your day!")
    while True:
        print("select one option")
        print("1. Add a task")
        print("2. Delete a task")
        print("3. Update a task")
        print("4. List tasks")
        print("5. Quit")

        choice=input("enter your choice: ")
        if choice=="1":
            addTask()
        
        elif choice=="2":
            deleteTask()

        elif choice=="3":
            updateTask()
        
        elif choice=="4":
            listTask()

        elif choice=="5":
            break

        else:
            print("invalid choice")
    print("see yaa")
        
        

        
    
