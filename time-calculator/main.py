from datetime import datetime
import pytz

def start():
    now = datetime.now()
    timezone = pytz.timezone("Asia/Jakarta")
    
    print("\n====== Time Calculator ======\n")
    print(f"Date: {now.strftime('%d %B %Y')}")
    print(f"Time: {now.strftime('%H:%M:%S')}")
    print(f"\nTimezone: {timezone}")
    print("\n=============================")




start()