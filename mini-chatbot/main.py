import datetime

def chatbot():
    print("🤖 Hai! Aku adalah Mini ChatBot. Ketik 'keluar' untuk mengakhiri.\n")

    while True:
        user_input = input("Kamu: ").lower().strip()

        # Keluar
        if "keluar" in user_input:
            print("Bot: Terima kasih telah mengobrol. Sampai jumpa!")
            break

        # Menyapa
        elif any(word in user_input for word in ["halo", "hai", "selamat pagi", "selamat siang", "selamat sore"]):
            print("Bot: Hai juga! Senang bertemu denganmu 😊")

        # Tanya nama pengguna
        elif "nama saya" in user_input:
            nama = user_input.replace("nama saya", "").strip().capitalize()
            print(f"Bot: Hai {nama}, senang berkenalan denganmu!")

        elif "siapa nama saya" in user_input:
            if nama:
                print(f"Bot: Namamu {nama}, kan? 😉")
            else:
                print("Bot: Aku belum tahu namamu. Coba ketik 'nama saya [namamu]'.")

        # Salam
        elif any(word in user_input for word in ["halo", "hai", "selamat pagi", "selamat siang", "selamat sore"]):
            print("Bot: Hai juga! Senang bertemu denganmu 😊")

        # Nama bot
        elif "nama kamu" in user_input or "siapa kamu" in user_input:
            print("Bot: Aku adalah chatbot mini berbasis if-else. Namaku MiniBot.")

        # Cuaca
        elif "cuaca" in user_input:
            print("Bot: Maaf, aku belum bisa memberi info cuaca secara langsung. Tapi semoga cerah ya!")

        # Waktu
        elif "jam" in user_input or "waktu" in user_input:
            now = datetime.datetime.now()
            print(f"Bot: Sekarang jam {now.strftime('%H:%M')}.")
        
        # Motivasi
        elif "motivasi" in user_input or "semangat" in user_input:
            motivasi = [
                "Jangan menyerah, hari ini penuh peluang!",
                "Terus belajar, terus maju 💪",
                "Kesuksesan adalah hasil dari usaha yang tidak terlihat.",
                "Setiap hari adalah kesempatan baru!",
                "Kamu hebat, jangan ragukan dirimu sendiri!"
            ]
            print(f"Bot: {random.choice(motivasi)}")
        
        # Hitung umur
        elif "umur saya" in user_input or "lahir tahun" in user_input:
            try:
                tahun = int(''.join(filter(str.isdigit, user_input)))
                now = datetime.datetime.now()
                umur = now.year - tahun
                print(f"Bot: Kalau kamu lahir tahun {tahun}, umurmu sekitar {umur} tahun.")
            except:
                print("Bot: Maaf, aku tidak bisa mengerti tahun lahirmu.")

        # Ucapan terima kasih
        elif "terima kasih" in user_input or "makasih" in user_input:
            print("Bot: Sama-sama! 😊")

        # Perpisahan
        elif any(word in user_input for word in ["bye", "dadah", "sampai jumpa"]):
            print("Bot: Sampai jumpa lagi! 🌟")

        elif "tebak angka" in user_input:
            angka_bot = random.randint(1, 10)
            print("Bot: Aku sudah memilih angka dari 1 sampai 10. Coba tebak!")
            try:
                tebakan = int(input("Tebakanmu: "))
                if tebakan == angka_bot:
                    print("Bot: Wah! Kamu benar 🎉")
                else:
                    print(f"Bot: Salah, yang benar adalah {angka_bot}. Coba lagi lain kali!")
            except:
                print("Bot: Itu bukan angka yang valid 😅")

        # Tidak dikenal
        else:
            print("Bot: Maaf, aku belum mengerti itu. Coba tanya hal lain ya!")

# Jalankan chatbot
chatbot()
