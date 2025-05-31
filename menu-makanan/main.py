menu = {
    'makanan': {'nasi goreng': 15000, 'mie goreng': 10000, 'sate': 20000},
    'minuman': {'es teh': 3000, 'es jeruk': 40000, 'kopi': 5000}
}

def print_menu(menu):
    print("===== DAFTAR MENU =====")  # Header menu
    for kategori, daftar_item in menu.items():  # Loop tiap kategori: 'makanan', 'minuman'
        print(f"\n📂 {kategori.capitalize()}:")  # Tampilkan nama kategori
        for i, (nama, harga) in enumerate(daftar_item.items(), start=1):  # Loop item dalam kategori
            print(f"  {i}. {nama} : Rp{harga:,}")  # Cetak nama dan harga



print_menu(menu)