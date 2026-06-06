__a. Judul Program__  
Sistem Manajemen Stok Barang di Toko Berbasis Hash Map Separate Chaining 

__b. Deskripsi Program__  
Program ini dikembangkan sebagai solusi untuk mempermudah pengelola toko dalam mengelola dan memantau stok barang secara real-time. Fungsi utama aplikasi ini adalah menyediakan alur kerja yang sistematis bagi pengguna untuk menambah barang baru, memperbarui informasi stok, menghapus data barang yang sudah tidak tersedia, serta melakukan pengecekan ketersediaan produk secara cepat. Melalui sistem ini, pengorganisasian data menjadi jauh lebih efisien dibandingkan cara manual, karena pengguna dapat mengetahui status inventaris, mencari detail barang berdasarkan ID, serta mengelola ketersediaan stok secara instan.

Dalam implementasinya, aplikasi ini menggunakan struktur data Hash Map dengan teknik Separate Chaining. Pilihan metode ini didasarkan pada efisiensi Hash Map dalam mengatur data secara otomatis; setiap ID barang yang masuk akan langsung dipetakan ke bucket yang tepat melalui fungsi hash. Jika terjadi collision (tabrakan data), sistem akan menyimpannya ke dalam linked list pada bucket tersebut, sehingga tidak memerlukan proses pencarian linear yang memakan waktu. Karakteristik ini membuat performa sistem sangat optimal, terutama untuk operasi pencarian, penambahan, maupun penghapusan data. Selain itu, program ini dilengkapi dengan manajemen bucket yang rapi untuk memastikan setiap barang dapat diakses dengan cepat dan akurat, meskipun jumlah stok yang dikelola terus bertambah.  

__c. Source Code__  
<img width="719" height="475" alt="Screenshot 2026-06-05 143100" src="https://github.com/user-attachments/assets/4f11fffe-4242-44b2-8e5c-052ba351af5f" />  
<img width="718" height="443" alt="Screenshot 2026-06-05 143136" src="https://github.com/user-attachments/assets/90b4cd05-ffab-4410-b0f4-5b1bec2d8f75" />  
<img width="722" height="452" alt="Screenshot 2026-06-05 143234" src="https://github.com/user-attachments/assets/32814b4a-2eb4-45fe-a88c-f4fb20f5a6fe" />  
<img width="720" height="378" alt="Screenshot 2026-06-05 143309" src="https://github.com/user-attachments/assets/ea8f8207-5ec0-418a-abb1-333fefb77b93" />  

- __class Node:__ Mendefinisikan sebuah kelas baru bernama Node sebagai struktur dasar penyimpanan data.
- __def __init__(self, key, value):__ Mendefinisikan fungsi konstruktor yang menerima tiga parameter: self, key, dan value.
- __self.key = key:__ Menyimpan nilai key yang diberikan pengguna ke dalam variabel self.key
- __self.value = value:__ Menyimpan nilai value yang diberikan pengguna ke dalam variabel self.value
- __self.next = None:__ Menetapkan nilai None ke dalam variabel self.next sebagai penunjuk awal yang kosong.
- __class HashMapSeparateChaining:__ Mendefinisikan sebuah kelas baru bernama HashMapSeparateChaining yang berfungsi sebagai kerangka utama untuk mengelola penyimpanan data dengan teknik hash map yang menangani tabrakan data (collision) menggunakan metode separate chaining
- __def __init__(self, size=10):__ : Mendefinisikan fungsi konstruktor dengan parameter self dan size yang memiliki nilai bawaan 10 yang digunakan untuk menentukan berapa banyak "rak" atau slot penyimpanan yang tersedia
- __self.SIZE = size:__ Menyimpan nilai dari parameter size ke dalam variabel self.SIZE.
- __self.table = [None] * self.SIZE:__ Membuat list self.table dengan panjang sebanyak SIZE dan mengisi setiap elemennya dengan nilai None.
- __def hash_function(self, key):__ Mendefinisikan fungsi hash dengan parameter self dan key untuk perhitungan terhadap key agar menghasilkan indeks yang benar.
- __return (key % self.SIZE + self.SIZE) % self.SIZE:__ Melakukan operasi modulus pada key dengan self.SIZE untuk menentukan posisi indeks yang valid.
- __def insert(self, key, value):__ Mendefinisikan fungsi insert untuk memasukkan atau memperbarui barang dengan parameter self, key, dan value.
- __index = self.hash_function(key):__ Memanggil fungsi hash_function dengan argumen key untuk menghitung di indeks berapa data tersebut harus ditempatkan atau dicari dan menyimpan hasilnya ke dalam variabel index.
- __current = self.table[index]:__ Mengambil node pertama yang ada di rak tersebut dan menyimpannya ke variabel current sebagai titik awal penelusuran
- __while current is not None:__ Melakukan perulangan selama variabel current tidak bernilai None.
- __if current.key == key:__ Logika percabangan untuk memeriksa apakah variabel key dari objek current sama dengan parameter key.
- __current.value = value:__ Jika key ditemukan, maka program akan memperbarui isi value dengan data baru yang diberikan.
- __return "update":__ Mengembalikan pesan "update" sebagai tanda bahwa data lama telah berhasil diperbarui dan fungsi selesai dijalankan.
- __current = current.next:__ Perintah untuk menggeser penunjuk ke node berikutnya jika key yang dicari belum ditemukan di node saat ini
- __new_node = Node(key, value):__ Jika perulangan selesai dan key tidak ditemukan, maka program membuat objek Node baru untuk menampung data yang akan dimasukkan
- __new_node.next = self.table[index]:__ Melakukan head insertion dengan menyambungkan pointer next dari node baru ke node lama yang sebelumnya menempati posisi paling depan di rak tersebut
- __self.table[index] = new_node:__ Menempatkan node baru tersebut menjadi node paling depan (head) di rak indeks tersebut
- __return "di tambahkan":__ Mengembalikan pesan "di tambahkan" sebagai tanda bahwa data baru berhasil dimasukkan ke dalam sistem
- __def search(self, key):__ Mendefinisikan fungsisearch untuk mencari data barang dengan parameter self dan key.
- __index = self.hash_function(key):__ Memanggil fungsi hash_function untuk menentukan di rak atau indeks mana barang tersebut disimpan
- __current = self.table[index]:__ Mengambil node pertama yang ada di rak tersebut dan menugaskannya ke variabel current sebagai titik awal untuk penelusuran
- __while current is not None:__ Melakukan perulangan selama current tidak kosong atau tidak None.
- __if current.key == key:__ Logika pengecekan untuk membandingkan apakah key (ID) pada node saat ini sama dengan key (ID) yang dicari
- __return current.value:__ Jika ditemukan kecocokan, fungsi langsung mengembalikan data value yang tersimpan di node tersebut
- __current = current.next:__ Perintah untuk menggeser penunjuk ke node berikutnya di dalam Linked List jika key belum ditemukan di node saat ini
- __return None:__ Mengembalikan nilai None jika perulangan selesai tetapi key (ID) yang dicari tidak ditemukan.
- __def remove_key(self, key):__ Mendefinisikan fungsi remove_key untuk menghapus data barang, dengan parameter key (ID barang) yang akan dicari dan dihapus
- __index = self.hash_function(key):__ Memanggil fungsi hash_function untuk menentukan di rak atau indeks berapa data tersebut berada dan menyimpan hasil pemanggilan hash_function(key) ke variabel index.
- __current = self.table[index]:__ Menginisialisasi pointer current ke node pertama di rak tersebut untuk memulai penelusuran
- __prev = None:__ Menetapkan nilai None ke variabel prev.
- __while current is not None:__ Melakukan perulangan selama current tidak None.
- __if current.key == key:__ Memeriksa apakah key milik objek current sama dengan parameter key.
- __if prev is None:__ Memeriksa apakah prev bernilai None.
- __self.table[index] = current.next:__ ika node tersebut adalah head, maka pointer pada rak tersebut diarahkan langsung ke node setelahnya
- __else:__ Menjalankan blok perintah jika kondisi if tidak terpenuhi.
- __prev.next = current.next:__ Mengubah pointer next dari node sebelumnya agar melompati node target dan langsung menunjuk ke node setelahnya
- __return True:__ Mengembalikan nilai True sebagai tanda bahwa proses penghapusan berhasil
- __prev = current:__ Menetapkan objek current ke variabel prev.
- __current = current.next:__ Menggeser pointer current ke node berikutnya untuk melanjutkan pencarian jika key belum ditemukan
- __return False:__ Mengembalikan nilai False jika perulangan selesai dan key tidak ditemukan
- __def display(self):__ Mendefinisikan fungsi display untuk memvisualisasikan seluruh data yang tersimpan di dalam hash table
- __empty = True:__ Menginisialisasi variabel empty dengan nilai True, yang berfungsi untuk memantau apakah tabel sama sekali tidak berisi data.
- __print("\n--- STATUS STOK BARANG DI TOKO ---"):__ Menampilkan pesan tersebut sebagai judul
- __for i in range(self.SIZE):__ Melakukan perulangan variabel i dari 0 hingga SIZE-1 atau hingga tabel terakhir.
- __if self.table[i] is not None:__ Logika pengecekan apakah self.table[i] tidak bernilai None
- __empty = False:__ ika ditemukan data di dalam rak, maka variabel empty diubah menjadi False
- __print(f"Rak [{i}]: ", end=""):__ Menampilkan nomor indeks rak ke layar, dengan end="" agar tampilan berikutnya tetap berada di baris yang sama
- __curr = self.table[i]:__ Mengambil node pertama dari Linked List yang berada di rak tersebut dan menyimpannya ke variabel curr
- __while curr:__ Melakukan perulangan hingga akhir selama curr bernilai True
- __print(f"ID:{curr.key}({curr.value})", end=" -> "):__ Menampilkan ID dan nama barang dari node saat ini, dengan tanda panah sebagai penanda hubungan antar node
- __curr = curr.next:__ Perintah untuk menggeser penunjuk ke node berikutnya
- __print("NULL"):__ Menampilkan pesan "NULL".
- __if empty:__ Melakukan pengecekan apakah variabel empty masih bernilai True.
- __print("Stok barang di gudang saat ini kosong."):__ Menampilkan pesan tersebut ke layar jika tidak ada data yang ditemukan di dalam tabel
- __def main():__ Mendefinisikan fungsi utama bernama main() yang berfungsi sebagai pusat kendali untuk menjalankan seluruh alur program dan interaksi dengan pengguna
- __toko = HashMapSeparateChaining(size=10):__ Membuat objek baru bernama toko dari kelas HashMapSeparateChaining dengan memberikan argumen size=10, yang berarti kita menyiapkan 10 slot atau "rak" penyimpanan di toko
- __while True:__ Membuat perulangan tak terbatas yang akan terus menampilkan menu pilihan kepada pengguna sampai pengguna memutuskan untuk keluar dari program
-  __print("\n--- MENU MANAJEMEN STOK BARANG DI TOKO ---"):__ Menampilkan pesan tersebut sebagai judul menu utama ke layar agar pengguna tau program apa yang sedang berjalan
-  __print("1. Tambah Barang"):__ Menampilkan pesan tersebut ke layar yaitu nomor 1 sebagai opsi untuk menambahkan data barang baru ke dalam sistem
-  __print("2. Cari Barang"):__ Menampilkan pesan tersebut yaitu nomor 2 sebagai opsi untuk mencari data barang
-  __print("3. Hapus Barang"):__ Menampilkan pesan tersebut yaitu nomor 3 sebagai opsi untuk menghapus data barang
-  __print("4. Lihat Daftar Barang"):__ Menampilkan pesan tersebut yaitu nomor 4 sebagai opsi untuk menampilkan visualisasi seluruh barang yang ada
-  __print("5. Keluar"):__ Menampilkan  pesan tersebut yaitu nomor 5 sebagai opsi bagi pengguna untuk menghentikan program
- __pilihan = input("Pilih menu (1-5): "):__ Pengguna diminta untuk memasukkan pilihan dari menu yang ada dan akan disimpan kedalam variabel pilihan
- __if pilihan == "1":__ Logika percabangan untuk memeriksa apakah pengguna memilih menu nomor 1, yang berarti ingin menambahkan atau memperbarui data barang di toko
- __try:__ Memulai blok try untuk melakukan pemantauan terhadap kode yang berisiko menyebabkan kesalahan
- __id_brg = int(input("Masukkan ID Barang : ")):__ Meminta pengguna untuk memasukkan ID barang dalam bentuk bilangan bulat kemudian menyimpannya kedalam variabel id_brg
- __nama = input("Masukkan Nama Barang: "):__ Meminta pengguna untuk memasukkan nama barang dan menyimpannya kedalam variabel nama dalam bentuk teks (string)
- __status = toko.insert(id_brg, nama):__ Memanggil fungsi insert dari objek toko dengan mengirimkan id_brg dan nama, kemudian menyimpan hasil kembaliannya (yaitu pesan "update" atau "di tambahkan") ke variabel status
- __print(f"Sukses: Barang berhasil {status}."):__ Menampilkan pesan tersebut ke layar, menggunakan f-string untuk membaca teks yang ada di dalam tanda kurung agar dibaca sebagai variabel yang memiliki data dan bukan sebagai teks biasa sehingga yang ditampilkan adalah isi dari variabel tersebut
- __except ValueError:__ Blok penanganan kesalahan yang akan dijalankan jika pengguna memasukkan inputan bukan berupa bilangan bulat
- __print("ID harus berupa angka!"):__ Menampilkan pesan tersebut ke layar jika pengguna memasukkan inputan tidak berupa bilangan bulat
- __elif pilihan == "2":__ Logika percabangan untuk memeriksa apakah pengguna memilih menu nomor 2, yang berarti pengguna ingin mencari informasi nama barang berdasarkan ID-nya
- __try:__ Memulai blok try untuk memantau potensi kesalahan input data dari pengguna
- __id_brg = int(input("Masukkan ID yang dicari: ")):__ Meminta pengguna untuk memasukkan ID barang yang ingin dicari dalam bentuk bilangan bulat dan menyimpannya ke dalam variabel id_barang
- __hasil = toko.search(id_brg):__ Memanggil fungsi search dari objek toko dengan mengirimkan id_brg, lalu menyimpan hasil pencariannya (berupa nama barang atau None) ke dalam variabel hasil
- __if hasil:__ Logika percabangan untuk memeriksa apakah variabel hasil memiliki data atau tidak none
- __print(f"Barang ditemukan: {hasil}"):__ Jika variabel hasil memiliki data,maka program akan menampilkan pesan tersebut ke layar, menggunakan f-string agar teks yang berada dalam tanda kurung dibaca sebagai variabel yang memiliki data bukan sebagai teks biasa sehingga yang ditampilkan adalah isinya
- __else:__ Kondisi alternatif yang akan dijalankan jika variabel hasil bernilai None
- __print("Barang dengan ID tersebut tidak ada didalam daftar."):__ Menampilkan pesan tersebut ke layar sebagai pesan pemberitahuan bahwa barang dengan ID yang dicari tidak tersedia atau tidak ditemukan didalam daftar
- __except ValueError:__ Blok penanganan kesalahan yang akan dijalankan jika pengguna memasukkan input selain angka saat diminta memasukkan ID yang ingin dicari
- __print("ID harus berupa angka!"):__ Menampilkan pesan tersebut kelayar jika pengguna memasukkan inputan selain bilangan bulat
- __elif pilihan == "3":__ Logika percabangan untuk memeriksa apakah pengguna memilih menu nomor 3, yang berarti pengguna ingin menghapus data barang berdasarkan ID-nya
- __try:__ Memulai blok try untuk menangani potensi kesalahan saat pengguna memberikan input data
- __id_brg = int(input("Masukkan ID yang akan dihapus: ")):__ Meminta pengguna memasukkan ID barang yang ingin dihapus dalam bentuk bilangan bulat dan menyimpannya ke dalam variabel id_barang
- __if toko.remove_key(id_brg):__ Memanggil fungsi remove_key milik objek toko dengan parameter id_brg. Fungsi ini akan mencoba menghapus data dan mengembalikan nilai True jika berhasil atau False jika gagal
- __print("Barang berhasil dihapus."):__ Jika remove_key mengembalikan True,maka pesan tersebut akan ditampilkan ke layar
- __else:__ Kondisi alternatif yang dijalankan jika fungsi remove_key mengembalikan nilai False
- __print("ID tidak ditemukan, tidak ada barang yang dihapus."):__ Menampilkan pesan kepada tersebut ke layar sebagai pesan informasi bahwa ID yang dimasukkan tidak ada di dalam daftar sehingga tidak ada data yang bisa dihapus
- __except ValueError:__ Blok penanganan kesalahan yang akan dijalankan jika pengguna memasukkan input selain angka bilangan bulat pada saat diminta mengisi ID
- __print("ID harus berupa angka!"):__ Menampilkan pesan tersebut ke layar jika pengguna memasukkan inputan selain angka bilangan bulat
- __elif pilihan == "4":__ Logika percabangan untuk memeriksa apakah pengguna memilih menu nomor 4, yang berarti pengguna ingin melihat daftar seluruh stok barang yang ada di toko
- __toko.display():__ Memanggil fungsi display() dari objek toko untuk menampilkan visualisasi isi hash table (termasuk Linked List di setiap rak) ke layar
- __elif pilihan == "5":__ Logika percabangan untuk memeriksa apakah pengguna memilih menu nomor 5, yang berarti pengguna ingin mengakhiri atau keluar dari program
- __print("Keluar dari program, program selesai."):__ Menampilkan pesan tersebut ke layar sebelum program ditutup
- __break:__ Perintah untuk menghentikan perulangan while True secara paksa, yang menyebabkan program keluar dari menu utama dan alur program berakhir
- __else:__ Kondisi terakhir yang akan dieksekusi jika pengguna memasukkan angka selain 1, 2, 3, 4, atau 5
- __print("Pilihan tidak valid, silakan masukkan pilihan angka 1-5."):__ Memberikan pesan tersebut ke layar sebagai peringatan bahwa input yang diberikan tidak sesuai dengan menu yang tersedia
- __if name == "main":__ Digunakan untuk memastikan bahwa rangkaian kode ini hanya akan berjalan jika file ini dieksekusi secara langsung
- __main():__ perintah untuk menjalankan fungsi utaman main() agar program dapat berjalan

__d. Output Program__  
<img width="725" height="498" alt="Screenshot 2026-06-06 144137" src="https://github.com/user-attachments/assets/6c57540e-6675-420b-a42a-edb9eb6b52cb" />  
<img width="728" height="491" alt="Screenshot 2026-06-06 144201" src="https://github.com/user-attachments/assets/f2ee2777-3767-4d10-9798-94aaa5d47ba5" />  
<img width="724" height="488" alt="Screenshot 2026-06-06 144223" src="https://github.com/user-attachments/assets/48743ed4-ba5d-49e3-a637-3bec7fc399a5" />  
<img width="732" height="167" alt="Screenshot 2026-06-06 144241" src="https://github.com/user-attachments/assets/c95e54df-2d10-4ec3-ac2d-022f14b14c78" />









