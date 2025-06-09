import datetime

def chatbot():
    print("🤖 Hai! Aku adalah Mini ChatBot. Ketik 'keluar' untuk mengakhiri.\n")

    while True:
        user_input = input("Kamu: ").lower().strip()

        # Keluar
        if "keluar" in user_input:
            print("Bot: Terima kasih telah mengobrol. Sampai jumpa!")
            break

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

        # Ucapan terima kasih
        elif "terima kasih" in user_input or "makasih" in user_input:
            print("Bot: Sama-sama! 😊")

        # Perpisahan
        elif any(word in user_input for word in ["bye", "dadah", "sampai jumpa"]):
            print("Bot: Sampai jumpa lagi! 🌟")

        # Tidak dikenal
        else:
            print("Bot: Maaf, aku belum mengerti itu. Coba tanya hal lain ya!")

# Jalankan chatbot
chatbot()
