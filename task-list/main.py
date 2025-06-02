print("Task List")
print("Program build by: gav")
print("-------------------")

print("Program built to handle create delete and show task list")

print("-------------------")
print("Menu")
print("1. Create Task")
print("2. Delete Task")
print("3. Show Task")


task = []
def create_task():
    
    task_name = input("Input Task Name: ")

    if task_name in task:
        print("Task Already Exist")
        return
    else:
        task.append(task_name)
        print("Task Created")

def list_task():
    for i, item in enumeration(task, start=1):
        print(f"{i}. {item}")


