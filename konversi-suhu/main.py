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
    print("\n")

def conditional_menu(menu):
    if menu == "1":
        celcius_ke_fahrenheit()
    elif menu == "2":
        celcius_ke_kelvin()
    elif menu == "3":
        celcius_ke_fahrenheit(True)
    elif menu == "4":
        fahrenheit_ke_kelvin()
    elif menu == "5":
        celcius_ke_kelvin(True)
    elif menu == "6":
        fahrenheit_ke_kelvin(True)
    elif menu == "7":
        exit()
    else:
        print("Pilihan tidak tersedia")
        menu()
        conditional_menu(input("Pilih Konversi (number): "))

def celcius_ke_fahrenheit(revert = False):
    if revert:
        input_fahrenheit = input("Masukkan suhu dalam Fahrenheit: ")
        result = (float(input_fahrenheit) - 32) * 5/9
        print(f"{input_fahrenheit} Fahrenheit = {result} Celcius")
        print("\n")
        goto_menu()
        return  

    input_celcius = input("Masukkan suhu dalam Celcius: ")
    result = (float(input_celcius) * 9/5) +32
    print(f"{input_celcius} Celcius = {result} Fahrenheit")
    print("\n")
    goto_menu()

def celcius_ke_kelvin(revert = False):
    if revert:
        input_kelvin = input("Masukkan suhu dalam Kelvin: ")
        result = float(input_kelvin) - 273.15
        print(f"{input_kelvin} Kelvin = {result} Celcius")
        print("\n")
        goto_menu()
        return

    input_celcius = input("Masukkan suhu dalam Celcius: ")
    result = float(input_celcius) + 273.15
    print(f"{input_celcius} Celcius = {result} Kelvin")
    print("\n")
    goto_menu()

def fahrenheit_ke_kelvin(revert = False):
    if revert:
        input_kelvin = input("Masukkan suhu dalam Kelvin: ")
        result = (float(input_kelvin) - 273.15) * 9/5 + 32
        print(f"{input_kelvin} Kelvin = {result} Fahrenheit")
        print("\n")
        goto_menu()
        return

    input_fahrenheit = input("Masukkan suhu dalam Fahrenheit: ")
    result = (float(input_fahrenheit) - 32) * 5/9 + 273.15
    print(f"{input_fahrenheit} Fahrenheit = {result} Kelvin")
    print("\n")
    goto_menu()

def goto_menu():
    input("Tekan enter untuk kembali ke menu")
    menu()


menu()