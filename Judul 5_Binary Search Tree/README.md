__a. Judul Program__  
Sistem Manajemen Papan Peringkat (Leaderboard) Skor Pemain Berbasis Struktur Data Binary Search Tree  

__b. Deskripsi Program__  
Program ini dikembangkan sebagai solusi untuk mempermudah penyelenggara kompetisi dalam mengelola dan memantau kumpulan skor secara real-time. Fungsi utama aplikasi ini adalah menyediakan alur kerja yang sistematis bagi pengguna untuk menambah skor baru, menghapus data yang sudah tidak diperlukan, serta melakukan pengecekan peringkat dengan cepat. Melalui sistem ini, pengorganisasian data menjadi jauh lebih efisien dibandingkan cara manual, karena pengguna dapat mengetahui skor tertinggi, skor terendah, serta posisi nilai relatif secara instan.  

Dalam implementasinya, aplikasi ini menggunakan struktur data Binary Search Tree (BST). Pilihan metode ini didasarkan pada efisiensi BST dalam mengatur data secara otomatis; setiap skor yang masuk akan langsung diposisikan pada cabang yang tepat (nilai lebih kecil di kiri, nilai lebih besar di kanan) tanpa memerlukan proses pengurutan ulang yang memakan waktu. Karakteristik ini membuat performa sistem sangat optimal, terutama untuk operasi pencarian, penambahan, maupun penghapusan data. Selain itu, program ini dilengkapi dengan fitur pencarian successor dan predecessor untuk mengetahui skor terdekat diatas dan skor terdekat dibawah  

__c. Source Code__  
<img width="1455" height="953" alt="Screenshot 2026-05-25 071626" src="https://github.com/user-attachments/assets/74c05536-adee-45fa-b069-9eb0d87dcdc3" />  
<img width="1458" height="899" alt="Screenshot 2026-05-25 071739" src="https://github.com/user-attachments/assets/8f315431-a966-40e9-a007-7196d59522c0" />  
<img width="1433" height="919" alt="Screenshot 2026-05-25 071819" src="https://github.com/user-attachments/assets/d27b321f-b488-4e09-9102-da3110207887" />  
<img width="1460" height="911" alt="Screenshot 2026-05-25 071905" src="https://github.com/user-attachments/assets/69495e00-86d2-4e95-a152-a73117fca71e" />  
<img width="1444" height="918" alt="Screenshot 2026-05-25 071940" src="https://github.com/user-attachments/assets/a5b93482-e49f-4824-ba39-db047bf51d4f" />  
<img width="1442" height="245" alt="Screenshot 2026-05-25 072006" src="https://github.com/user-attachments/assets/249877eb-acb3-4a9f-b852-885807f41658" />  

__- class Node:__ Mendefinisikan sebuah kelas baru bernama Node yang berfungsi sebagai struktur dasar untuk membuat setiap simpul (node) di dalam pohon data.  
__- def init(self, key):__ Mendefinisikan fungsi init dengan parameter key untuk menginisialisasi atribut awal saat objek node baru dibuat.  
__- self.key = key:__ Membuat variabel key untuk menyimpan nilai skor yang dimasukkan ke dalam node tersebut.  
__- self.left = None:__ Menginisialisasi pointer left dengan nilai None sebagai penanda bahwa awalnya tidak ada anak di cabang sebelah kiri.  
__- self.right = None:__ Menginisialisasi pointer right dengan nilai None sebagai penanda bahwa awalnya tidak ada anak di cabang sebelah kanan.  
__- class Leaderboard:__ Mendefinisikan sebuah kelas baru bernama Leaderboard yang berfungsi sebagai struktur utama untuk mengatur seluruh operasi pohon Binary Search Tree.  
__- def init(self):__ Mendefinisikan fungsi init untuk menginisialisasi properti awal saat objek Leaderboard dibuat.  
__- self.root = None:__ Membuat variabel root untuk menyimpan posisi akar pohon, diinisialisasi dengan None karena data masih kosong.  
__- def insert_node(self, root, key):__ Mendefinisikan fungsi insert_node dengan parameter root dan key untuk menyisipkan nilai skor ke posisi yang tepat secara rekursif.  
__- if root is None:__ Logika percabangan untuk memeriksa apakah posisi node saat ini kosong.  
__- return Node(key):__ Mengembalikan objek Node baru yang berisi skor tersebut jika posisi kosong ditemukan.  
__- if key < root.key:__ Logika percabangan untuk membandingkan jika skor baru lebih kecil dari skor pada node root saat ini.  
__- root.left = self.insert_node(root.left, key):__ Memanggil fungsi secara rekursif untuk menaruh skor di cabang sebelah kiri.  
__- elif key > root.key:__ Logika percabangan jika skor baru lebih besar dari skor pada node root saat ini.  
__- root.right = self.insert_node(root.right, key):__ Memanggil fungsi secara rekursif untuk menaruh skor di cabang sebelah kanan.  
__- return root:__ Mengembalikan node root setelah proses penyisipan selesai.  
__- def insert(self, key):__ Mendefinisikan fungsi pembungkus (wrapper) bernama insert untuk memulai proses penyisipan data dari akar.  
__- self.root = self.insert_node(self.root, key):__ Memanggil fungsi insert_node dimulai dari root dan memperbarui posisi root.  
__- def find_min_node(self, root):__ Mendefinisikan fungsi find_min_node untuk mencari node dengan nilai terkecil di dalam pohon.  
__- current = root:__ Membuat variabel bantu current untuk menelusuri pohon dimulai dari root.  
__- while current is not None and current.left is not None:__ Memulai perulangan selama masih ada cabang ke sebelah kiri.  
__- current = current.left:__ Menggeser penunjuk current ke node sebelah kiri secara terus menerus.  
__- return current:__ Mengembalikan node yang paling kiri atau yang memiliki nilai terkecil.  
__- def delete_node(self, root, key):__ Mendefinisikan fungsi delete_node untuk menghapus data skor tertentu dari dalam pohon.  
__- if root is None:__ Logika jika data yang dicari tidak ditemukan di dalam pohon.  
__- return None:__ Mengembalikan None sebagai penanda penghapusan tidak perlu dilakukan.  
__- if key < root.key:__ Logika untuk mencari data ke cabang kiri jika target skor lebih kecil.  
__- root.left = self.delete_node(root.left, key):__ Memanggil fungsi secara rekursif untuk menghapus di cabang kiri.  
__- elif key > root.key:__ Logika untuk mencari data ke cabang kanan jika target skor lebih besar.  
__- root.right = self.delete_node(root.right, key):__ Memanggil fungsi secara rekursif untuk menghapus di cabang kanan.  
__- else:__ Kondisi ketika target skor telah ditemukan.  
__- if root.left is None and root.right is None:__ Memeriksa jika node tersebut adalah leaf (tidak punya anak).  
__- return None:__ Menghapus node dengan mengembalikan None.  
__- elif root.left is None:__ Memeriksa jika node hanya punya anak di sebelah kanan.  
__- return root.right:__ Menggantikan posisi node tersebut dengan anak kanannya.  
__- elif root.right is None:__ Memeriksa jika node hanya punya anak di sebelah kiri.  
__- return root.left:__ Menggantikan posisi node tersebut dengan anak kirinya.  
__- else:__ Kondisi jika node memiliki dua anak.  
__- successor = self.find_min_node(root.right):__ Mencari nilai terkecil dari cabang sebelah kanan sebagai pengganti (successor).  
__- root.key = successor.key:__ Mengganti nilai node yang akan dihapus dengan nilai dari successor.  
__- root.right = self.delete_node(root.right, successor.key):__ Menghapus node successor asli dari cabang kanan.  
__- return root:__ Mengembalikan posisi node setelah proses penghapusan.  
__- def delete(self, key):__ Mendefinisikan fungsi pembungkus delete untuk menghapus skor.  
__- self.root = self.delete_node(self.root, key):__ Memulai proses penghapusan dari akar (root).  
__- def search(self, root, key):__ Mendefinisikan fungsi search untuk mencari apakah skor tertentu tersedia di dalam pohon.  
__- if root is None: return False:__ Jika pohon kosong atau skor tidak ditemukan, kembalikan nilai False.  
__- if root.key == key: return True:__ Jika nilai pada node saat ini sama dengan skor yang dicari, kembalikan True.  
__- if key < root.key: return self.search(root.left, key):__ Jika target lebih kecil, cari ke cabang kiri secara rekursif.  
__- return self.search(root.right, key):__ Jika target lebih besar, cari ke cabang kanan secara rekursif.  
__- def get_min(self, root):__ Mendefinisikan fungsi get_min untuk mengambil nilai skor terendah.  
__- if root is None:__ return None: Memeriksa jika pohon kosong, maka kembalikan None.  
__- current = root:__ Inisialisasi posisi pencarian di root.  
__- while current.left is not None: current = current.left:__ Melakukan penelusuran ke arah kiri paling ujung.  
__- return current.key:__ Mengembalikan nilai skor yang ditemukan di posisi paling kiri.  
__- def get_max(self, root):__ Mendefinisikan fungsi get_max untuk mengambil nilai skor tertinggi.  
__- if root is None: return None:__ Memeriksa jika pohon kosong, maka kembalikan None.  
__- current = root:__ Inisialisasi posisi pencarian di root.  
__- while current.right is not None: current = current.right:__ Melakukan penelusuran ke arah kanan paling ujung.  
__- return current.key:__ Mengembalikan nilai skor yang ditemukan di posisi paling kanan.  
__- def level_order(self, root):__ Mendefinisikan fungsi level_order untuk menampilkan data pohon per level menggunakan antrean (queue).  
__- if root is None:__ Memeriksa jika pohon dalam keadaan kosong.  
__- print("(Leaderboard kosong)"):__ Menampilkan pesan jika pohon kosong.  
__- return:__ Keluar dari fungsi jika pohon kosong.  
__- queue = []:__ Membuat list kosong sebagai antrean untuk menyimpan node yang akan dikunjungi.  
__- queue.append(root):__ Memasukkan node root ke dalam antrean.  
__- while len(queue) > 0:__ Melakukan perulangan selama antrean masih memiliki data.  
__- current = queue.pop(0):__ Mengambil node dari posisi terdepan antrean.  
__- print(f"Skor: {current.key}", end=" | "):__ Menampilkan skor dari node tersebut ke layar.  
__- if current.left is not None: queue.append(current.left):__ Memasukkan anak kiri ke antrean jika tersedia.  
__- if current.right is not None: queue.append(current.right):__ Memasukkan anak kanan ke antrean jika tersedia.  
__- print():__ Mencetak baris baru setelah seluruh level selesai ditampilkan.  
__- def find_successor(self, root, key):__ Mendefinisikan fungsi find_successor untuk mencari skor terdekat yang lebih besar dari target.  
__- current = root:__ Memulai pencarian dari root.  
__- successor = None:__ Inisialisasi variabel untuk menyimpan successor yang ditemukan.  
__- while current is not None:__ Melakukan perulangan selama masih ada node yang dicek.  
__- if key < current.key:__ Jika target lebih kecil, simpan node saat ini sebagai kandidat successor dan cari ke cabang kiri.  
__- successor = current:__ Menyimpan node saat ini sebagai kandidat successor.  
__- current = current.left:__ Berpindah ke cabang kiri.  
__- elif key > current.key:__ Jika target lebih besar, berpindah ke cabang kanan.  
__- current = current.right:__ Berpindah ke cabang kanan.  
__- else: break:__ Jika target ditemukan, hentikan pencarian.  
__- if current is None: return None, False:__ Jika target tidak ditemukan, kembalikan None dan False.  
__- if current.right is not None:__ Jika node target memiliki cabang kanan, successor adalah nilai terkecil di cabang kanan tersebut.  
__- successor = self.find_min_node(current.right):__ Mencari nilai terkecil di subtree kanan.  
__- if successor is None: return None, False:__ Jika tidak ada successor, kembalikan None dan False.  
__- return successor.key, True:__ Mengembalikan nilai successor dan status True.  
__- def find_predecessor(self, root, key):__ Mendefinisikan fungsi find_predecessor untuk mencari skor terdekat yang lebih kecil dari target.  
__- current = root:__ Memulai pencarian dari root.  
__- predecessor = None:__ Inisialisasi variabel untuk menyimpan predecessor yang ditemukan.  
__- while current is not None:__ Melakukan perulangan untuk menelusuri pohon.  
__- if key > current.key:__ Jika target lebih besar, simpan node saat ini sebagai kandidat predecessor dan cari ke cabang kanan.  
__- predecessor = current:__ Menyimpan node saat ini sebagai kandidat predecessor.  
__- current = current.right:__ Berpindah ke cabang kanan.  
__- elif key < current.key:__ Jika target lebih kecil, berpindah ke cabang kiri.  
__- current = current.left:__ Berpindah ke cabang kiri.  
__- else: break:__ Jika target ditemukan, hentikan pencarian.  
__- if current is None: return None, False:__ Jika target tidak ditemukan, kembalikan None dan False.  
__- if current.left is not None:__ Jika node target memiliki cabang kiri, predecessor adalah nilai terbesar di cabang kiri.  
__- temp = current.left:__ Menyimpan cabang kiri sebagai titik awal pencarian nilai terbesar.  
__- while temp.right is not None: temp = temp.right:__ Menelusuri ke kanan sampai menemukan nilai terbesar.  
__- predecessor = temp:__ Mengatur predecessor ke nilai terbesar di cabang kiri.  
__- if predecessor is None: return None, False:__ Jika tidak ada predecessor, kembalikan None dan False.  
__- return predecessor.key, True:__ Mengembalikan nilai predecessor dan status True.  
__- def main():__ Mendefinisikan fungsi utama bernama main() sebagai pusat berjalannya program.  
__- game = Leaderboard():__ Membuat objek bernama game dari kelas Leaderboard.  
__- pilih = 0:__ Menginisialisasi variabel pilih dengan nilai 0 untuk memulai perulangan menu.  
__- while pilih != 7:__ Membuat perulangan yang akan terus berjalan selama pilihan pengguna bukan 7 (Keluar).  
__- print("\n=== LEADERBOARD SKOR PEMAIN ==="):__ Menampilkan judul menu.  
__- print("1. Tambah Skor"):__ Menampilkan pilihan menu pertama.  
__- print("2. Hapus Skor (Pemain Keluar)"):__ Menampilkan pilihan menu kedua.  
__- print("3. Lihat Ranking (Level-order)"):__ Menampilkan pilihan menu ketiga.  
__- print("4. Cek Skor Tertinggi/Terendah Sekitar"):__ Menampilkan pilihan menu keempat.  
__- print("5. Cari Skor Setelahnya (Successor)"):__ Menampilkan pilihan menu kelima.  
__- print("6. Cari Skor Sebelumnya (Predecessor)"):__ Menampilkan pilihan menu keenam.  
__- print("7. Keluar"):__ Menampilkan pilihan menu ketujuh.  
__- pilih = int(input("Pilih: ")):__ Meminta input pilihan menu dari pengguna dalam bentuk integer.  
__- if pilih == 1:__ Logika jika user memilih nomor 1 untuk menambah skor.  
__- x = int(input("Masukkan skor baru: ")):__ Meminta input skor baru.  
__- game.insert(x):__ Memanggil fungsi insert untuk memasukkan skor ke dalam Leaderboard.  
__- elif pilih == 2:__ Logika jika user memilih nomor 2 untuk menghapus skor.  
__- try:__ Memulai blok try untuk menangani kesalahan input.  
__- x = int(input("Hapus skor pemain: ")):__ Meminta skor yang ingin dihapus.
__- if game.search(game.root, x):__ Memeriksa apakah skor tersebut ada di dalam Leaderboard.
__- game.delete(x):__ Memanggil fungsi delete untuk menghapus skor jika ditemukan.  
__- print(f"Skor {x} berhasil dihapus."):__ Menampilkan pesan keberhasilan penghapusan.  
__- else:__ Jika skor tidak ditemukan.  
__- print(f"Pesan: Skor {x} tidak ditemukan di leaderboard."):__ Menampilkan pesan skor tidak ditemukan.  
__- except ValueError:__ Menangkap kesalahan jika input bukan angka.  
__- print("Input tidak valid! Harap masukkan angka."):__ Menampilkan pesan error jika input bukan angka.  
__- elif pilih == 3:__ Logika jika user memilih nomor 3 untuk menampilkan ranking.
__- game.level_order(game.root):__ Memanggil fungsi level_order untuk menampilkan ranking.  
__- elif pilih == 4:__ Logika jika user memilih nomor 4 untuk cek skor tertinggi/terendah.  
__- print(f"Skor Terendah: {game.get_min(game.root)}"):__ Menampilkan skor terkecil.  
__- print(f"Skor Tertinggi: {game.get_max(game.root)}"):__ Menampilkan skor terbesar.  
__- elif pilih == 5:__ Logika jika user memilih nomor 5 untuk cari successor.  
__- x = int(input("Cari skor setelah (lebih besar dari) skor: ")):__ Meminta skor target.  
__- ans, found = game.find_successor(game.root, x):__ Memanggil fungsi find_successor untuk mencari skor berikutnya.  
__- print(f"Skor berikutnya: {ans}" if found else "Tidak ditemukan"):__ Menampilkan hasil successor.  
__- elif pilih == 6:__ Logika jika user memilih nomor 6 untuk cari predecessor.  
__- x = int(input("Cari skor sebelum (lebih kecil dari) skor: ")):__ Meminta skor target.  
__- ans, found = game.find_predecessor(game.root, x):__ Memanggil fungsi find_predecessor untuk mencari skor sebelumnya.  
__- print(f"Skor sebelumnya: {ans}" if found else "Tidak ditemukan"):__ Menampilkan hasil predecessor.  
__- elif pilih == 7:__ Logika jika user memilih nomor 7 untuk keluar.  
__- print("Program selesai."):__ Menampilkan pesan program selesai.  
__- if name == "main":__ Memastikan fungsi main() hanya dijalankan jika file dieksekusi secara langsung.  
__- main():__ Perintah untuk menjalankan fungsi main().








