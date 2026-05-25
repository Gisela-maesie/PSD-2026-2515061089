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
<img width="1457" height="299" alt="Screenshot 2026-05-25 085947" src="https://github.com/user-attachments/assets/bf7bf480-2c0f-4b89-a43c-3a0c60e809b5" />
  

- __class Node:__ Mendefinisikan sebuah kelas baru bernama Node yang berfungsi sebagai struktur dasar untuk membuat setiap simpul (node) di dalam pohon data.  
- __def init(self, key):__ Mendefinisikan fungsi init dengan parameter key untuk menginisialisasi atribut awal saat objek node baru dibuat.  
- __self.key = key:__ Membuat variabel key untuk menyimpan nilai skor yang dimasukkan ke dalam node tersebut.  
- __self.left = None:__ Menginisialisasi pointer left dengan nilai None sebagai penanda bahwa awalnya tidak ada anak di cabang sebelah kiri.  
- __self.right = None:__ Menginisialisasi pointer right dengan nilai None sebagai penanda bahwa awalnya tidak ada anak di cabang sebelah kanan.  
- __class Leaderboard:__ Mendefinisikan sebuah kelas baru bernama Leaderboard yang berfungsi sebagai struktur utama untuk mengatur seluruh operasi pohon Binary Search Tree.  
- __def init(self):__ Mendefinisikan fungsi init untuk menginisialisasi properti awal saat objek Leaderboard dibuat.  
- __self.root = None:__ Membuat variabel root untuk menyimpan posisi akar pohon, diinisialisasi dengan None karena data masih kosong.  
- __def insert_node(self, root, key):__ Mendefinisikan fungsi insert_node dengan parameter root dan key untuk menyisipkan nilai skor ke posisi yang tepat secara rekursif.  
- __if root is None:__ Logika percabangan untuk memeriksa apakah posisi node saat ini kosong.  
- __return Node(key):__ Mengembalikan objek Node baru yang berisi skor tersebut jika posisi kosong ditemukan.  
- __if key < root.key:__ Logika percabangan untuk membandingkan jika skor baru lebih kecil dari skor pada node root saat ini.  
- __root.left = self.insert_node(root.left, key):__ Memanggil fungsi secara rekursif untuk menaruh skor di cabang sebelah kiri.  
- __elif key > root.key:__ Logika percabangan jika skor baru lebih besar dari skor pada node root saat ini.  
- __root.right = self.insert_node(root.right, key):__ Memanggil fungsi secara rekursif untuk menaruh skor di cabang sebelah kanan.  
- __return root:__ Mengembalikan node root setelah proses penyisipan selesai.  
- __def insert(self, key):__ Mendefinisikan fungsi pembungkus (wrapper) bernama insert untuk memulai proses penyisipan data dari akar.  
- __self.root = self.insert_node(self.root, key):__ Memanggil fungsi insert_node dimulai dari root dan memperbarui posisi root.  
- __def find_min_node(self, root):__ Mendefinisikan fungsi find_min_node untuk mencari node dengan nilai terkecil di dalam pohon.  
- __current = root:__ Membuat variabel bantu current untuk menelusuri pohon dimulai dari root.  
- __while current is not None and current.left is not None:__ Memulai perulangan selama masih ada cabang ke sebelah kiri.  
- __current = current.left:__ Menggeser penunjuk current ke node sebelah kiri secara terus menerus.  
- __return current:__ Mengembalikan node yang paling kiri atau yang memiliki nilai terkecil.  
- __def delete_node(self, root, key):__ Mendefinisikan fungsi delete_node untuk menghapus data skor tertentu dari dalam pohon.  
- __if root is None:__ Logika jika data yang dicari tidak ditemukan di dalam pohon.  
- __return None:__ Mengembalikan None sebagai penanda penghapusan tidak perlu dilakukan.  
- __if key < root.key:__ Logika untuk mencari data ke cabang kiri jika target skor lebih kecil.  
- __root.left = self.delete_node(root.left, key):__ Memanggil fungsi secara rekursif untuk menghapus di cabang kiri.  
- __elif key > root.key:__ Logika untuk mencari data ke cabang kanan jika target skor lebih besar.  
- __root.right = self.delete_node(root.right, key):__ Memanggil fungsi secara rekursif untuk menghapus di cabang kanan.  
- __else:__ Kondisi ketika target skor telah ditemukan.  
- __if root.left is None and root.right is None:__ Memeriksa jika node tersebut adalah leaf (tidak punya anak).  
- __return None:__ Menghapus node dengan mengembalikan None.  
- __elif root.left is None:__ Memeriksa jika node hanya punya anak di sebelah kanan.  
- __return root.right:__ Menggantikan posisi node tersebut dengan anak kanannya.  
- __elif root.right is None:__ Memeriksa jika node hanya punya anak di sebelah kiri.  
- __return root.left:__ Menggantikan posisi node tersebut dengan anak kirinya.  
- __else:__ Kondisi jika node memiliki dua anak.  
- __successor = self.find_min_node(root.right):__ Mencari nilai terkecil dari cabang sebelah kanan sebagai pengganti (successor).  
- __root.key = successor.key:__ Mengganti nilai node yang akan dihapus dengan nilai dari successor.  
- __root.right = self.delete_node(root.right, successor.key):__ Menghapus node successor asli dari cabang kanan.  
- __return root:__ Mengembalikan posisi node setelah proses penghapusan.  
- __def delete(self, key):__ Mendefinisikan fungsi pembungkus delete untuk menghapus skor.  
- __self.root = self.delete_node(self.root, key):__ Memulai proses penghapusan dari akar (root).  
- __def search(self, root, key):__ Mendefinisikan fungsi search untuk mencari apakah skor tertentu tersedia di dalam pohon.  
- __if root is None: return False:__ Jika pohon kosong atau skor tidak ditemukan, kembalikan nilai False.  
- __if root.key == key: return True:__ Jika nilai pada node saat ini sama dengan skor yang dicari, kembalikan True.  
- __if key < root.key: return self.search(root.left, key):__ Jika target lebih kecil, cari ke cabang kiri secara rekursif.  
- __return self.search(root.right, key):__ Jika target lebih besar, cari ke cabang kanan secara rekursif.  
- __def get_min(self, root):__ Mendefinisikan fungsi get_min untuk mengambil nilai skor terendah.  
- __if root is None:__ return None: Memeriksa jika pohon kosong, maka kembalikan None.  
- __current = root:__ Inisialisasi posisi pencarian di root.  
- __while current.left is not None: current = current.left:__ Melakukan penelusuran ke arah kiri paling ujung.  
- __return current.key:__ Mengembalikan nilai skor yang ditemukan di posisi paling kiri.  
- __def get_max(self, root):__ Mendefinisikan fungsi get_max untuk mengambil nilai skor tertinggi.  
- __if root is None: return None:__ Memeriksa jika pohon kosong, maka kembalikan None.  
- __current = root:__ Inisialisasi posisi pencarian di root.  
- __while current.right is not None: current = current.right:__ Melakukan penelusuran ke arah kanan paling ujung.  
- __return current.key:__ Mengembalikan nilai skor yang ditemukan di posisi paling kanan.  
- __def level_order(self, root):__ Mendefinisikan fungsi level_order untuk menampilkan data pohon per level menggunakan antrean (queue).  
- __if root is None:__ Memeriksa jika pohon dalam keadaan kosong.  
- __print("(Leaderboard kosong)"):__ Menampilkan pesan jika pohon kosong.  
- __return:__ Keluar dari fungsi jika pohon kosong.  
- __queue = []:__ Membuat list kosong sebagai antrean untuk menyimpan node yang akan dikunjungi.  
- __queue.append(root):__ Memasukkan node root ke dalam antrean.  
- __while len(queue) > 0:__ Melakukan perulangan selama antrean masih memiliki data.  
- __current = queue.pop(0):__ Mengambil node dari posisi terdepan antrean.  
- __print(f"Skor: {current.key}", end=" | "):__ Menampilkan skor dari node tersebut ke layar.  
- __if current.left is not None: queue.append(current.left):__ Memasukkan anak kiri ke antrean jika tersedia.  
- __if current.right is not None: queue.append(current.right):__ Memasukkan anak kanan ke antrean jika tersedia.  
- __print():__ Mencetak baris baru setelah seluruh level selesai ditampilkan.  
- __def find_successor(self, root, key):__ Mendefinisikan fungsi find_successor untuk mencari skor terdekat yang lebih besar dari target.  
- __current = root:__ Memulai pencarian dari root.  
- __successor = None:__ Inisialisasi variabel untuk menyimpan successor yang ditemukan.  
- __while current is not None:__ Melakukan perulangan selama masih ada node yang dicek.  
- __if key < current.key:__ Jika target lebih kecil, simpan node saat ini sebagai kandidat successor dan cari ke cabang kiri.  
- __successor = current:__ Menyimpan node saat ini sebagai kandidat successor.  
- __current = current.left:__ Berpindah ke cabang kiri.  
- __elif key > current.key:__ Jika target lebih besar, berpindah ke cabang kanan.  
- __current = current.right:__ Berpindah ke cabang kanan.  
- __else: break:__ Jika target ditemukan, hentikan pencarian.  
- __if current is None: return None, False:__ Jika target tidak ditemukan, kembalikan None dan False.  
- __if current.right is not None:__ Jika node target memiliki cabang kanan, successor adalah nilai terkecil di cabang kanan tersebut.  
- __successor = self.find_min_node(current.right):__ Mencari nilai terkecil di subtree kanan.  
- __if successor is None: return None, False:__ Jika tidak ada successor, kembalikan None dan False.  
- __return successor.key, True:__ Mengembalikan nilai successor dan status True.  
- __def find_predecessor(self, root, key):__ Mendefinisikan fungsi find_predecessor untuk mencari skor terdekat yang lebih kecil dari target.  
- __current = root:__ Memulai pencarian dari root.  
- __predecessor = None:__ Inisialisasi variabel untuk menyimpan predecessor yang ditemukan.  
- __while current is not None:__ Melakukan perulangan untuk menelusuri pohon.  
- __if key > current.key:__ Jika target lebih besar, simpan node saat ini sebagai kandidat predecessor dan cari ke cabang kanan.  
- __predecessor = current:__ Menyimpan node saat ini sebagai kandidat predecessor.  
- __current = current.right:__ Berpindah ke cabang kanan.  
- __elif key < current.key:__ Jika target lebih kecil, berpindah ke cabang kiri.  
- __current = current.left:__ Berpindah ke cabang kiri.  
- __else: break:__ Jika target ditemukan, hentikan pencarian.  
- __if current is None: return None, False:__ Jika target tidak ditemukan, kembalikan None dan False.  
- __if current.left is not None:__ Jika node target memiliki cabang kiri, predecessor adalah nilai terbesar di cabang kiri.  
- __temp = current.left:__ Menyimpan cabang kiri sebagai titik awal pencarian nilai terbesar.  
- __while temp.right is not None: temp = temp.right:__ Menelusuri ke kanan sampai menemukan nilai terbesar.  
- __predecessor = temp:__ Mengatur predecessor ke nilai terbesar di cabang kiri.  
- __if predecessor is None: return None, False:__ Jika tidak ada predecessor, kembalikan None dan False.  
- __return predecessor.key, True:__ Mengembalikan nilai predecessor dan status True.  
- __def main():__ Mendefinisikan fungsi utama bernama main() sebagai pusat berjalannya program.  
- __game = Leaderboard():__ Membuat objek bernama game dari kelas Leaderboard.  
- __pilih = 0:__ Menginisialisasi variabel pilih dengan nilai 0 untuk memulai perulangan menu.  
- __while pilih != 7:__ Membuat perulangan yang akan terus berjalan selama pilihan pengguna bukan 7 (Keluar).  
- __print("\n=== LEADERBOARD SKOR PEMAIN ==="):__ Menampilkan judul menu.  
- __print("1. Tambah Skor"):__ Menampilkan pilihan menu pertama.  
- __print("2. Hapus Skor (Pemain Keluar)"):__ Menampilkan pilihan menu kedua.  
- __print("3. Lihat Ranking (Level-order)"):__ Menampilkan pilihan menu ketiga.  
- __print("4. Cek Skor Tertinggi/Terendah Sekitar"):__ Menampilkan pilihan menu keempat.  
- __print("5. Cari Skor Setelahnya (Successor)"):__ Menampilkan pilihan menu kelima.  
- __print("6. Cari Skor Sebelumnya (Predecessor)"):__ Menampilkan pilihan menu keenam.  
- __print("7. Keluar"):__ Menampilkan pilihan menu ketujuh.  
- __pilih = int(input("Pilih: ")):__ Meminta input pilihan menu dari pengguna dalam bentuk integer.  
- __if pilih == 1:__ Logika jika user memilih nomor 1 untuk menambah skor.  
- __x = int(input("Masukkan skor baru: ")):__ Meminta input skor baru.  
- __game.insert(x):__ Memanggil fungsi insert untuk memasukkan skor ke dalam Leaderboard.  
- __elif pilih == 2:__ Logika jika user memilih nomor 2 untuk menghapus skor.  
- __try:__ Memulai blok try untuk menangani kesalahan input.  
- __x = int(input("Hapus skor pemain: ")):__ Meminta skor yang ingin dihapus.
- __if game.search(game.root, x):__ Memeriksa apakah skor tersebut ada di dalam Leaderboard.
- __game.delete(x):__ Memanggil fungsi delete untuk menghapus skor jika ditemukan.  
- __print(f"Skor {x} berhasil dihapus."):__ Menampilkan pesan keberhasilan penghapusan.  
- __else:__ Jika skor tidak ditemukan.  
- __print(f"Pesan: Skor {x} tidak ditemukan di leaderboard."):__ Menampilkan pesan skor tidak ditemukan.  
- __except ValueError:__ Menangkap kesalahan jika input bukan angka.  
- __print("Input tidak valid! Harap masukkan angka."):__ Menampilkan pesan error jika input bukan angka.  
- __elif pilih == 3:__ Logika jika user memilih nomor 3 untuk menampilkan ranking.
- __game.level_order(game.root):__ Memanggil fungsi level_order untuk menampilkan ranking.  
- __elif pilih == 4:__ Logika jika user memilih nomor 4 untuk cek skor tertinggi/terendah.  
- __print(f"Skor Terendah: {game.get_min(game.root)}"):__ Menampilkan skor terkecil.  
- __print(f"Skor Tertinggi: {game.get_max(game.root)}"):__ Menampilkan skor terbesar.  
- __elif pilih == 5:__ Logika jika user memilih nomor 5 untuk cari successor.  
- __x = int(input("Cari skor setelah (lebih besar dari) skor: ")):__ Meminta skor target.  
- __ans, found = game.find_successor(game.root, x):__ Memanggil fungsi find_successor untuk mencari skor berikutnya.  
- __print(f"Skor berikutnya: {ans}" if found else "Tidak ditemukan"):__ Menampilkan hasil successor.  
- __elif pilih == 6:__ Logika jika user memilih nomor 6 untuk cari predecessor.  
- __x = int(input("Cari skor sebelum (lebih kecil dari) skor: ")):__ Meminta skor target.  
- __ans, found = game.find_predecessor(game.root, x):__ Memanggil fungsi find_predecessor untuk mencari skor sebelumnya.  
- __print(f"Skor sebelumnya: {ans}" if found else "Tidak ditemukan"):__ Menampilkan hasil predecessor.  
- __elif pilih == 7:__ Logika jika user memilih nomor 7 untuk keluar.  
- __print("Program selesai."):__ Menampilkan pesan program selesai.  
- __if name == "main":__ Memastikan fungsi main() hanya dijalankan jika file dieksekusi secara langsung.  
- __main():__ Perintah untuk menjalankan fungsi main().

__d. Output Program__  
<img width="1462" height="1006" alt="Screenshot 2026-05-25 090256" src="https://github.com/user-attachments/assets/bff01e34-014e-4a6a-9d13-7470b5205abf" />  
<img width="1494" height="992" alt="Screenshot 2026-05-25 090322" src="https://github.com/user-attachments/assets/99a85448-26ce-460c-b0d6-3a0437ba6487" />  
<img width="1502" height="974" alt="Screenshot 2026-05-25 090410" src="https://github.com/user-attachments/assets/7f9fa733-f02a-4599-a752-077e032291f7" />  
<img width="1499" height="621" alt="Screenshot 2026-05-25 090428" src="https://github.com/user-attachments/assets/7bd8b034-2dc5-4e6b-a49e-61f54606d7b5" />  

__Tampilan Menu utama dan Validasi Kesalahan Pilihan__  
Saat program pertama kali dijalankan, sistem akan masuk ke dalam fungsi main() dan menampilkan judul === LEADERBOARD SKOR PEMAIN ===. Di bawah judul, program akan menampilkan 7 daftar pilihan menu, yaitu: 1. Tambah Skor, 2. Hapus Skor, 3. Lihat Ranking, 4. Cek Skor Tertinggi/Terendah, 5. Cari Skor Setelahnya (Successor), 6. Cari Skor Sebelumnya (Predecessor), dan 7. Keluar. Setelah daftar menu muncul, program akan menampilkan prompt Pilih:  untuk meminta input angka dari pengguna. Jika pengguna memasukkan input selain angka, program akan mendeteksi kesalahan melalui blok except ValueError dan menampilkan pesan Input tidak valid! Harap masukkan angka.. Jika pengguna memasukkan angka bilangan bulat namun tidak ada dalam rentang 1-7, sistem akan masuk ke logika else paling bawah dan menampilkan pesan Pilihan tidak ada di daftar menu sebagai peringatan, lalu akan kembali menampilkan menu utama dari awal.  

__Proses Tambah Skor (Menu 1)__  
Apabila pengguna memilih menu 1, program akan menampilkan pesan Masukkan skor baru: . Di sini, pengguna diminta untuk memasukkan nilai skor dalam bentuk angka. Setelah angka dimasukkan, sistem akan menjalankan fungsi game.insert(x) yang secara otomatis menempatkan data tersebut ke dalam struktur Binary Search Tree sesuai dengan aturan BST, di mana nilai yang lebih kecil akan berada di cabang kiri dan nilai yang lebih besar di cabang kanan, menjaga data tetap terorganisir secara otomatis.  

__Proses Hapus Skor (Menu 2)__  
Jika pengguna memilih menu 2, program akan menampilkan pesan Hapus skor pemain:  untuk meminta skor yang ingin dihapus. Program kemudian menjalankan fungsi game.search(game.root, x) untuk memastikan apakah skor tersebut ada dalam sistem. Jika skor ditemukan, program akan menjalankan fungsi game.delete(x) dan memunculkan pesan Skor [angka] berhasil dihapus.. Namun, jika skor yang dicari tidak ada di dalam leaderboard, maka program akan membatalkan proses penghapusan dan menampilkan pesan Pesan: Skor [angka] tidak ditemukan di leaderboard.  

__Proses Lihat Ranking (Menu 3)__  
Ketika pengguna memilih pilihan 3, program akan menjalankan fungsi level_order() untuk menampilkan seluruh data skor yang ada dalam sistem secara terurut berdasarkan level pohonnya. Sistem akan memunculkan pesan Skor: [nilai] |  untuk setiap node yang ditemukan. Proses ini menggunakan antrean (queue) untuk memastikan data ditampilkan secara sistematis mulai dari akar (root) ke bawah. Jika saat menu ini dipilih sistem belum memiliki data skor sama sekali, maka program akan mendeteksinya dan menampilkan pesan (Leaderboard kosong).  

__Proses Cek Skor Tertinggi dan Terendah (Menu 4)__  
Apabila pengguna memilih menu 4, program akan menjalankan fungsi get_min() untuk mencari nilai terkecil dan get_max() untuk mencari nilai terbesar. Sistem akan menampilkan hasilnya ke layar melalui dua pesan: Skor Terendah: [nilai] dan Skor Tertinggi: [nilai]. Sistem melakukan ini dengan menelusuri cabang paling kiri dari root untuk mendapatkan nilai terendah, dan menelusuri cabang paling kanan dari root untuk mendapatkan nilai tertinggi.  

__Proses Cari Successor dan Predecessor (Menu 5 dan 6)__  
Jika pengguna memilih menu 5, program akan meminta input target skor dan menjalankan fungsi find_successor(). Program akan menampilkan Skor berikutnya: [nilai] jika ditemukan, atau Tidak ditemukan jika tidak ada skor yang lebih besar dari target. Begitu pula jika memilih menu 6, program akan menjalankan find_predecessor() dan menampilkan Skor sebelumnya: [nilai] jika ada skor yang lebih kecil dari target, atau Tidak ditemukan jika tidak ada. Keduanya membantu pengguna memahami posisi skor relatif terhadap nilai lain dalam leaderboard.  

__Proses Keluar Dari Program (Menu 7)__  
Jika pengguna memilih pilihan 7 pada daftar menu, maka program akan menampilkan pesan Program selesai. ke layar. Setelah pesan ini muncul, program akan otomatis berhenti karena perulangan while telah dihentikan, yang menandakan seluruh rangkaian operasional pada program leaderboard ini telah ditutup dengan aman.  

## Link Youtube:  
https://youtu.be/7bwpfgdWe8I
















