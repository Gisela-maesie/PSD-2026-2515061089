__a. Judul Program:__  
Aplikasi Manajemen Wishlist Belanja

__b. Deskripsi singkat:__  
Program ini dirancang sebagai aplikasi sederhana namun efektif untuk membantu pengguna dalam mengelola daftar rencana belanja. Fungsi utama dari program ini adalah memberikan kemudahan bagi pengguna untuk mencatat barang-barang yang dibutuhkan, memantau kembali seluruh isi daftar secara berkala, hingga menghapus item tertentu yang telah dibeli. Dengan menggunakan aplikasi ini, proses perencanaan belanja menjadi lebih terorganisir, sehingga pengguna dapat memastikan tidak ada kebutuhan yang terlewatkan  


Aplikasi ini menggunakan struktur data list 1 dimensi, pemilihan penggunaan struktur data ini berdasarkan karakteristiknya yang sangat dinamis dan fleksibel dalam menangani perubahan jumlah data. Kapasitas penyimpanan dalam program ini akan secara otomatis menyesuaikan saat pengguna menambahkan ataupun menghapus sebuah item. Hal ini menjadikan pengelolaan data belanja jauh lebih efisien karena program tidak membatasi jumlah input pengguna sejak awal dijalankan  

__c. Source Code__  

<img width="1285" height="969" alt="Screenshot 2026-04-25 230249" src="https://github.com/user-attachments/assets/e6caea78-d6dd-4e49-bf18-844bd5a9113d" />
<img width="1289" height="749" alt="Screenshot 2026-04-25 230726" src="https://github.com/user-attachments/assets/f9dfcde6-a804-4f2f-8446-30c69fa168ba" />  



__def menu()__ : Mendefinisikan fungsi bernama menu (tanpa parameter) untuk menampilkan pilihan menu kepada pengguna  


__print("Wishlist Belanja")__ : Menampilkan judul program di layar  


__print("1. Tambahkan barang baru")__ : Menampilkan pilihan intruksi nomor 1 ke layar untuk menambah data  


__print("2. Tampilkan isi wishlist")__ : Menampilkan pilihan intruksi nomor 2 ke layar untuk melihat isi dari data wishlist yang ada  


__print("3. Hapus barang yang sudah dibeli")__ : Menampilkan pilihan intruksi nomor 3 ke layar untuk menghapus data yang sudah dibeli  


__print("4. Keluar")__ : Menampilkan pilihan intruksi nomor 4 ke layar untuk keluar atau menghentikan program  


__def main()__ : Mendefinisikan fungsi utama bernama main()  


__List_barang = []__ : Membuat variabel List_barang berupa list kosong untuk menampung semua nama barang yang dimasukkan nantinya  


__running = True__ : Inisialisasi variabel running dengan nilai true sebagai pengontrol perulangan  


__while running__ : Memulai perulangan while yang akan berjalan terus-menerus selama variabel running bernilai true  


__menu()__ : Memanggil fungsi menu() agar daftar pilihan muncul di layar setiap kali perulangan dimulai  


__try__ : Memulai blok untuk mencoba mengeksekusi kode input angka  


__choice = int(input("Pilihan:))__ : Meminta pengguna memasukkan pilihannya dalam bentuk integer (bilangan bulat) dan menyimpannya pada variabel choice  


__except ValueError__: Menangkap kesalahan dari pengguna jika pengguna memasukkan inputan sealin angka  


__print("Masukkan angka yang valid!")__ : Menampilkan pesan "Masukkan angka yang valid" ke layar jika pengguna memasukkan inputan selain angka  


__continue__ : Perintah untuk melewati sisa kode di bawahnya dan langsung kembali ke awal perulangan while  


__if choice == 1__ : Logika percabangan jika pengguna memilih menu nomor 1  


__barang = input("Nama barang baru: ")__ : Meminta pengguna untuk memasukkan nama barang yang nantinya akan disimpan pada variabel barang  


__if barang.isdigit()__ : Validasi logika untuk mengecek apakah input nama barang yang dimasukkan oleh pengguna berupa angka  


__print("Nama barang tidak boleh hanya angka saja")__ : Menampilkan pesan "Nama barang tidak boleh hanya angka saja" ke layar jika input nama barang yang dimasukkan oleh pengguna berupa angka saja  


__elif len(barang) <3__ : validasi logika untuk mengecek apakah panjang karakter nama barang kurang dari 3 huruf   


__print("Nama barang terlalu pendek, masukkan minimal 3 huruf")__ : Menampilkan pesan berikut jika pengguna memasukkan nama barang kurang dari 3 huruf  


__else__ : Dijalankan jika nama barang sudah memenuhi syarat (bukan angka dan panjang karakter lebih dari 2 huruf)  


__List_barang.append(barang)__ : Menambahkan data dari variabel barang ke dalam variabel Lis_barang  


__print(f"{barang} berhasil ditambahkan")__ : Menampilkan pesan berikut ke layar, sebagai informasi bahwa data dari variabel barang berhasil ditambahkan ke dalam variabel List_barang  


__elif choice == 2__ : Logika percabangan jika pengguna memilih menu nomor 2  


__print("Daftar wishlist barang anda:")__ : Menampilkan pesan "Daftar wishlist barang anda:" ke layar 


__if not List_barang__ : Mengecek apakah list di dalam variabel List_barang dalam keadaan kososng(belum ada barang)  


__print("Daftar wishlist masih kosong")__ : Menampilkan pesan "Daftar wishlist masih kosong" ke layar, jika belum ada barang di dalam variabel List_barang  


__else__ : Dijalankan jika variabel List_barang terdeteksi memiliki isi  


__for i, item in enumerate(List_barang, 1)__ : Melakukan perulangan untuk mengambil data barang dari variabel List_barang beserta nomor urutnya dimulai dari angka 1  


__print(f"{i}, {item}")__ : Menampilkan nomor urut dan nama barang ke layar secara berurutan atau terstruktur  


__elif choice == 3__ : Logika percabangan jika pengguna memilih menu nomor 3  


__if not List_barang__ : Validasi awal untuk memastikan apakah ada data di didalam variabel List _barang sebelum melakukan proses penghapusan  


__print("Tidak ada barang di wishlist yang bisa di hapus")__ : Menampilkan pesan "Tidak ada barang di wishlist yang bisa di hapus" ke layar sebagai informasi bahwa tidak ada barang di dalam variabel List_barang sehingga proses penghapusan tidak dapat dilakukan  


__continue__ : Melewati proses penghapusan dan kembali ke menu utama jika daftar pada variabel List_barang kosong  


__for i, item in enumerate(List_barang, 1)__ : Menampilkan daftar barang terlebih dahulu agar pengguna tau nama barang di nomor berapa yang ingin dia hapus  


__try__ : memulai blok khusus untuk input nomor barang yang ingin di hapus (di dalam menu nomor 3)  


__nomor = int(input("Masukkan nomor barang yang sudah dibeli:"))__ : Meminta pengguna untuk memasukkan nomor barang yang sudah ia beli dan ingin dia hapus, kemudian menyimpannya ke dalam variabel nomor  


__if 1 <= nomor <= len(List_barang)__ : Memastikan bahwa nomor yang dimasukkan oleh pengguna yang ingin dia hapus itu nomornya tidak lebih kecil dari 1 dan tidak lebih besar dari jumlah barang yang ada di variabel List_barang  


__dihapus = List_barang.pop(nomor - 1)__ : Menghapus nama barang yang ingin dihapus tadi berdasarkan posisi indeks(input dikurangi 1) dan disimpan ke dalam variabel dihapus  


__print(f"{dihapus} sudah dibeli dan dihapus dari wishlist")__ : Menampilkan pesan bahwa barang yang tersimpan di variabel dihapus tadi sudah dibeli dan dihapus dari wishlist ke layar  


__else__ : Dijalankan jika nomor yang dimasukkan oleh pengguna tadi tidak ada didalam daftar atau melebihi jumlah barang yang ada  


__print("Nomor tersebut tidak ada di dalam daftar wishlist anda")__ : Menampilkan pesan "Nomor tersebut tidak ada di dalam daftar wishlist anda" jika pengguna memasukkan nomor lebih dari jumlah barang yang ada di variabel List_barang  


__except ValueError__ : Menangkap kesalahan jika nomor barang yang dimasukkan oleh pengguna bukan berupa angka  


__print("Input salah, masukkan nomor(angka)")__ : Menampilkan pesan "Input salah, masukkan nomor (angka)" ke layar, jika pengguna nomor barang yang dimasukka oleh pengguna buka berupa angka  


__elif choice == 4__ : Logika percabangan jika pengguna memilih menu nomor 4  


__running = False__ : Mengubah nilai running menjadi false untuk memutus perulangan dan menghentikan program  


__print("Program selesai")__ : Menampilkan pesan "Program seselsai" ke layar jika pengguna memilih menu no 4  


__else__ : Logika jika pengguna memasukkan angka selain 1,2,3 atau 4  


__print("Pilihan tidak tersedia")__ : Menampilkan pesan "Pilihan tidak tersedia" ke layar jika pengguna memasukkan pilihan selain nomor 1,2,3, dan 4 yang ada di menu  


__if __name__ == "__main__"__ : Memastikan fungsi main() hanya dijalankan saat file ini dieksekusi secara langsung  


__main()__ : Perintah terakhir untuk mengeksekusi fungsi utama program  


__d. Output Program__  


<img width="1096" height="1034" alt="Screenshot 2026-04-26 153653" src="https://github.com/user-attachments/assets/1914ab50-82f7-464c-9508-459baff5c37c" />
<img width="1094" height="994" alt="Screenshot 2026-04-26 153738" src="https://github.com/user-attachments/assets/a46abe57-afc2-4bd8-85cb-2f31fbeda4a0" />
<img width="1093" height="996" alt="Screenshot 2026-04-26 153811" src="https://github.com/user-attachments/assets/9580eef5-9b69-4d2f-b2ad-87197255201f" />
<img width="1099" height="271" alt="Screenshot 2026-04-26 153847" src="https://github.com/user-attachments/assets/fcd54918-562f-41b8-b08e-109fab2ee6e9" />  


__-Menampilkan menu utama__  


Setiap kali perulangan dimulai program akan memanggil fungsi menu(), yang akan menampilkan pesan:  


Wishlist Belanja   


1. Tambahkan barang baru


2. Tampilkan isi wishlist


3. Hapus barang yang sudah dibeli


4. Selesai


ini adalah tampilan yang berasal dari fungsi def menu(). program yang sudah berjalan setelah menampilkan isi dari def menu() maka akan langsung menampilkan pesan "Pilihan:", disini pengguna diminta untuk memasukkan nomor dari fungsi def menu() yang ingin dia jalankan  


Jika pada saat memasukkan nomor pada pesan "Pilihan:" tadi pengguna memasukkan pilihan selain angka maka program akan menjalankan except ValueError dan menampilkan pesan "Masukkan angka yang valid!". Dan apabila saat memasukkan nomor pada pesan "Pilihan:" tadi pengguna memasukkan angka yang tidak ada di menu misalkan angka 5 maka program akan menjalankan bagian else dan menampilkan pesan "Pilihan tidak tersedia"   


__-Proses tambah barang (pilihan 1)__  


Ketika pengguna memilih pilihan 1 maka program akan masuk ke logika penambahan barang. Selanjutnya program akan menampilkan pesan "Nama barang baru:" disini pengguna diminta untuk memasukkan nama barang yang ingin ia tambahkan ke dalam daftar wishlist belanja  


kemudian program akan melakukan proses validasi, jika pengguna memasukkan angka pada bagian ini maka program akan menampilkan pesan "Nama barang tidak boleh hanya angka saja", ataupun jika pada bagian ini pengguna memasukkan nama barang tetapi hurufnya lebih kecil dari 3 huruf maka program akan menampilkan pesan "Nama barang terlalu pendek, masukkan minimal 3 huruf", tetapi apabila pada bagian ini pengguna memasukkan nama barang dengan benar yaitu bukan berupa angka saja ataupun panjang hurufnya lebih dari 2 huruf maka program akan menjalankan List_barang.append(barang) yang artinya program menambahkan nama barang yang dimasukkan oleh pengguna tadi ke dalam List barang, dan akan menampilkan pesan "(barang yang dimasukkan tadi misalnya buku) berhasil ditambahkan"  


__-Menampilkan isi wishlist (pilihan 2)__  


ketika pengguna memilih pilihan 2 maka program akan mengecek isi list, jika list masih kosong maka program akan menampilkan pesan "Daftar wishlist masih kosong", tetapi jika list terisi maka program akan melakukan perulangan dan menampilkan isi list dengan nomor urut yang dimulai dari nomor 1  


__-Menghapus barang (pilihan 3)__  


Ketika pengguna memilih pilihan 3 maka program akan menampilkan daftar barang yang ada terlebih dahulu kemudian meminta pengguna untuk memasukkan nomor barang yang ingin dia hapus sesuai dengan nomor barang yang ada ditampilan daftar barang, jika pengguna memilih pilihan nomor 3 tetapi belum ada barang yang ditambahkan atau list masih dalam keadaan kosong maka program akan menampilkan pesan "Tidak ada barang di wishlist yang bisa dihapus", tetapi jika sebelumnya pengguna sudah memasukkan barang dalam list atau list sudah terisi maka misal pengguna memasukkan nomor 1 pada pilihan nomor barang yang ingin di hapus maka program akan menjalankan List_barang.pop(nomor - 1) yang artinya program menghapus nama barang pada nomor itu dari daftar list barang dan menampilkan pesan "(barang yang ingin dihapus misalnya baju) sudah dibeli dan dihapus dari wishlist", tetapi jika pengguna memasukkan nomor yang tidak ada di daftar maka program akan menampilkan pesan "Nomor tersebut tidak ada di dalam daftar wishlist anda"  


__-Keluar dari program (pilihan 4)__  


Ketika pengguna memilih pilihan 4 maka program mengubah status pada running menjadi false yang artinya perulangan berhenti dan program telah selesai 
















