menu = {
    'makanan': {'nasi goreng': 15000, 'mie goreng': 10000, 'sate': 20000},
    'minuman': {'es teh': 3000, 'es jeruk': 40000, 'kopi': 5000}
}

pilihan_user = []

def print_menu(menu):
    print("===== DAFTAR MENU =====")  # Header menu
    for kategori, daftar_item in menu.items():  # Loop tiap kategori: 'makanan', 'minuman'
        print(f"\n📂 {kategori.capitalize()}:")  # Tampilkan nama kategori
        for i, (nama, harga) in enumerate(daftar_item.items(), start=1):  # Loop item dalam kategori
            print(f"  {i}. {nama} : Rp{harga:,}")  # Cetak nama dan harga

def input_menu(key, menu):
    while True:
        print(f"Masukkan Pilihan {key} Anda (masukkan dalam nomor):")
        makanan = int(input())
        index = makanan - 1
        listMakanan = list(menu.items())
        newMakanan = listMakanan[index]
        pilihan_user.append(newMakanan)

        if pilihan(key) == False:
            break


def pilihan(key):
    is_order = input(f'apakah anda ingin memesan {key} lagi? y/n: ')
    is_order = is_order.lower()
    if is_order == 'y':
        return True  # Lanjutkan loop input_menu
    else:
        print('terimakasih sudah memesan')
        return False  # Hentikan loop input_menu


def print_pilihan_user():
    print("===== PEMESANAN ANDA =====")
    for i, (key, value) in enumerate(pilihan_user, start=1):
        print(f"{i}. {key} : {value}")

print_menu(menu)
input_menu('Makanan', menu['makanan'])
input_menu('Minuman', menu['minuman'])
print_pilihan_user()
