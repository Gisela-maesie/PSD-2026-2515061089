def sequential_search(nilai_siswa, n, target):
    i = 0
    counter = 0
    while i < n:
        if nilai_siswa[i] == target:
            counter += 1
        i += 1
    return counter


def main():
    nilai_siswa = [60, 55, 100, 70, 75, 70, 80, 90, 65, 80, 95, 60, 45, 50, 40, 100, 100, 50, 65, 100]
    n = len(nilai_siswa)
    print("\n-----SISTEM ANALISIS NILAI TRY OUT-----\n")
    print(f"Daftar nilai try out: {nilai_siswa}\n")
    while True:
        try:
            target = int(input("Masukkan nilai try out yang ingin dicari (0-100): "))
            break
        except ValueError:
            print("Input tidak valid, silakan masukkan angka!")
    counter = sequential_search(nilai_siswa, n, target)
    if counter > 0:
        print(f"\nHasil: Nilai {target} ditemukan pada {counter} orang siswa.")
        print(f"Keterangan: Ada {counter} orang siswa yang mendapatkan nilai {target} dalam try out ini")
    else:
        print(f"Hasil: Tidak ada siswa yang mendapatkan nilai {target}.")
        
        
if __name__ == "__main__":
    main()