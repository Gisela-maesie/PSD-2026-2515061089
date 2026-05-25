class Node:
    def __init__(self, key):
        self.key = key  
        self.left = None
        self.right = None

class Leaderboard:
    def __init__(self):
        self.root = None
    
    def insert_node(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self.insert_node(root.left, key)
        elif key > root.key:
            root.right = self.insert_node(root.right, key)
        return root
    
    def insert(self, key):
        self.root = self.insert_node(self.root, key)
 
    def find_min_node(self, root):
        current = root
        while current is not None and current.left is not None:
            current = current.left
        return current
 
    def delete_node(self, root, key):
        if root is None:
            return None
        if key < root.key:
            root.left = self.delete_node(root.left, key)
        elif key > root.key:
            root.right = self.delete_node(root.right, key)
        else:
            if root.left is None and root.right is None:
                return None
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                successor = self.find_min_node(root.right)
                root.key = successor.key
                root.right = self.delete_node(root.right, successor.key)
        return root
 
    def delete(self, key):
        self.root = self.delete_node(self.root, key)
    
    def search(self, root, key):
        if root is None: return False
        if root.key == key: return True
        if key < root.key: return self.search(root.left, key)
        return self.search(root.right, key)
    
    def get_min(self, root):
        if root is None: return None
        current = root
        while current.left is not None:
            current = current.left
        return current.key

    def get_max(self, root):
        if root is None: return None
        current = root
        while current.right is not None:
            current = current.right
        return current.key
    
    def level_order(self, root):
        if root is None:
            print("(Leaderboard kosong)")
            return
        queue = []
        queue.append(root)
        while len(queue) > 0:
            current = queue.pop(0)
            print(f"Skor: {current.key}", end=" | ")
            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)
        print()
 
    def find_successor(self, root, key):
        current = root
        successor = None
        while current is not None:
            if key < current.key:
                successor = current
                current = current.left
            elif key > current.key:
                current = current.right
            else:
                break
        if current is None: return None, False
        if current.right is not None:
            successor = self.find_min_node(current.right)
        if successor is None: return None, False
        return successor.key, True
 
    def find_predecessor(self, root, key):
        current = root
        predecessor = None
        while current is not None:
            if key > current.key:
                predecessor = current
                current = current.right
            elif key < current.key:
                current = current.left
            else:
                break
        if current is None: return None, False
        if current.left is not None:
            temp = current.left
            while temp.right is not None:
                temp = temp.right
            predecessor = temp
        if predecessor is None: return None, False
        return predecessor.key, True

def main():
    game = Leaderboard()
    pilih = 0
    while pilih != 7:
        print("\n=== LEADERBOARD SKOR PEMAIN ===")
        print("1. Tambah Skor")
        print("2. Hapus Skor (Pemain Keluar)")
        print("3. Lihat Ranking (Level-order)")
        print("4. Cek Skor Tertinggi/Terendah Sekitar")
        print("5. Cari Skor Setelahnya (Successor)")
        print("6. Cari Skor Sebelumnya (Predecessor)")
        print("7. Keluar")
        
        pilih = int(input("Pilih: "))
        if pilih == 1:
            x = int(input("Masukkan skor baru: "))
            game.insert(x)
        elif pilih == 2:
            try:
                x = int(input("Hapus skor pemain: "))
                if game.search(game.root, x):
                    game.delete(x)
                    print(f"Skor {x} berhasil dihapus.")
                else:
                    print(f"Pesan: Skor {x} tidak ditemukan di leaderboard.")
            except ValueError:
                print("Input tidak valid! Harap masukkan angka.")
        elif pilih == 3:
            game.level_order(game.root)
        elif pilih == 4:
            print(f"Skor Terendah: {game.get_min(game.root)}")
            print(f"Skor Tertinggi: {game.get_max(game.root)}")
        elif pilih == 5:
            x = int(input("Cari skor setelah (lebih besar dari) skor: "))
            ans, found = game.find_successor(game.root, x)
            print(f"Skor berikutnya: {ans}" if found else "Tidak ditemukan")
        elif pilih == 6:
            x = int(input("Cari skor sebelum (lebih kecil dari) skor: "))
            ans, found = game.find_predecessor(game.root, x)
            print(f"Skor sebelumnya: {ans}" if found else "Tidak ditemukan")
        elif pilih == 7:
            print("Program selesai.")
        else:
            print("Pilihan tidak ada di daftar menu")

if __name__ == "__main__":
    main()