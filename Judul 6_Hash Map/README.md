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




