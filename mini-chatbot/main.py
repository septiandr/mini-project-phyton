def chatbot():
    print("🤖 Hai! Aku adalah Mini ChatBot. Ketik 'keluar' untuk mengakhiri.\n")

    while True:
        user_input = input("Kamu: ").lower()

        if "halo" in user_input or "hai" in user_input:
            print("Bot: Halo juga! Ada yang bisa aku bantu?")
        elif "nama kamu" in user_input or "siapa kamu" in user_input:
            print("Bot: Aku adalah chatbot sederhana buatan manusia.")
        elif "cuaca" in user_input:
            print("Bot: Maaf, aku tidak bisa memberikan info cuaca saat ini.")
        elif "terima kasih" in user_input:
            print("Bot: Sama-sama! 😊")
        elif "bye" in user_input or "dadah" in user_input:
            print("Bot: Sampai jumpa! Semoga harimu menyenangkan!")
        elif "keluar" in user_input:
            print("Bot: Terima kasih telah mengobrol. Sampai jumpa!")
            break
        else:
            print("Bot: Maaf, aku tidak mengerti. Bisa diulangi dengan kata lain?")

# Jalankan chatbot
chatbot()
