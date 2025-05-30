def kategori_bmi(bmi):
    if bmi < 18.5:
        return "Kurus"
    elif bmi < 25:
        return "Ideal"
    elif bmi < 30:
        return "Kegemukan"
    else:
        return "Obesitas"

def calculator_bmi():
    print("===== BMI CALCULATOR ====")
    berat = float(input("Masukkan berat badan (kg): "))
    tinggi = float(input("Masukkan tinggi badan (cm): "))

    tinggi = tinggi / 100  # ubah cm ke meter
    bmi = berat / (tinggi ** 2)
    result = kategori_bmi(bmi)

    print(f"\nBMI Anda: {bmi:.2f}")
    print(f"Kategori: {result}")
    calculator_bmi()

# Jalankan program
calculator_bmi()
