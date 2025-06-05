from datetime import datetime
import re
# Remove unused import

pattern = r"^(?:[01]\d|2[0-3]):[0-5]\d:[0-5]\d$"

def start():
    now = datetime.now()
    
    print("\n====== Time Calculator ======\n")
    print(f"Date: {now.strftime('%d %B %Y')}")
    print(f"Time: {now.strftime('%H:%M:%S')}")
    print("\n=============================")
    print("\n")
    print("Menu:")
    print("1. Add Time")
    print("2. Subtract Time")
    print("3. Exit\n")
    menu = input("Pilih menu: ")
    if menu == "1":
        add_time()
    elif menu == "2":
        subtract_time()
    elif menu == "3":
        exit()
    else:
        print("Pilihan tidak tersedia")
        start()

def add_time():
    print("\n====== Add Time ======\n")
    startTime = input("Masukkan waktu awal (HH:MM:SS): ")
    hour, minute, second = map(int, startTime.split(":"))
    penambah = int(input("Masukkan waktu yang akan ditambahkan (dalam detik): "))

    # handle second
    if penambah % 60 == 0:
        minute += penambah / 60
    else:
        minute += penambah / 60
        second += penambah % 60

    #handle minute
    if minute % 60 == 0:
        hour += minute / 60
    else:
        hour += minute / 60
        minute = minute % 60
    
    print("\n=============================")
    print(f"\nHasil: {int(hour)}:{int(minute)}:{int(second)}")
    print("\n")
    if go_back():
        start()
    else:
        add_time()

def go_back():
    is_gobak = input("apakah anda ingin kembali ke menu? (y/n): ")
    if is_gobak == "y":
        return True
    elif is_gobak == "n":
        return False

start()