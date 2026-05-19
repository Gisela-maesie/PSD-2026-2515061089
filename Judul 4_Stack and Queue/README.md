__a. Judul Program__  
Sistem Manajemen Tumpukan Kursi Berbasis Struktur Data Stack Array

__b. Deskripsi Program__  
Porgram ini dirancang sebagai sistem sederhana namun efektif untuk membantu pengelola fasilitas atau kru lapangan dalam memantau inventaris tumpukan kursi di suatu tempat, misalnya seperti aula, gedung acara, atau tenda. Fungsi utama dari program ini adalah memberikan kemudahan bagi pengguna untuk mengelola proses keluar masuknya kursi secara teratur di suatu tempat. Dengan menggunakan sistem ini, proses penataan akan menjadi lebih terorganisir, sehingga pengguna dapat melihat urutan tumpukan kursi secara cepat tanpa harus mengeceknya secara manual satu persatu  

Aplikasi ini menggunakan metode Stack Array. Pemilihan metode ini karena karakteristiknya yang menggunakan prinsip LIFO (Last In First Out), yangmana sangat mencerminkan kondisi yang terjadi di dunia nyata. Kursi yang terakhir dimasukkan pasti akan menjadi kursi yang pertama kali diambil ketika kursi ingin digunakan, hal ini yang mengakibatkan mengapa penggunaan metode stack array sangat sesuai dengan keadaan seperti ini. 

__c. Source Code__  
<img width="635" height="476" alt="Screenshot 2026-05-18 212454" src="https://github.com/user-attachments/assets/6f41fc13-43dd-4c78-bb97-455c59a092e0" />
<img width="636" height="463" alt="Screenshot 2026-05-18 212541" src="https://github.com/user-attachments/assets/af0f6dbd-2f3b-4419-be5b-3ee5a09ad1ac" />
<img width="635" height="209" alt="Screenshot 2026-05-18 212609" src="https://github.com/user-attachments/assets/e6878ba4-5334-42b6-a68b-24905835a135" />  

- __Class StackKursi:__ Mendefinisikan sebuah kelas baru bernama StackKursi yang berfungsi sebagai struktur utama untuk membuat objek tumpukan kursi  
- __def __init__(self, max_size=5):__ Mnedefinisikan fungsi init dengan parameter max_size yang diberi nilai bawaan yaitu 5, digunakan utuk meginisialisasi properti awal saat objek tumpukan dibuat  
- __self.MAX = max_size:__ Membuat variabel MAX untuk menyimpan batas maksimal kapasitas kursi yang bisa ditumpuk di dalam sistem yaitu 5 kursi  
- __self.st = [None] * self.MAX:__ Membuat sebuah list/array bernama st sepanjangn nilai MAX yang seluruh tempatnya diisi dengan none (kosong) sebagai wadah fisik penyimpanan data kursi  
- __self.top_idx = -1:__ Menginisialisasi variabel pointer top.idx dengan nilai awal -1 sebagai penanda bahwa tumpukan saat ini masih kosong dan belum ada indeks kursi yang ditunjuk  
- __def is_empty(self):__ Mendefinisikan fungsi is_empty untuk mengecek status tumpukan, fungsi ini akan mengembalikan nilai True jika tumpukan kosonh dan False jika ada isinya  
- __return self.top_idx == -1__ Mengembalikan hasil perbandingan logika apakah top_idx bernilai -1 jika iya berarti tumpukan terbukti kosong  
- __def is_full(self):__ Mendefinisikan fungsi is_full untuk mengecek apakah kapasitas tumpukan kursi sudah mencapai batas maksimal yang ditentukan  
- __return self.top_idx == self.MAX - 1:__ Mengembalikan hasil perbandingan apakah nilai top_idx sudah sama dengan MAX -1 (indeks terakhir array) jika iya, maka tumpukan terbukti sudah penuh  
- __def push(self, warna_kursi):__ Mendefinisikan fungsi push dengan parameter warna_kursi untuk memasukkan data warna kursi baru ke posisi paling atas tumpukan  
- __if self.is_full():__ Logika percabangan untuk memeriksa kondisi tumpukan terlebih dahulu dengan memanggil fungsi is_full()  
- __print("Tumpukan kursi sudah terlalu tinggi! tidak bisa menerima kursi baru lagi"):__ Menampilkan pesan tersebut ke layar jika fungsi is_full bernilai True, yang menandakan bahwa kursi baru tidak bisa dimasukkan atau ditambahkan kedalam tumpukan kursi karena tumpukan sudah mencapai batas maksimalnya  
- __return:__ Perintah untuk keluar dari fungsi push agar baris kode dibawahnya tidak dieksekusi jika kondisi tumpukan sudah penuh  
- __self top_idx += 1:__ Menambahkan nilai variabel top_idx sebanyak 1 angka untuk menggeser posisi penunjuk tumpukan ke indeks kosong berikutnya  
- __self.st[self.top_idx] = warna_kursi:__ Memasukkan data warna_kursi yang dsimasukkan pengguna ke dalam array st pada pososo indeks yang ditunjuk oleh top_idx saat ini  
- __print(f"Kursi warna {warna_kursi} berhasil ditambahkan ke tumpukan"):__ Menampilkan pesan tersebut ke layar, menggunakan f-string agar teks warna_kursi terbaca sebagai variabel yang memiliki data atau isi bukan sebagai teks biasa  
- __def pop(self):__ Mendefinisikan fungsi pop untuk mengambil atau menghapus data kursi yang berada di posisi paling atas tumpukan (sesuai prinsip LIFO)  
- __if self.is_empty():__ Logika percabangan untuk memeriksa apakah tumpukan kursi sata ini sedang dalam keadaan kosong dengan memanggil fungsi is_empty()  
- __print("Tumpukan kosong! tidak ada kursi yang bisa diambil"):__ Menampilkan pesan tersebut ke layar jika fungsi is_empty bernilai True, pesan ini berfungsiuntuk memberikan kabar bahwa tidak ada kursi yang bisa diambil karena tumpukan kursi dalam keadaan kosong  
- __return:__ Perintah untuk keluar dari fungsi pop agar program tidak memproses penghapusan data pada tumpukan yang kosong  
- __kursi_diambil = self.st[self.top_idx]:__ Mengambil data warna kursi dari array st pada posisi top_idx saat ini dan menyimpannya ke dalam variabel kursi_diambil  
- __self.top_idx -= 1:__ Mengurangi nilai variabel top_idx sebanyak 1 angka agar penunjuk tumpukan turun ke kursi dibawahnya, secara otomatis akan menghapus akses ke kursi yang sebelumnya berada diatasnya  
- __print(f"Kursi warna {kursi_diambil} diambil dari tumpukan:__ Menampilkan pesan tersebut ke layar menggunakan f-string agar tulisan kursi_diambil tidak dibaca sebagai teks biasa tetapi dibaca sebagai variabel yang memiliki isi atau data di dalamnya  
- __def peek(self):__ Mendefinisikan fungsi peek untuk melihat data kursi yang berada diposisi paling atas tanpa mengubah atau menghapus posisi tumpukan  
- __if self.is_empty():__ Logika percabangan untuk memastikan tumpukan tidak sedang dalamkeadaan kosong sebelum melakukan proses peek  
- __print("Tidak ada kursi di tumpukan"):__ Menampilkan pesan "Tidak ada kursi di tumpukan " ke layar  
- __return:__ Perintah untuk keluar dari fungsi peek jika kondisi tumpukan terbukti kosong  
- __print(f"Kursi yang ada di posisi paling atas adalah kursi berwarna {self.st[self.top_idx]}"):__ Menampilkan data warna kursi yang berada di posisi paling atas tumpukan (indeks top_idx) ke layar menggunakan f-string agar teks self.st[self.top_idx] tidak dibaca sebagai teks biasa  
- __def display(self):__ Mendefinisikan fungsi display untuk menampilkan visualisasi seluruh isi tumpukan kursi secara berurutan mulai dari posisi teratas hingga posisi paling bawah  
- __if self.is_empty():__ Logika percabangan untuk memastikan tumpukan memiliki data sebelum menampilkan daftar kursi ke layar  
- __print("Tumpukan kursi kosong"):__ Menampilkan pesan "Tumpukan kursi kosong" ke layar sebagai pemberitahuan bahwa tumpukan dalam keadaan kosong sehingga tidak ada daftar kursi yang dapat ditampilkan  
- __return:__ Perintah untuk keluar dari fungsi display jika kondisi tumpukan memang kosong  
- __print("\nKondisi tumpukan kursi (Atas ke Bawah): ", end="")__ Menampilkan pesan tersebut ke layar  
- __for i in range(self.top_idx, -1, -1):__ Memulai perulangan for dengan fungsi range yang bergerak mundur dimulai dari indeks tertinggi (top_idx) menuju indeks o dengan langkah penurunan -1  
- __print(self.st[i], end=""):__ Mengambil data warna kursi dari array st pada posisi indeks i yang sedang diulang, lalu menampilkan ke layar dengan tambahan end="" agar antar warna kursi dipisahkan oleh satu spasi dan posisinya berjejer kesamping dibaris yang sama  
- __print():__ Perintah untuk mencetak baris kosong diluar perulangan for yangberfungsi memberikan perintah ganti baris satu kali setelah semua warna kursi selesai ditampilkan agar tampilan lebih rapi  
- __def main():__ Mendefinisikan fungsi utama bernama main() sebagai pusat jalannya seluruh alur program  
- __gudang_kursi = StackKursi(max_size=5):__ Membuat variabel baru bernama gudang_kursi dengan memanggil fungsi class StackKursi dan memeberikan batasan kapasitas maksimal yaitu sebanyak 5 kursi  
- __pilih = 0:__ Menginisialisasi variabel pilih dengan nilai awal 0 yang nantinya akan digunakan untuk menampung nomor menu pilihan dari pengguna  
- __while pilih != 5:__ Membuat peruangan while yang akan terus berjalan dan menampilkan menu utama berulang kali selama pengguna belum memilih angka 5 yang berarti keluar dari program  
- __print("\n-----PROGRAM SIMULASI TUMPUKAN KURSI-----":__ Menampilkan pesan tersebut ke layar sebagai judul dari program ini  
- __print("1. Tumpuk kursi baru"):__ Menampilkan pesan pilihan nomor 1 yaitu untuk melakukan penambahan kursi baru atau fungsi push  
- __print("2. Ambil kursi dari tumpukan"):__ Menampilkan pesan pilihan nomor 2 yaitu untuk melakukan pengambilan kursi dari tumpukan atau fungsi pop  
- __print("3. Lihat kursi"):__ Menampilkan pesan pilihan nomor 3 yaitu untuk melihat kursi teratas atau fungsi peek  
- __print("4. Lihat semua tumpukan kursi"):__ Menampilkan pesan nomor 4 yaitu untuk menampilkan semua daftar tumpukan kursi atau fungsi display  
- __print("5. Keluar"):__ Menampilkan pesan nomor 5 yaitu untuk keluar dari program  
- __try:__ Mmemulai blok untuk mengecek inputan dari pengguna  
- __pilih = int(input("Pilih menu (1-5): ")):__ Meminta pengguna untuk memasukkan nomor menu pilihan dalam bentuk integer (bilangan bulat) dan menyimpannya kedalam variabe pilih  
- __Except ValueError:__ Untuk emangkap kesalahan yang terjadi ketika pengguna memasukkan pilihan nomor menu tidak berupa bilangan bulat  
- __print("Input salah! Masukkan angka."):__ Menampilkan pesan Ïnpust salah! mAaukkan angka" ke layar  
- __continue:__ Perintah untuk melompati baris sisa dibawahnya dan langsung mengulang embali perulangan ke baris menu utama  
- __if pilih == 1:__ Logika percabangan jika variabel pilih atau nilai yang dimasukkan oleh pengguna adalah 1, menandakan bahwa pengguna ingin menambahkan kursi baru kedalam tumpukan  
- __warna = input("\nMasukkan warna kursi:):__  Meminta pengguna memasukkan warna kursi yang inging ditambahkan ke dalam tumpukan dan menyimpannya ke dalam variabel warna  
- __if not warna.isalpha():__ Logika percabangan untuk mengecek apakah isi dari variabel warna mengandung tipe data selain huruf yaitu angka atau simbol  
- __print("Input tidak valid! Warna kursi harus berupa huruf (bukan angka/simbol)."):__ Menampilkan pesan tersebut ke layar jika pengguna memasukkan inputan warna kursi selain huruf  
- __else:__ Kondisi alternatif yang dieksekusi jika pengguna memasukkan input bernar yaitu berupa huruf  
- __gudang_kursi.push():__ Memanggil fungsi pop dari variabel gudang_kursi untuk memasukkan variabel warna ke dalam tumpukan kursi  
- __elif pilih == 2:__ Kondisi alternatif jika pengguna memasukkan pilihan nomor 2 disaat memilih menu utama program  
- __gudang_kursi.pop():__ Memanggil fungsi pop dari variabel gudang_kursi untuk mengeksekusi pengambilan kursti dari sebuah tumpukan  
- __elif pilih == 3:__ Kondisi alternatif jika pengguna memasukkan pilihan nomor 3 di pilihan menu utama program  
- __gudang_kursi.peek():__ Mmemanggil fungsi peek dari variabel gudang_kursi untuk menampilkan informasi warna kursi yang berada ditumpukan teratas  
- __elif pilih == 4:__ ondisi alternatif jika pengguna memasukkan pilihan nomr 3 di pilihan menu utama program  
- __gudang_kursi.display():__ Mmemanggil fungsi display dari variabel gudang_kursi untuk menampilkan seluruh daftar tumpukan kursi yang ada  
- __elif pilih == 5:__ Kondisi alternatif jika pengguna memasukkan pilihan nomor 5 di pilihan menu utama program  
- __print("Program selesai"):__ Menampilkan pesan tersebut kelayar sebagai tanda jika program telah selesai dan keluar dari program  
- __else:__ Kondisi terakhir yang akan berjalan jika pengguna memasukkan pilihan nomor di menu utama berupa bilangan bulat tetapi diluar batas pilihan menu yang tersedia  
- __print("Pilihan menu tidak valid! Silakan pilih 1-5."):__ Menampilkan pesan tersebut ke layar sebagai informasi bahwa pengguna telah memasukkan angka melebihi batas pilihan menu yang ada  
- __if __name__ == "__main__":__ Digunakan untuk memastikan bahwa rangkaian kode ini hanya akan berjalan jika file ini dieksekusi secara langsung  
- __main():__ perintah untuk menjalankan fungsi utaman main() agar program dapat berjalan











__d. Output Program__  

<img width="614" height="482" alt="Screenshot 2026-05-18 212038" src="https://github.com/user-attachments/assets/b28cb252-aab2-426a-bff7-5e4e1c3453b2" />
<img width="617" height="493" alt="Screenshot 2026-05-18 212102" src="https://github.com/user-attachments/assets/409e6021-b53d-44b9-bcde-e9167844643c" />
<img width="618" height="494" alt="Screenshot 2026-05-18 212159" src="https://github.com/user-attachments/assets/f44fe1e0-da0a-4196-a967-9e469f65b393" />
<img width="617" height="503" alt="Screenshot 2026-05-18 212317" src="https://github.com/user-attachments/assets/ba91ec05-ac6b-4133-b054-ee2ac092490b" />
<img width="610" height="57" alt="Screenshot 2026-05-18 212339" src="https://github.com/user-attachments/assets/ad99c996-ea91-4bda-96b9-7ea455d37ea6" />  

__Menampilkan Menu Utama dan Validasi Kesalahan Pilihan__  
Saat program pertama kali dijalankan, sistem akan langsung masuk ke dalam fungsi main() dan menampilkan pesan "----- PROGRAM SIMULASI TUMPUKAN KURSI -----" sebagai judul utama sistem. Di bawah judul, program akan menampilkan 5 daftar pilihan dari menu utama, yaitu: 1. Tumpuk kursi baru, 2. Ambil kursi dari tumpukan, 3. Lihat Kursi, 4. Tampilkan Semua tumpukan kursi, dan 5. Keluar.

Setelah daftar menu ditampilkan, selanjutnya program akan menampilkan pesan "Pilih Menu (1-5): " untuk meminta pengguna memasukkan angka pilihan dari daftar menu yang ada. Jika pada saat memilih menu ternyata pengguna salah memasukkan inputan berupa huruf atau simbol, maka program akan mendeteksi terjadinya kesalahan pada saat memasukkan inputan, dan otomatis akan menjalankan atau mengeksekusi bagian except ValueError yaitu menampilkan pesan "Input salah! Masukkan angka." sebagai peringatan kepada pengguna bahwa pengguna telah memasukkan inputan yang salah. Setelah pesan tersebut keluar, program akan menjalankan perintah continue, yang artinya program tidak akan berhenti melainkan otomatis memunculkan kembali judul utama dan daftar menu dari awal sampai pengguna memasukkan pilihan menu sesuai dengan format yang telah ditentukan yaitu berupa angka bilangan bulat. Namun, jika pengguna memasukkan inputan berupa angka bilangan bulat tetapi angkanya di luar rentang pilihan yang ada (misalnya angka 6) maka sistem akan masuk ke logika else paling bawah dan menampilkan pesan "Pilihan menu tidak valid!".  

__Proses Tambah Kursi dan Validasi Karakter Huruf (Menu 1)__  
Apabila pengguna memilih menu 1, program akan masuk ke kondisi if pilih == 1 dan menampilkan pesan "Masukkan warna kursi: ". Di sini pengguna diminta untuk memasukkan inputan warna dari kursi baru yang ingin ditambahkan. Sistem ini memiliki fungsi proteksi khusus menggunakan .isalpha() sebagai syarat bahwa inputan harus berupa alfabet. Jika pengguna memasukkan angka atau simbol (misalnya mengetik 123), maka program akan langsung mendeteksi bahwa inputan tersebut bukan berupa alfabet murni, yangmana langsung menjalankan kondisi if not warna.isalpha(), lalu akan menampilkan pesan "Input tidak valid! Warna kursi harus berupa huruf (bukan angka/simbol)." sebagai pemberitahuan bahwa pengguna harus memasukkan inputan berupa huruf alfabet.

Sebaliknya, jika pengguna memasukkan data dengan benar berupa huruf alfabet murni (misalnya Merah), sistem akan menjalankan fungsi push(warna). Selama kapasitas array tumpukan belum penuh, maka data tersebut otomatis akan disimpan dan ditambahkan kedalam tumpukan dan program akan memunculkan pesan "Kursi warna Merah berhasil ditambahkan ke tumpukan." sebagai pemberitahuan bahwa operasi penambhan kursi baru berhasil dilakukan. Namun, jika pengguna terus menambahkan kursi hingga melebihi batas maksimal kapasitas penumpukan (max_size=5), maka fungsi is_full() akan bernilai True sehingga program menghentikan proses penambahan kursi baru atau push dan mengeluarkan pesan "Tumpukan kursi sudah terlalu tinggi! tidak bisa menerima kursi baru lagi" sebagai pemberitahuan bahwa tumpukan telah mencapai kapasitas maksimalnya dan tidak bisa menerima inputan lagi.  

__Proses Pengambilan Kursi Teratas (Menu 2)__
Jika pengguna memilih menu 2, program akan mengeksekusi kode fungsi pop() sebagai proses penghapusan atau pengambilan kursi yang dilakukan dari tumpukan kursi yang ada. Berdasarkan prinsip struktur data Stack yaitu LIFO (Last In, First Out), sistem secara otomatis akan mengambil data kursi yang posisinya berada di paling atas (indeks data yang terakhir kali dimasukkan). Jika di dalam tumpukan terdapat kursi, program akan menampilkan pesan "Kursi warna (nama warna teratas, misal: Merah) diambil dari tumpukan." sebagai pemberitahuan bahwa proses penghapusan atau pengambilan berhasil dijalankan, lalu menurunkan posisi penunjuk indeks paling atasnya ke indeks yang berada dibawahnya. Namun, jika pengguna memilih menu ini saat belum ada satu pun kursi yang dimasukkan ke dalam sistem, maka fungsi is_empty() akan bernilai True, dan program akan membatalkan proses penghapusan atau pengambilan yang ingin dilakukan dengan menampilkan pesan "Tumpukan kosong! tidak ada kursi yang bisa diambil".  

__Proses Melihat Kursi Teratas (Menu 3)__  
Ketika pengguna memilih pilihan menu pada pilihan 3, maka program akan memanggil atau menjalankan fungsi peek() yang berguna untuk melihat kursi yang berada di posisi teratas. Selama kondisi tumpukan tidak kosong, sistem akan langsung membaca data pada indeks teratas tanpa mengubah susunan tumpukan, lalu menampilkannya ke layar melalui pesan "Kursi yang ada di posisi paling atas adalah kursi berwarna (nama warna kursi teratas, misal: Merah)". Jika operasi ini dilakukan pada saat sistem belum memiliki data kursi sama sekali, logika percabangan akan langsung mengarahkan program untuk menampilkan pesan "Tidak ada kursi di tumpukan." sebagai pesan pemberitahuan bahwa saat itu tidak ada kursi sama sekali didalam tumpukan  

__Proses Menampilkan Seluruh Struktur Tumpukan (Menu 4)__  
Apabila pengguna memilih pilihan pada menu 4, maka program akan memanggil atau menjalankan fungsi display() untuk menampilkan seluruh data kursi yang ada didalam tumpukan. Jika data tersedia, sistem akan menampilkan pesan "\nKondisi tumpukan kursi (Atas ke Bawah): " ke layar. Setelah itu, program mengaktifkan mekanisme perulangan mundur (looping range) dari indeks tertinggi ke terendah, lalu mencetak semua warna kursi secara berjejer menyamping yang dipisahkan oleh karakter spasi tunggal, misalnya "hitam hijau biru coklat merah". Hal ini mempermudah pengguna untuk melihat urutan tumpukan secara cepat. Jika kondisi tumpukan ternyata masih kosong saat menu ini dipilih, maka program akan mendeteksinya melalui fungsi is_empty() dan langsung memunculkan pesan "Tumpukan kursi kosong.".  

__Kondisi Keluar dari Program (Menu 5)__  
Jika pengguna memilih pilihan 5 pada pilihan daftar menu, maka program akan menampilkan pesan "Program selesai." ke layar dan otomatis akan keluar dari program atau program akan otomatis akan berhenti, yang menandakan bahwa perulangan while telah dihentikan dan seluruh rangkaian operasional pada program ini ditutup dengan aman.
