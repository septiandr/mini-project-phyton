from datetime import datetime

def main():
    print("\nHi Gav")
    print("What do you want to do?\n")
    time()

    print("1. Add Note")
    print("2. Edit Note")
    print("3. Delete Note")
    print("4. Show Notes")
    print("5. Calculator")
    print("6. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        add_note()
    elif choice == "2":
        edit_note()
    elif choice == "3":
        calculator()
    elif choice == "4":
        exit()
    else:
        print("Invalid choice")
        main()

def time():
    time = datetime.now()
    print(f"{time.strftime('%A, %d %B %Y %H:%M:%S')}\n")
    
def add_note():
    note = input("Enter your note: ")
    with open("notes.txt", "a") as f:
        f.write(note + "\n")
    print("Note added")
    main()
    
def edit_note():
    with open("notes.txt", "r") as f:
        notes = f.readlines()
    for i, note in enumerate(notes):
        print(f"{i+1}. {note}")
    choice = input("Enter the number of the note you want to edit: ")
    if choice.isdigit() and int(choice) <= len(notes):


main()