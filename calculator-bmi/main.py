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
    berat = input("Masukkan berat badan (kg): ")
    tinggi = input("Masukkan tinggi badan (cm): ")

    bmi = berat / tinggi ** 2
    result = kategori_bmi(bmi)
    print(f"Berat badan: {result} kg")

    