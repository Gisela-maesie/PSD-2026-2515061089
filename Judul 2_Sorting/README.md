__a. Judul Program__  
Sistem Digitalisasi Pengurutan Data Berat Badan Anak di Posyandu  

__b. Deskripsi Singkat__  
Program ini dibuat untuk membantu petugas posyandu dalam merapikan data berat badan anak secara digital. Fungsi utamanya adalah menyusun daftar berat badan anak dari yang paling ringan hingga yang paling berat secara otomatis. Deangan program ini, petugas tidak perlu lagi mengurutkan datasatu per stau secara manual, sehingga resiko salah catat dapat dikurangi dan pemantauan gizi anak jadi lebih praktis  

Untuk bagian pengurutan, program ini menggunakan cara kerja buble sort. Algoritma ini bekerja dengan cara membandingkan dua data yang bersebelahan, lalu menukarnya jika posisinya belum urut. Proses ini diulang terus-menerus sampai semua data benar-benar tersusun rapi. Cara ini dipilih karena langkah-langkahnya pasti dan teliti dalam memastikan setiap data berat badan anak berada dalam urutan yang tepat, sehingga hasil akhirnya akurat dan mudah dibaca oleh petugas. Program ini sangat cocok digunakan untuk pendataan rutin bulanan agar pertugas dapat langsung mengetahui siapa saja anak dengan berat badan terendah sampai tertinggi di wilayah tersebut.  

__c. Code Program__  
<img width="1276" height="946" alt="Screenshot 2026-05-02 115441" src="https://github.com/user-attachments/assets/06b2b38a-f5e4-456d-925d-7b1d8363c3c3" />
<img width="1286" height="214" alt="Screenshot 2026-05-02 114745" src="https://github.com/user-attachments/assets/df8b198a-d8f6-4adc-9119-ad400c5ee3af" />  

__def tukar(arr, i, j):__ Mendefinisikan fungsi bernama tukar untuk memindahkan dua elemen di dalam list berdasarkan indeksnya  
__temp = aff[i]:__ Membuat variabel sementara bernama temp untuk menyimpan nilai data pada posisi i agar tidak hilang saat ditimpa  
__arr[i] = arr[j]:__ Menimpa nilai pada posisi i dengan nilai yang diambil dari posisi j  
__arr[j] = temp:__ Mengisi posisi j dengan nilai yang sebelumnya disimpan di variabel temp sehingga kedua data bertukar posisi  
__def buble_sort(arr, n):__ Mendefinisikan fungsi bernama buble_sort untuk melakukan proses pengurutan data menggunakan algoritma gelembung  
__for i in range(n - 1):__ Melakukan perulangan luar untuk menentukan berapa banyak putaran pengecekan yang harus dilakukan pada list  
__for j in range(n - 1 - 1):__ Melakukan perulangan dalam untuk membandingkan setiap dua data yang letaknya besebelahan secara bertahap  
__if arr[j] > arr[j+  1]:__ Logika percabangan untuk mengecek apakah data di sebelah kiri nilainya lebih besar daripada data di sebelah kanannya  
__tukar(arr, j, j + 1):__ Memanggil fungsi tukar untuk memindahkan data yang lebih besar ke posisi sebelah kanan jika urutannya belum benar  
__def main():__ Mendefinisikan fungsi utama bernama main() sebagai pusat kendali jalannya seluruh intruksi program  
__print("\n---SISTEM DIGITALISASI PENGURUTAN DATA BERAT BADAN ANAK DI POSYANDU--
-"):__ Menampilkan pesan tersebut sebagai judul dari sistem ini  
__try:__ Memulai blok intruksi untuk menjalankan program  
__n = int(input("Masukkan jumlah anak : ")):__ Meminta pengguna untuk memasukkan jumlah anak dalambentuk integer(bilangan bulat) dan menyimpannya di variabel n  
__except ValueError:__ Menangkap kesalahan jika pengguna memasukkan inputan selain integer(bilangan bulat)  
__print"Input tidak valid!"):__ Menampilkan pesan "Inpust tidak valid!") ke layar jika pengguna memasukkan inputan selain integer(bilangan bulat)  
__return:__ Menghentikan fungsi main dan keluar dari program seketika karena input awal tidak memenuhi syarat yangmana harus berupa bilangan bulat  
__berat_badan = []:__ Membuat variabel berat_badan berup list kosong untuk menyimpan semua data yang akan dimasukkan nantinya  
__for i in range(n):__ Melakukan perulangan sebanyak n kali untuk meminta untuk meminta input data berat badan anak satu persatu  
__while True:__ Memulai perulangan while yang akan terus berjalan sampai pengguna memasukkan data berat badan yang benar  
__try:__ Memulai blok intruksi untuk mengeksekusi inputan angka berat badan dari user  
__nilai = float(input(f"Anak ke-(i+1):"):__ Meminta user untuk memasukkanangka berat badan anak bisa berupa bilangan desimal dan menyimpannya ke dalam variabel nilai  
__berat_badan.append(nilai):__ Menambahkan data angka dari variabel nilai ke dalam list variabel berat_badan  
__break:__ Menghentikan perulangan while dan lanjut ke anak berikutnya karena data sudah berhasil ditambahkan  
__except ValueError:__ Menangkap kesalahan jika pengguna atau user memasukkan inputan bukan berupa angka  
__print("Masukkan angka berat badan yang valid!"):__ Menampilkan pesan "Masukkan angka berat badan yang valid!" ke layar jika user memasukkan inputan selain angka  
__print(f"\nData berat badan awal : {berat_badan}"):__ Menampilkan isi daftar berat badan yang ada di variabel berat_badan sebelum dilakukan proses pengurutan  
__buble_sort(berat_badan, n):__ Memanggil fungsi buble_sort agar list berat_badan diproses dan diurutkan dari nilai terkecil hingga terbesar  
__print("\nUrutan berat badan setelah diurutkan dari yang paling ringan e paling berat:"):__ Menampilkan pesan tersebut ke layar  
__for i in range(n):__ Melakukan perulangan untuk mengambil setiap data berat badan yang sekarang sudah tersusun rapi di dalam list  
__print("f{berat_badan[i] kg", end=" "):__ Menggunakan f-string untuk memanggil isi data yang tersimpan di variabel berat_badan disertai satuan kg serta menggunakan end=" " agar data nya tertulis ke samping  
__print():__ Membuat baris kosong baru  
____if__name______=="_____main_____": Logika untuk memastikan fungsi utama program hanya berjalan jika file kode ini dieksekusi secara langsung  
__main():__ Perintah terakhir untuk mengeksekusi fungsi utama sehingga program mulai berjalan dari awal hingga akhir





