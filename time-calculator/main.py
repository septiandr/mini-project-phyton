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





start()