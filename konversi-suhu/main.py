def menu():
    print("\n------------ Konversi Suhu ------------\n")
    print("1. Celcius ke Fahrenheit")
    print("2. Celcius ke Kelvin")
    print("3. Fahrenheit ke Celcius")
    print("4. Fahrenheit ke Kelvin")
    print("5. Kelvin ke Celcius")
    print("6. Kelvin ke Fahrenheit")
    print("7. Keluar\n")

    menu = input("Pilih Konversi (number): ")
    conditional_menu(menu)

def conditional_menu(menu):
    if menu == "1":
        celcius_ke_fahrenheit()
    elif menu == "2":
        celcius_ke_kelvin()
    elif menu == "3":
        fahrenheit_ke_celcius()
    elif menu == "4":
        fahrenheit_ke_kelvin()
    elif menu == "5":
        kelvin_ke_celcius()
    elif menu == "6":
        kelvin_ke_fahrenheit()
    elif menu == "7":
        exit()
    else:
        print("Pilihan tidak tersedia")
        menu()
        conditional_menu(input("Pilih Konversi (number): "))


menu()