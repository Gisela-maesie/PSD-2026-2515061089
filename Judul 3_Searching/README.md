__a. Judul Program__  
Aplikasi Penghitung Frekuensi Nilai Ujian Try Out  

__b. Deskripsi Singkat__  
Program ini dirancang sebagai aplikasi sederhana namun efektif untuk membantu pengajar dalam memantau nilai hasil ujian siswa. Fungsi utama dari program ini adalah memberikan kemudahan bagi pengguna untuk mencari tahu seberapa banyak siswa yang mendapatkan skor tertentu dalam satu kali ujian. Dengan menggunakan aplikasi ini, proses analisis nilai menjadi lebih terorganisir, sehingga pengajar dapat melihat distribusi nilai secara cepat tanpa harus menghitungnya secara manual satu per satu.  

Aplikasi ini menggunakan algoritma Sequential Search. Pemilihan metode ini didasarkan pada karakteristiknya yang sangat fleksibel dalam menangani data yang tidak terurut (acak), seperti daftar nilai yang masuk secara acak. Karena menggunakan pencarian berurutan dari awal hingga akhir data, program ini mampu memindai seluruh isi daftar nilai untuk memastikan setiap skor yang sama dapat terhitung dengan akurat.  

__c. Source Code__  
<img width="698" height="464" alt="Screenshot 2026-05-09 231019" src="https://github.com/user-attachments/assets/b749bf76-c404-4099-8753-31cbbd161800" />

- __def sequential_search(nilai_siswa, n, target):__ Mendefinisikan fungsi bernama sequential_search dengan tiga parameter yaitu data nilai (nilai_siswa), jumlah data(n), dan nilai yang dicari (target)
- __i = 0:__ Inisialisasi variabel i atau indeks dengan nilai 0 sebagai penanda bahwa pencarian dimulai dari indeks 0
- __counter = 0:__ Inisialisasi variabel counter dengan nilai 0 sebagai nilai awalnya dan variabel ini digunakan untuk menghitung berapa kali nilai yang dicari ditemukan di dalam daftar
- __while i < n:__ Memulai perulangan yang akan terus berjalan selama indeks i masih lebih kecil dari jumlah data (n)
- __if nilai_siswa[i] == target:__ Logika percabangan untuk mengecek apakah nilai pada posisi i sama dengan nilai target yang dicari
- __counter += 1:__ Menambahkan nilai 1 ke dalam variabel counter jika ditemukan data yang cocok dengan nilai yag di cari
- __i += 1:__ Menambahkan nilai 1 ke variabel i atau indeks agar program berlanjut mengecek data yang ada pada posisi berikutnya
- __return counter:__ Mengembalikan nilai counter yang ada
- __def main():__ Mendefinisikan fungsi utama bernama main() sebagai pusat berjalannya program
- __nilai_siswa = [60, 55, 100, 70, 75, 70, 80, 90, 65, 80, 95, 60, 45, 50, 40, 100, 100, 50, 65, 90]:__ Membuat variabel nilai_siswa yang berisi kumpulan nilai hasil ujian try out para siswa
- __n = len(nilai_siswa):__ Menghitung total banyaknya data yang ada di dalam variabel nilai_siswa menggunakan fungsi len() dan menyimpannya di dalam variabel n
- __print("\n-----SISTEM ANALISIS NIALI TRY OUT---\n):__ Menampilkan pesan SISTEM ANALISIS NILAI TRY OUT ke layar sebagai judul program agar pengguna tahu program apa yang sedang berjalan
- __print(f"Daftar nilai try out: {nilai_siswa}\n):__ Menampilkan seluruh isi data nilai yang tersedia di dalam variabel nilai_siswa ke layar menggunakan fungsi f-string agar nilai_siswa dapat dibaca sebagai variabel yang memiliki data didalamnya bukan sebagai teks biasa
- __while True:__  Memulai perulangan yang akan terus berjalan sampai input data yang dimasukkan oleh user itu benar
- __try:__ Percobaan untuk mengeksekusi kode input
- __target = int(input("Masukkan nilai yang ingin dicari (0-100):__ Meminta pengguna untuk memasukkan inputan berupa nilai yang ingin dicari dalam bentuk bilangan bulat (integer) dengan rentang nilai dari 0 sampai 100
- __break:__ Berhenti dan keluar dari perulangan while True jika inputan yang dimasukkan oleh user sudah benar
- __except ValueError:__ Menangkap kesalahan jika pengguna memasukkan inputan selain angka bilangan bulat misalnya bilangan desimal, huruf atau simbol
- __print("Input tidak valid, silahkan masukkan angka!"):__ Menampilkan pesan tersebut ke layar jika pengguna memasukkan inputan selain angka bilangan bulat
- __counter = sequential_search(nilai_siswa, n, target):__ Memanggil fungsi sequential_search dan menyimpan hasil hitungannya ke dalam variabel counter
- __if counter > 0:__ Logika percabangan jika hasil hitungan ditemukan lebih dari 0
- __print(f"\nHasil: Nilai {target} ditemukan pada {counter} orang siswa"):__ Menampilkan pesan berupa informasi jumlah siswa yang memiliki nilai yang dicari oleh pengguna tadi ke layar dan disini menggunakan f-string untuk membaca tulisan target dan counter sebagai variabel yang memiliki data bukan sebagai teks biasa
- __print(f"Keterangan: Ada {counter} orang siswa" f" yang mendapatkan nilai {target} dalam try out ini"):__ Menampilkan pesan berupa informasi jumlah siswa yang memiliki nilai yang dicari oleh pengguna tadi dalam try out kali ini ke layar dan disini menggunakan f-string untuk membaca tulisan target dan counter sebagai variabel yang memiliki data bukan sebagai teks biasa
- __else:__ Dijalankan jika nilai yang dicari tidak ditemukan sama sekali di dalam daftar yang ada
- __print(f"Hasil: Tidak ada siswa yang mendapatkan nilai {target}"):__ Menampilkan pesan tersebut ke layar sebagai informasi bahwa nilai yang dicari tidak ada atau tidak ditemukan di dalam daftar nilai yang tersedia dan disini menggunakan fungsi f-string untuk membaca tulisan target sebagai variabel yang memiliki data bukan sebagai teks biasa
- __if __name__=="__main__":__ Digunakan untuk memastikan bahwa fungsi main() hanya akan berjalan jika file ini dieksekusi secara langsung
- __main():__ Perintah untuk mengeksekusi atau menjalankan seluruh rangkaian yang ada di fungsi main() atau fungsi utama

