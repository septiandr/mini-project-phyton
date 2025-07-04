
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
    print("4. Exit")
    conditional_menu()



def conditional_menu():
    menu = input("Input Menu: ")
    if menu == "1":
        create_task()
    elif menu == "2":
        delete_task()
    elif menu == "3":
        list_task()
    elif menu == "4":
        return
    else:
        print("Menu Not Found")


def create_task():
    
    task_name = input("Input Task Name: ")

    if task_name in task:
        print("Task Already Exist")
        list_task()
        return
    else:
        task.append(task_name)
        print("Task Created")
        list_task()

def list_task():
    print("----- Task List -----")
    #get data length
    if len(task) == 0: 
        print("Task List is Empty")
        back_to_menu()
        return
    #get data with index start index from 1
    for i, item in enumerate(task, start=1):
        print(f"{i}. {item}")

    back_to_menu()

def delete_task():
    delete_task_number = input("Input Delete Task Number: ")
    index_data_task = int(delete_task_number) - 1
    if task[index_data_task] == None:
        print("Task Not Found")
        back_to_menu()
        return
    
    # delete data
    task.pop(index_data_task)
    print("Task Deleted")
    back_to_menu()

def back_to_menu():
    print("-------------------")
    back_menu = int(input("Press 0 to Back to Menu : "))
    if back_menu == 0 :
        show_menu()
    else:
        print("Menu Not Found")
        back_to_menu()

show_menu()