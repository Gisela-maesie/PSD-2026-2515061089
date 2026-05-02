def tukar(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def bubble_sort(arr, n):
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                tukar(arr, j, j + 1)

def main():
    print("\n--- SISTEM PENGURUTAN DATA BERAT BADAN ANAK DI POSYANDU ---\n")
    try:
        n = int(input("Masukkan jumlah anak : "))
    except ValueError:
        print("Input tidak valid!")
        return

    berat_badan = []
    print(f"Masukkan data berat badan untuk {n} anak (kg) : ")
    for i in range(n):
        while True:
            try:
                nilai = float(input(f"Anak ke-{i+1} : "))
                berat_badan.append(nilai)
                break
            except ValueError:
                print("Masukkan angka berat badan yang valid!")

    print(f"\nData berat badan awal : {berat_badan}")
    bubble_sort(berat_badan, n)
    print("\nUrutan berat badan setelah diurutkan dari paling ringan ke paling berat : ", end=" ")
    for i in range(n):
        print(f"{berat_badan[i]} kg", end=" ")
    print()

if __name__ == "__main__":
    main()
