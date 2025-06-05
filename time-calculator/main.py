from datetime import datetime
import pytz
# Remove unused import

def start():
    now = datetime.now()
    timezone = pytz.timezone("Asia/Jakarta")
    
    print("\n====== Time Calculator ======\n")
    print(f"Date: {now.strftime('%d %B %Y')}")
    print(f"Time: {now.strftime('%H:%M:%S')}")
    print(f"\nTimezone: {timezone}")
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
    penambah = int(input("Masukkan waktu yang akan ditambahkan (dalam menit): "))
    penambahToSecond = penambah / 60 

    newSecond = second + penambahToSecond

    if newSecond % 60 == 0:
        newSecond = 0
        minute = minute + (newSecond / 60)
    else:
        newSecond = newSecond % 60
        minute = minute + (newSecond / 60)





start()