def menu():
    print("Wishlist Belanja")
    print("1. Tambahkan barang baru")
    print("2. Tampilkan semua barang")
    print("3. Hapus barang yang sudah di beli")
    print("4. Keluar")
    
    
def main():
    List_barang = []
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
            if barang.isdigit():
                print("Nama barang tidak boleh hanya angka saja")
            elif len(barang) < 3:
                print("Nama barang terlalu pendek, masukkan minimal 3 huruf")
            else:
                List_barang.append(barang)
                print(f"{barang} berhasil ditambahkan")
        elif choice == 2:
            print("Daftar wishlist barang: ")
            if not List_barang:
                print("Daftar wishlist masih kosong")
            else:
                for i, item in enumerate(List_barang, 1):
                    print(f"{i}. {item}")
        elif choice == 3:
            if not List_barang:
                print("Tidak ada barang yang bisa di hapus")
                continue
            for i, item in enumerate(List_barang, 1):
                print(f"{i}. {item}")
            try:
                nomor = int(input("Masukkan nomor barang yang sudah di beli: "))
                if 1 <= nomor <= len(List_barang):
                    dihapus = List_barang.pop(nomor - 1)
                    print(f"{dihapus} sudah di beli dan di hapus dari wishlist")
                else:
                    print("Nomor tersebut tidak ada di dalam daftar")
            except ValueError:
                print("Input salah, masukkan nomor (angka)") 
        elif choice == 4:
            running = False
            print("Program selesai.")
        else:
            print("Pilihan tidak tersedia")
            
            
            
if __name__ == "__main__":
    main()
