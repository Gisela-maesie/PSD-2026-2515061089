__a. Judul Program__  
Sistem Manajemen Tumpukan Kursi Berbasis Struktur Data Stack Array

__b. Deskripsi Program__  
Porgram ini dirancang sebagai sistem sederhana namun efektif untuk membantu pengelola fasilitas atau kru lapangan dalam memantau inventaris tumpukan kursi di suatu tempat, misalnya seperti aula, gedung acara, atau tenda. Fungsi utama dari program ini adalah memberikan kemudahan bagi pengguna untuk mengelola proses keluar masuknya kursi secara teratur di suatu tempat. Dengan menggunakan sistem ini, proses penataan akan menjadi lebih terorganisir, sehingga pengguna dapat melihat urutan tumpukan kursi secara cepat tanpa harus mengeceknya secara manual satu persatu  

Aplikasi ini menggunakan metode Stack Array. Pemilihan metode ini karena karakteristiknya yang menggunakan prinsip LIFO (Last In First Out), yangmana sangat mencerminkan kondisi yang terjadi di dunia nyata. Kursi yang terakhir dimasukkan pasti akan menjadi kursi yang pertama kali diambil ketika kursi ingin digunakan, hal ini yang mengakibatkan mengapa penggunaan metode stack array sangat sesuai dengan keadaan seperti ini. 

__c. Source Code__  
<img width="635" height="476" alt="Screenshot 2026-05-18 212454" src="https://github.com/user-attachments/assets/6f41fc13-43dd-4c78-bb97-455c59a092e0" />
<img width="636" height="463" alt="Screenshot 2026-05-18 212541" src="https://github.com/user-attachments/assets/af0f6dbd-2f3b-4419-be5b-3ee5a09ad1ac" />
<img width="635" height="209" alt="Screenshot 2026-05-18 212609" src="https://github.com/user-attachments/assets/e6878ba4-5334-42b6-a68b-24905835a135" />  

__- Class StackKursi:__ Mendefinisikan sebuah kelas baru bernama StackKursi yang berfungsi sebagai struktur utama untuk membuat objek tumpukan kursi  
__- def __init__(self, max_size=5):__ Mnedefinisikan fungsi init dengan parameter max_size yang diberi nilai bawaan yaitu 5, digunakan utuk meginisialisasi properti awal saat objek tumpukan dibuat  
__- self.MAX = max_size:__ Membuat variabel MAX untuk menyimpan batas maksimal kapasitas kursi yang bisa ditumpuk di dalam sistem yaitu 5 kursi  
__- self.st = [None] * self.MAX:__ Membuat sebuah list/array bernama st sepanjangn nilai MAX yang seluruh tempatnya diisi dengan none (kosong) sebagai wadah fisik penyimpanan data kursi  
__- self.top_idx = -1:__ Menginisialisasi variabel pointer top.idx dengan nilai awal -1 sebagai penanda bahwa tumpukan saat ini masih kosong dan belum ada indeks kursi yang ditunjuk  
__- def is_empty(self):__ Mendefinisikan fungsi is_empty untuk mengecek status tumpukan, fungsi ini akan mengembalikan nilai True jika tumpukan kosonh dan False jika ada isinya  
__- return self.top_idx == -1__ Mengembalikan hasil perbandingan logika apakah top_idx bernilai -1 jika iya berarti tumpukan terbukti kosong  
__- def is_full(self):__ Mendefinisikan fungsi is_full untuk mengecek apakah kapasitas tumpukan kursi sudah mencapai batas maksimal yang ditentukan  
__- return self.top_idx == self.MAX - 1:__ Mengembalikan hasil perbandingan apakah nilai top_idx sudah sama dengan MAX -1 (indeks terakhir array) jika iya, maka tumpukan terbukti sudah penuh  
__- def push(self, warna_kursi):__ Mendefinisikan fungsi push dengan parameter warna_kursi untuk memasukkan data warna kursi baru ke posisi paling atas tumpukan  
__- if self.is_full():__ Logika percabangan untuk memeriksa kondisi tumpukan terlebih dahulu dengan memanggil fungsi is_full()  
__- print("Tumpukan kursi sudah terlalu tinggi! tidak bisa menerima kursi baru lagi"):__ Menampilkan pesan tersebut ke layar jika fungsi is_full bernilai True, yang menandakan bahwa kursi baru tidak bisa dimasukkan atau ditambahkan kedalam tumpukan kursi karena tumpukan sudah mencapai batas maksimalnya  
__- return:__ Perintah untuk keluar dari fungsi push agar baris kode dibawahnya tidak dieksekusi jika kondisi tumpukan sudah penuh  
__- self top_idx += 1:__ Menambahkan nilai variabel top_idx sebanyak 1 angka untuk menggeser posisi penunjuk tumpukan ke indeks kosong berikutnya  
__- self.st[self.top_idx] = warna_kursi:__ Memasukkan data warna_kursi yang dsimasukkan pengguna ke dalam array st pada pososo indeks yang ditunjuk oleh top_idx saat ini  
__- print(f"Kursi warna {warna_kursi} berhasil ditambahkan ke tumpukan"):__ Menampilkan pesan tersebut ke layar, menggunakan f-string agar teks warna_kursi terbaca sebagai variabel yang memiliki data atau isi bukan sebagai teks biasa  
__- def pop(self):__ Mendefinisikan fungsi pop untuk mengambil atau menghapus data kursi yang berada di posisi paling atas tumpukan (sesuai prinsip LIFO)  
__- if self.is_empty():__ Logika percabangan untuk memeriksa apakah tumpukan kursi sata ini sedang dalam keadaan kosong dengan memanggil fungsi is_empty()  
__- print("Tumpukan kosong! tidak ada kursi yang bisa diambil"):__ Menampilkan pesan tersebut ke layar jika fungsi is_empty bernilai True, pesan ini berfungsiuntuk memberikan kabar bahwa tidak ada kursi yang bisa diambil karena tumpukan kursi dalam keadaan kosong  
__- return:__ Perintah untuk keluar dari fungsi pop agar program tidak memproses penghapusan data pada tumpukan yang kosong  
__- kursi_diambil = self.st[self.top_idx]:__ Mengambil data warna kursi dari array st pada posisi top_idx saat ini dan menyimpannya ke dalam variabel kursi_diambil  
__- self.top_idx -= 1:__ Mengurangi nilai variabel top_idx sebanyak 1 angka agar penunjuk tumpukan turun ke kursi dibawahnya, secara otomatis akan menghapus akses ke kursi yang sebelumnya berada diatasnya  
__- print(f"Kursi warna {kursi_diambil} diambil dari tumpukan:__ Menampilkan pesan tersebut ke layar menggunakan f-string agar tulisan kursi_diambil tidak dibaca sebagai teks biasa tetapi dibaca sebagai variabel yang memiliki isi atau data di dalamnya  
__- def peek(self):__ Mendefinisikan fungsi peek untuk melihat data kursi yang berada diposisi paling atas tanpa mengubah atau menghapus posisi tumpukan  
__- if self.is_empty():__ Logika percabangan untuk memastikan tumpukan tidak sedang dalamkeadaan kosong sebelum melakukan proses peek  
__- print("Tidak ada kursi di tumpukan"):__ Menampilkan pesan "Tidak ada kursi di tumpukan " ke layar  
__- return:__ Perintah untuk keluar dari fungsi peek jika kondisi tumpukan terbukti kosong  
__- print(f"Kursi yang ada di posisi paling atas adalah kursi berwarna {self.st[self.top_idx]}"):__ Menampilkan data warna kursi yang berada di posisi paling atas tumpukan (indeks top_idx) ke layar menggunakan f-string agar teks self.st[self.top_idx] tidak dibaca sebagai teks biasa  
__- def display(self):__ Mendefinisikan fungsi display untuk menampilkan visualisasi seluruh isi tumpukan kursi secara berurutan mulai dari posisi teratas hingga posisi paling bawah  
__- if self.is_empty():__ Logika percabangan untuk memastikan tumpukan memiliki data sebelum menampilkan daftar kursi ke layar  
__- print("Tumpukan kursi kosong"):__ Menampilkan pesan "Tumpukan kursi kosong" ke layar sebagai pemberitahuan bahwa tumpukan dalam keadaan kosong sehingga tidak ada daftar kursi yang dapat ditampilkan  
__- return:__ Perintah untuk keluar dari fungsi display jika kondisi tumpukan memang kosong  
__- print("\nKondisi tumpukan kursi (Atas ke Bawah): ", end="")__ Menampilkan pesan tersebut ke layar  
__- for i in range(self.top_idx, -1, -1):__ Memulai perulangan for dengan fungsi range yang bergerak mundur dimulai dari indeks tertinggi (top_idx) menuju indeks o dengan langkah penurunan -1  
__- print(self.st[i], end=""):__ Mengambil data warna kursi dari array st pada posisi indeks i yang sedang diulang, lalu menampilkan ke layar dengan tambahan end="" agar antar warna kursi dipisahkan oleh satu spasi dan posisinya berjejer kesamping dibaris yang sama  
__- print():__ Perintah untuk mencetak baris kosong diluar perulangan for yangberfungsi memberikan perintah ganti baris satu kali setelah semua warna kursi selesai ditampilkan agar tampilan lebih rapi  
__-def main():__ Mendefinisikan fungsi utama bernama main() sebagai pusat jalannya seluruh alur program  
__- gudang_kursi = StackKursi(max_size=5):__ Membuat variabel baru bernama gudang_kursi dengan memanggil fungsi class StackKursi dan memeberikan batasan kapasitas maksimal yaitu sebanyak 5 kursi  
__- pilih = 0:__ Menginisialisasi variabel pilih dengan nilai awal 0 yang nantinya akan digunakan untuk menampung nomor menu pilihan dari pengguna  
__- while pilih != 5:__ Membuat peruangan while yang akan terus berjalan dan menampilkan menu utama berulang kali selama pengguna belum memilih angka 5 yang berarti keluar dari program  
__- print("\n-----PROGRAM SIMULASI TUMPUKAN KURSI-----":__ Menampilkan pesan tersebut ke layar sebagai judul dari program ini  
__- print("1. Tumpuk kursi baru"):__ Menampilkan pesan pilihan nomor 1 yaitu untuk melakukan penambahan kursi baru atau fungsi push  
__- print("2. Ambil kursi dari tumpukan"):__ Menampilkan pesan pilihan nomor 2 yaitu untuk melakukan pengambilan kursi dari tumpukan atau fungsi pop  
__- print("3. Lihat kursi"):__ Menampilkan pesan pilihan nomor 3 yaitu untuk melihat kursi teratas atau fungsi peek  
__- print("4. Lihat semua tumpukan kursi"):__ Menampilkan pesan nomor 4 yaitu untuk menampilkan semua daftar tumpukan kursi atau fungsi display  
__- print("5. Keluar"):__ Menampilkan pesan nomor 5 yaitu untuk keluar dari program  
__-try:__ Mmemulai blok untuk mengecek inputan dari pengguna  
__- pilih = int(input("Pilih menu (1-5): ")):__ Meminta pengguna untuk memasukkan nomor menu pilihan dalam bentuk integer (bilangan bulat) dan menyimpannya kedalam variabe pilih  
__- Except ValueError:__ Untuk emangkap kesalahan yang terjadi ketika pengguna memasukkan pilihan nomor menu tidak berupa bilangan bulat  
__-  print("Input salah! Masukkan angka."):__ Menampilkan pesan Ïnpust salah! mAaukkan angka" ke layar  
__- continue:__ Perintah untuk melompati baris sisa dibawahnya dan langsung mengulang embali perulangan ke baris menu utama  
__- if pilih == 1:__ Logika percabangan jika variabel pilih atau nilai yang dimasukkan oleh pengguna adalah 1, menandakan bahwa pengguna ingin menambahkan kursi baru kedalam tumpukan  
__- warna = input("\nMasukkan warna kursi:):__  Meminta pengguna memasukkan warna kursi yang inging ditambahkan ke dalam tumpukan dan menyimpannya ke dalam variabel warna  
__- if not warna.isalpha():__ Logika percabangan untuk mengecek apakah isi dari variabel warna mengandung tipe data selain huruf yaitu angka atau simbol  
__- print("Input tidak valid! Warna kursi harus berupa huruf (bukan angka/simbol)."):__ Menampilkan pesan tersebut ke layar jika pengguna memasukkan inputan warna kursi selain huruf  
__- else:__ Kondisi alternatif yang dieksekusi jika pengguna memasukkan input bernar yaitu berupa huruf  
__- gudang_kursi.push():__ Memanggil fungsi pop dari variabel gudang_kursi untuk memasukkan variabel warna ke dalam tumpukan kursi  
__- elif pilih == 2:__ Kondisi alternatif jika pengguna memasukkan pilihan nomor 2 disaat memilih menu utama program  
__- gudang_kursi.pop():__ Memanggil fungsi pop dari variabel gudang_kursi untuk mengeksekusi pengambilan kursti dari sebuah tumpukan  
__- elif pilih == 3:__ Kondisi alternatif jika pengguna memasukkan pilihan nomor 3 di pilihan menu utama program  
__- gudang_kursi.peek():__ Mmemanggil fungsi peek dari variabel gudang_kursi untuk menampilkan informasi warna kursi yang berada ditumpukan teratas  
__- elif pilih == 4:__ ondisi alternatif jika pengguna memasukkan pilihan nomr 3 di pilihan menu utama program  
__- gudang_kursi.display():__ Mmemanggil fungsi display dari variabel gudang_kursi untuk menampilkan seluruh daftar tumpukan kursi yang ada  
__- elif pilih == 5:__ Kondisi alternatif jika pengguna memasukkan pilihan nomor 5 di pilihan menu utama program  
__- print("Program selesai"):__ Menampilkan pesan tersebut kelayar sebagai tanda jika program telah selesai dan keluar dari program  
__- else:__ Kondisi terakhir yang akan berjalan jika pengguna memasukkan pilihan nomor di menu utama berupa bilangan bulat tetapi diluar batas pilihan menu yang tersedia  
__- print("Pilihan menu tidak valid! Silakan pilih 1-5."):__ Menampilkan pesan tersebut ke layar sebagai informasi bahwa pengguna telah memasukkan angka melebihi batas pilihan menu yang ada  
__- if __name__ == "__main__":__ Digunakan untuk memastikan bahwa rangkaian kode ini hanya akan berjalan jika file ini dieksekusi secara langsung  
__- main():__ perintah untuk menjalankan fungsi utaman main() agar program dapat berjalan











__d. Output Program__  

<img width="614" height="482" alt="Screenshot 2026-05-18 212038" src="https://github.com/user-attachments/assets/b28cb252-aab2-426a-bff7-5e4e1c3453b2" />
<img width="617" height="493" alt="Screenshot 2026-05-18 212102" src="https://github.com/user-attachments/assets/409e6021-b53d-44b9-bcde-e9167844643c" />
<img width="618" height="494" alt="Screenshot 2026-05-18 212159" src="https://github.com/user-attachments/assets/f44fe1e0-da0a-4196-a967-9e469f65b393" />
<img width="617" height="503" alt="Screenshot 2026-05-18 212317" src="https://github.com/user-attachments/assets/ba91ec05-ac6b-4133-b054-ee2ac092490b" />
<img width="610" height="57" alt="Screenshot 2026-05-18 212339" src="https://github.com/user-attachments/assets/ad99c996-ea91-4bda-96b9-7ea455d37ea6" />
