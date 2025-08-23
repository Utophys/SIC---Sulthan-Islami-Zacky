import sys

def tugas1_simpan_dan_tampil_data():

    # Tugas 1: Menyimpan dan Menampilkan Data.
    
    print("\n--- Menjalankan Tugas 1: Menyimpan dan Menampilkan Data ---")
    
    produk_1 = "Kopi Pagi"
    harga_1 = 18000.5
    produk_2 = "Roti Cokelat"
    harga_2 = 10000
    statusRoti = True

    print(f"Nama produk 1: {produk_1}")
    print(f"Harga produk 1: {harga_1}")
    print(f"Nama produk 2: {produk_2}")
    print(f"Harga produk 2: {harga_2}")
    print(f"Status ketersediaan roti: {statusRoti}")
    print("--- Selesai Tugas 1 ---")

def tugas2_konversi_tipe_data_dan_input():
    
    # Tugas 2: Konversi Tipe Data dan Input Pengguna.

    print("\n--- Menjalankan Tugas 2: Konversi Tipe Data dan Input Pengguna ---")
    
    jumlah_kopi_str = input("Masukkan jumlah pesanan kopi: ")
    jumlah_roti_str = input("Masukkan jumlah pesanan roti: ")

    print(f"Tipe data awal jumlah kopi: {type(jumlah_kopi_str)}")
    print(f"Tipe data awal jumlah roti: {type(jumlah_roti_str)}")

    try:
        jumlah_kopi_int = int(jumlah_kopi_str)
        jumlah_roti_int = int(jumlah_roti_str)
        print(f"Tipe data setelah konversi (kopi): {type(jumlah_kopi_int)}")
        print(f"Tipe data setelah konversi (roti): {type(jumlah_roti_int)}")
    except ValueError:
        print("Error: Input harus angka.")
        return 
    
    print("--- Selesai Tugas 2 ---")
    return jumlah_kopi_int, jumlah_roti_int

def tugas3_operasi_pada_angka():
    
    # Tugas 3: Operasi pada Angka.
    
    print("\n--- Menjalankan Tugas 3: Operasi pada Angka ---")

    harga_1 = 18000.5
    harga_2 = 10000
    
    jumlah_kopi_str = input("Masukkan jumlah pesanan kopi: ")
    jumlah_roti_str = input("Masukkan jumlah pesanan roti: ")
    uang_bayar = 50000

    try:
        jumlah_kopi = float(jumlah_kopi_str)
        jumlah_roti = float(jumlah_roti_str)
    except ValueError:
        print("Error: Jumlah pesanan harus angka.")
        return 

    total_harga_kopi = harga_1 * jumlah_kopi
    total_harga_roti = harga_2 * jumlah_roti

    total_belanja = total_harga_kopi + total_harga_roti

    print(f"Total harga kopi: Rp{total_harga_kopi:.2f}")
    print(f"Total harga roti: Rp{total_harga_roti:.2f}")
    print(f"Uang yang dibayarkan: Rp{uang_bayar:.2f}")

    kembalian = uang_bayar - total_belanja

    print(f"Total belanja: Rp{total_belanja:.2f}")
    print(f"Kembalian: Rp{kembalian:.2f}")

    print("--- Selesai Tugas 3 ---")

def tugas4_operasi_pada_string():

    # Tugas 4: Operasi pada String

    print("\n--- Menjalankan Tugas 4: Operasi pada String ---")
    
    nama_pelanggan = input("Masukkan nama pelanggan: ")


    pesan_terima_kasih = "Terimakasih" + " " + nama_pelanggan + " " + "sudah berbelanja di Coffee Shop Bahagia!"

    total_belanja = 36001.0

    print("\n")
    print("*" * 25)
    print(f"\n {pesan_terima_kasih} \n")
    print("*" * 25)
    print("\n")


    print(f"Total harga Kopi Pagi adalah Rp{total_belanja}") 
    
    print("--- Selesai Tugas 4 ---")

if __name__ == "__main__":
    while True:
        print("\n=== Pilih Tugas yang Ingin Dijalankan ===")
        print("1. Tugas 1: Menyimpan dan Menampilkan Data")
        print("2. Tugas 2: Konversi Tipe Data dan Input Pengguna")
        print("3. Tugas 3: Operasi pada Angka")
        print("4. Tugas 4: Operasi pada String")
        print("0. Keluar")

        pilihan = input("Masukkan Pilihan (0-4): ")

        if pilihan == '1':
            tugas1_simpan_dan_tampil_data()
        elif pilihan == '2':
            tugas2_konversi_tipe_data_dan_input()
        elif pilihan == '3':
            tugas3_operasi_pada_angka()
        elif pilihan == '4':
            tugas4_operasi_pada_string()
        elif pilihan == '0':
            print("Terima kasih! Program selesai.")
            sys.exit()
        else:
            print("Pilihan tidak valid. Silakan masukkan angka antara 0 dan 4.")

