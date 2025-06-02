
task = []
def show_menu():
    print("Task List")
    print("Program build by: gav")
    print("-------------------")

    print("Program built to handle create delete and show task list")
    print("-------------------")
    print("Menu")
    print("1. Create Task")
    print("2. Delete Task")
    print("3. Show Task")

    menu = input("Input Menu: ")
    if menu == "1":
        create_task()
    elif menu == "2":
        delete_task()
    elif menu == "3":
        list_task()
    else:
        print("Menu Not Found")

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

def delete_task():
    list_task()
    delete_task_number = input("Input Delete Task Number: ")
    index_data_task = int(delete_task_number) - 1
    task.pop(index_data_task)
    print("Task Deleted")

def back_to_menu():
    print("-------------------")
    back_menu = int(input("Press 0 to Back to Menu : "))
    if back_menu == 0 :
        show_menu()
    else:
        print("Menu Not Found")

show_menu()