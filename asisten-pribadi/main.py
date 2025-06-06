from datetime import datetime

def main():
    print("\nHi Gav")
    print("What do you want to do?\n")
    time()

    print("1. Add Note")
    print("2. Show Notes")
    print("3. Calculator")
    print("4. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        add_note()
    elif choice == "2":
        show_notes()
    elif choice == "2":
        show_notes()
    elif choice == "4":
        exit()
    else:
        print("Invalid choice")
        main()

def time():
    time = datetime.now()
    print(f"{time.strftime('%A, %d %B %Y %H:%M:%S')}\n")
    
    

main()