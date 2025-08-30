# Fungsi untuk mendapatkan input numerik yang valid
def get_valid_input(prompt, value_type):
  
    # Meminta input dari pengguna dan memastikan itu adalah angka yang valid.
    while True:
        try:
            value = value_type(input(prompt))
            if value <= 0:
                print("Input harus berupa angka positif. Silakan coba lagi.")
            else:
                return value
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka.")



# Fungsi utama untuk menentukan kategori BMI
def tentukan_kategori_bmi(berat, tinggi_meter):
    
    # Menghitung BMI dan menentukan kategorinya berdasarkan rentang standar.
    
    # Menghitung BMI dengan rumus: berat (kg) / tinggi (m)^2
    bmi = berat / (tinggi_meter ** 2)

    # Menentukan kategori BMI menggunakan if/elif/else dan operator logika
    if bmi < 18.5:
        kategori = "Kurus (Underweight)"
    elif 18.5 <= bmi < 24.9:
        kategori = "Normal"
    elif 24.9 <= bmi < 29.9:
        kategori = "Gemuk (Overweight)"
    else:  # bmi >= 29.9
        kategori = "Obesitas (Obesity)"

    return bmi, kategori


# Fungsi utama yang menjalankan program
def main():

    # Fungsi utama untuk menjalankan program kalkulator BMI.
    print("Selamat datang di Kalkulator BMI!")
    print("-----------------------------------")
    
    # Mendapatkan input berat dan tinggi dari pengguna
    berat = get_valid_input("Masukkan berat badan Anda dalam kilogram (kg): ", float)
    tinggi = get_valid_input("Masukkan tinggi badan Anda dalam meter (cm): ", float)

    tinggi_meter = tinggi / 100  # Mengubah tinggi dari cm ke meter

    # Menghitung BMI dan menentukan kategori
    bmi, kategori = tentukan_kategori_bmi(berat, tinggi_meter)

    # Menampilkan hasil
    print("\n-----------------------------------")
    print(f"Nilai BMI Anda adalah: {bmi:.2f}")
    print(f"Berdasarkan BMI Anda, Anda termasuk dalam kategori **{kategori}**.")
    print("-----------------------------------")


if __name__ == "__main__":
    main()