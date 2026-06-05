class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashMapSeparateChaining:
    def __init__(self, size=10):
        self.SIZE = size
        self.table = [None] * self.SIZE
    
    def hash_function(self, key):
        return (key % self.SIZE + self.SIZE) % self.SIZE
    
    def insert(self, key, value):
        index = self.hash_function(key)
        current = self.table[index]
        
        while current is not None:
            if current.key == key:
                current.value = value
                return "update"
            current = current.next    
        new_node = Node(key, value)
        new_node.next = self.table[index]
        self.table[index] = new_node
        return"di tambahkan"
    
    def search(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        while current is not None:
            if current.key == key:
                return current.value
            current = current.next
        return None
    
    def remove_key(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        prev = None
        while current is not None:
            if current.key == key:
                if prev is None:
                    self.table[index] = current.next
                else:
                    prev.next = current.next
                return True 
            prev = current
            current = current.next
        return False 
    
    def display(self):
        empty = True
        print("\n--- STATUS STOK BARANG DI TOKO ---")
        for i in range(self.SIZE):
            if self.table[i] is not None:
                empty = False
                print(f"Rak [{i}]: ", end="")
                curr = self.table[i]
                while curr:
                    print(f"ID:{curr.key}({curr.value})", end=" -> ")
                    curr = curr.next
                print("NULL")
        if empty:
            print("Stok barang di gudang saat ini kosong.")

def main():
    toko = HashMapSeparateChaining(size=10)
    while True:
        print("\n--- MENU MANAJEMEN STOK BARANG DI TOKO ---")
        print("1. Tambah Barang")
        print("2. Cari Barang")
        print("3. Hapus Barang")
        print("4. Lihat Daftar Barang")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ")
        
        if pilihan == "1":
            try:
                id_brg = int(input("Masukkan ID Barang : "))
                nama = input("Masukkan Nama Barang: ")
                status = toko.insert(id_brg, nama)
                print(f"Sukses: Barang berhasil {status}.")
            except ValueError:
                print("ID harus berupa angka!")
                
        elif pilihan == "2":
            try:
                id_brg = int(input("Masukkan ID yang dicari: "))
                hasil = toko.search(id_brg)
                if hasil:
                    print(f"Barang ditemukan: {hasil}")
                else:
                    print("Barang dengan ID tersebut tidak ada didalam daftar.")
            except ValueError:
                print("ID harus berupa angka!")
                
        elif pilihan == "3":
            try:
                id_brg = int(input("Masukkan ID yang akan dihapus: "))
                if toko.remove_key(id_brg):
                    print("Barang berhasil dihapus.")
                else:
                    print("ID tidak ditemukan, tidak ada barang yang dihapus.")
            except ValueError:
                print("ID harus berupa angka!")
                
        elif pilihan == "4":
            toko.display()
            
        elif pilihan == "5":
            print("Keluar dari program, program selesai.")
            break
            
        else:
            print("Pilihan tidak valid, silakan masukkan pilihan angka 1-5.")

if __name__ == "__main__":
    main()