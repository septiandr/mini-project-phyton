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
    print("Format: HH:MM:SS")
    print("Example: 01:00:00")
    print("\n")
    time1 = input("Masukkan waktu pertama: ")
    time2 = input("Masukkan waktu kedua: ")
    time1 = time1.split(":")
    time2 = time2.split(":")
    time1 = [int(x) for x in time1]
    time2 = [int(x) for x in time2]
    time1 = time1[0] * 3600 + time1[1] * 60 + time1[2]
    time2 = time2[0] * 3600 + time2[1] * 60 + time2[2]
    result = time1 + time2
    result = str(result)
    result = result.split(":")
    result = [int(x) for x in result]
    result = result[0] * 3600 + result[1] * 60 + result[2]
    result = str(result)
    result = result.split(":")
    result = [int(x) for x in result]
    print(f"{time1} + {time2} = {result[0]}:{result[1]}:{result[2]}")
    print("\n")
    start()




start()