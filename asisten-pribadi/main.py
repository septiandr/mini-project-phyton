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
        delete_note()
    elif choice == "4":
        show_note()
    elif choice == "5":
        calculator()
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
        new_note = input("Enter the new note: ")
        notes[int(choice)-1] = new_note + "\n"
        with open("notes.txt", "w") as f:
            f.writelines(notes)
        print("Note edited")
    else:
        print("Invalid choice")
    main()
def delete_note():
    with open("notes.txt", "r") as f:
        notes = f.readlines()
    for i, note in enumerate(notes):
        print(f"{i+1}. {note}")
    choice = input("Enter the number of the note you want to delete: ")
    if choice.isdigit() and int(choice) <= len(notes):
        del notes[int(choice)-1]
        with open("notes.txt", "w") as f:
            f.writelines(notes)
        print("Note deleted")
    else:
        print("Invalid choice")
    main()
def show_note():
    with open("notes.txt", "r") as f:
        notes = f.readlines()
    for i, note in enumerate(notes):
        print(f"{i+1}. {note}")
    main()
def calculator():
    print("\n====== Calculator ======\n")
    input = input("Enter your calculation: ")
    try:
        result = eval(input)
        print(f"Result: {result}")
    except:
        print("Invalid calculation")
    main()

main()