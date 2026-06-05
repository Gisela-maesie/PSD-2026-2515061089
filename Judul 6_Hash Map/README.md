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
- __self.key = key:__ Menetapkan nilai dari parameter key ke dalam variabel self.key milik objek.
- __self.value = value:__ Menetapkan nilai dari parameter value ke dalam variabel self.value milik objek.
- __self.next = None:__ Menetapkan nilai None ke dalam variabel self.next sebagai penunjuk awal yang kosong.
- __class HashMapSeparateChaining:__ Mendefinisikan kelas utama untuk sistem penyimpanan berbasis hash.
- __def __init__(self, size=10):__ : Mendefinisikan fungsi konstruktor dengan parameter self dan size yang memiliki nilai bawaan 10.
- __self.SIZE = size:__ Menetapkan nilai dari parameter size ke dalam variabel self.SIZE.
- __self.table = [None] * self.SIZE:__ Membuat list self.table dengan panjang sebanyak SIZE dan mengisi setiap elemennya dengan None.
- __def hash_function(self, key):__ Mendefinisikan fungsi dengan parameter self dan key untuk perhitungan indeks.
- __return (key % self.SIZE + self.SIZE) % self.SIZE:__ Melakukan operasi modulus pada key dengan self.SIZE untuk menentukan posisi indeks yang valid.
- __def insert(self, key, value):__ Mendefinisikan fungsi dengan parameter self, key, dan value.
- __index = self.hash_function(key):__ Memanggil fungsi hash_function dengan argumen key dan menyimpan hasilnya di variabel index.
- __current = self.table[index]:__ Menugaskan nilai dari self.table[index] ke variabel current.
- __while current is not None:__ Melakukan perulangan selama variabel current tidak bernilai None.
- __if current.key == key:__ Memeriksa apakah variabel key dari objek current sama dengan parameter key.
- __current.value = value:__ Menetapkan nilai dari parameter value ke dalam variabel value milik objek current.
- __return "update":__ Mengembalikan string "update" sebagai hasil fungsi.
- __current = current.next:__ Menetapkan referensi dari variabel next milik objek current ke variabel current.
- __new_node = Node(key, value):__ Membuat objek baru dari kelas Node dengan parameter key dan value.
- __new_node.next = self.table[index]:__ Menetapkan referensi objek pada self.table[index] ke variabel next milik new_node.
- __self.table[index] = new_node:__ Menetapkan objek new_node ke dalam self.table[index].
- __return "di tambahkan":__ Mengembalikan string "di tambahkan" sebagai hasil fungsi.
- __def search(self, key):__ Mendefinisikan fungsi dengan parameter self dan key.
- __index = self.hash_function(key):__ Menyimpan hasil pemanggilan hash_function(key) ke variabel index.
- __current = self.table[index]:__ Menugaskan nilai self.table[index] ke variabel current.
- __while current is not None:__ Melakukan perulangan selama current tidak None.
- __if current.key == key:__ Memeriksa kesamaan key milik objek current dengan parameter key.
- __return current.value:__ Mengembalikan nilai value milik objek current.
- __current = current.next:__ Menetapkan referensi next dari objek current ke variabel current.
- __return None:__ Mengembalikan nilai None jika perulangan selesai.
- __def remove_key(self, key):__ Mendefinisikan fungsi dengan parameter self dan key.
- __index = self.hash_function(key):__ Menyimpan hasil pemanggilan hash_function(key) ke variabel index.
- __current = self.table[index]:__ Menugaskan nilai self.table[index] ke variabel current.
- __prev = None:__ Menetapkan nilai None ke variabel prev.
- __while current is not None:__ Melakukan perulangan selama current tidak None.
- __if current.key == key:__ Memeriksa kesamaan key milik objek current dengan parameter key.
- __if prev is None:__ Memeriksa apakah prev bernilai None.
- __self.table[index] = current.next:__ Menetapkan referensi next dari current ke self.table[index].
- __else:__ Menjalankan blok perintah jika kondisi if tidak terpenuhi.
- __prev.next = current.next:__ Menetapkan referensi next dari current ke variabel next milik objek prev.
- __return True:__ Mengembalikan nilai boolean True.
- __prev = current:__ Menetapkan objek current ke variabel prev.
- __current = current.next:__ Menetapkan referensi next dari objek current ke variabel current.
- __return False:__ Mengembalikan nilai boolean False setelah perulangan selesai.
- __def display(self):__ Mendefinisikan fungsi dengan parameter self.
- __empty = True:__ Menetapkan nilai boolean True ke variabel empty.
- __for i in range(self.SIZE):__ Melakukan perulangan variabel i dari 0 hingga SIZE-1.
- __if self.table[i] is not None:__ Memeriksa apakah self.table[i] tidak bernilai None.
- __empty = False:__ Menetapkan nilai boolean False ke variabel empty.
- __print(f"Rak [{i}]: ", end=""):__ Mencetak teks dengan format variabel i.
- __curr = self.table[i]:__ Menugaskan nilai self.table[i] ke variabel curr.
- __while curr:__ Melakukan perulangan selama curr bernilai benar.
- __print(f"ID:{curr.key}({curr.value})", end=" -> "):__ Mencetak teks dengan format key dan value dari objek curr.
- __curr = curr.next:__ Menetapkan referensi next dari objek curr ke variabel curr.
- __print("NULL"):__ Mencetak teks "NULL".
- __if empty:__ Memeriksa apakah variabel empty bernilai True.
- __print("Stok barang di gudang saat ini kosong."):__ Mencetak teks keterangan kosong.
- __def main():__ Mendefinisikan fungsi utama.
- __toko = HashMapSeparateChaining(size=10):__ Membuat objek dari kelas HashMapSeparateChaining dengan argumen 10.
- __while True:__ Membuat perulangan tanpa henti.
- __pilihan = input("Pilih menu (1-5): "):__ Menerima input dari pengguna dan menyimpannya ke variabel pilihan.





