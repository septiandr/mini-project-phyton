from pickle import NONE
import random


angka = NONE

def selectAngka():
    return random.randint(1, 100)

def inputAngka():
    while True:
        userAngka = int(input("Tebak Angka 1 - 100 : "))
        if 1 <= userAngka <= 100:
            return userAngka
        else:
            print('Angka tidak valid, solahkan coba lagi')

def cekAngka(angkaComputer):
    while True:
        userAngka = inputAngka()
        if angkaComputer == userAngka :
            print(f"Angka Benar, : {angkaComputer}")
            break
        elif angkaComputer > userAngka :
            print("Angka terlalu kecil")
        else:
            print("Angka terlalu besar")
    
angkaComputer = selectAngka()

cekAngka(angkaComputer)