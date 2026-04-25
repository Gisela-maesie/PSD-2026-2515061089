def menu():
    print("Wishlist Belanja")
    print("1. Tambah Barang")
    print("2. Tampilkan Semua Barang")
    print("3. Hapus Barang")
    print("4. Keluar")
    
    
def main():
    Wishlist = ["Sepatu Sneakers", "Tas Hermes", "Pashmina Viscose Hitam"]
    running = True
    while running:
        menu()
        try:
            choice = int(input("Pilihan: "))
        except ValueError:
            print("Masukkan angka yang valid!")
            continue
        if choice == 1:
            barang = input("Nama barang baru: ")
            Wishlist.append(barang)
            print(f"{barang} berhasil ditambahkan")
        elif choice == 2:
            print("Daftar Wishlist")
            if not Wishlist:
                print("Kosong")
            else:
                for i, item in enumerate(Wishlist, 1):
                    print(f"{i}. {item}")
        elif choice == 3:
            if not Wishlist:
                print("Tidak ada barang untuk di hapus")
                continue
            for i, item in enumerate(Wishlist, 1):
                print(f"{i}. {item}")
            try:
                nomor = int(input("Maukkan nomor barang yang sudah di beli: "))
                dihapus = Wishlist.pop(nomor - 1)
                print(f"{dihapus} sudah di beli dan di hapus dari list")
            except ValueError:
                print("Nomor tidak valid, masukkan nomor yang ada di daftar!")
            
        elif choice == 4:
            running = False
            print("Program selesai.")
            
            
            
if __name__ == "__main__":
 main()
