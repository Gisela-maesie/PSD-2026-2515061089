class StackKursi:
    def __init__(self, max_size=5):
        self.MAX = max_size
        self.st = [None] * self.MAX
        self.top_idx = -1
        
    def is_empty(self):
        return self.top_idx == -1
    
    def is_full(self):
        return self.top_idx == self.MAX - 1
 
    def push(self, warna_kursi):
        if self.is_full():
            print("Tumpukan kursi sudah terlalu tinggi! tidak bisa menerima kursi baru lagi")
            return
        self.top_idx += 1
        self.st[self.top_idx] = warna_kursi
        print(f"Kursi warna {warna_kursi} berhasil ditambahkan ke tumpukan.")
 
    def pop(self):
        if self.is_empty():
            print("Tumpukan kosong! tidak ada kursi yang bisa diambil")
            return
        kursi_diambil = self.st[self.top_idx]
        self.top_idx -= 1
        print(f"Kursi warna {kursi_diambil} diambil dari tumpukan.")

    def peek(self):
        if self.is_empty():
            print("Tidak ada kursi di tumpukan.")
            return
        print(f"Kursi yang ada di posisi paling atas adalah kursi berwarna {self.st[self.top_idx]}")
 
    def display(self):
        if self.is_empty():
            print("Tumpukan kursi kosong.")
            return
        print("\nKondisi tumpukan kursi (Atas ke Bawah): ", end="")
        for i in range(self.top_idx, -1, -1):
            print(self.st[i], end=" ")
        print()
 
def main():
    gudang_kursi = StackKursi()
    pilih = 0
    
    while pilih != 5:
        print("\n----- PROGRAM SIMULASI TUMPUKAN KURSI -----")
        print("1. Tumpuk kursi baru")
        print("2. Ambil kursi dari tumpukan")
        print("3. Lihat Kursi")
        print("4. Tampilkan Semua tumpukan kursi")
        print("5. Keluar\n")
        
        try:
            pilih = int(input("Pilih Menu (1-5): "))
        except ValueError:
            print("Input salah! Masukkan angka.")
            continue
            
        if pilih == 1:
            warna = input("\nMasukkan warna kursi: ")
            if not warna.isalpha():
                print("Input tidak valid! Warna kursi harus berupa huruf (bukan angka/simbol).")
            else:
                gudang_kursi.push(warna)
        elif pilih == 2:
            gudang_kursi.pop()
        elif pilih == 3:
            gudang_kursi.peek()
        elif pilih == 4:
            gudang_kursi.display()
        elif pilih == 5:
            print("Program selesai.")
        else:
            print("Pilihan menu tidak valid!")

if __name__ == "__main__":
    main()