def is_prime(n):
    modulus = 0
    for i in range(10):
        iteration = i + 1
        if n % iteration == 0:
            modulus += 1

    if modulus == 2:
        return n


def find_prime_number():
    min_number = int(input("Masukkan angka minimal: "))
    maks_number = int(input("Masukkan angka maksimal: "))
    for i in range(min_number, maks_number):
        number = i + 1
        if(number > 1):
            is_prime(number)




find_prime_number()