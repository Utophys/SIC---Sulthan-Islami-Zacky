from utils import konversi_suhu

if __name__ == "__main__":
    print("=== KONVERSI SUHU ===")

    # Get user input
    while True:
        try:
            nilai = float(input("Masukkan nilai suhu: "))
            break
        except ValueError:
            print("Input tidak valid. Harap masukkan angka.")

    dari = input("Dari satuan (C/F/K): ").strip()
    ke = input("Ke satuan (C/F/K): ").strip()

    # Panggil fungsi konversi
    hasil_konversi = konversi_suhu(nilai, dari, ke)

    # Tampilkan hasil
    if isinstance(hasil_konversi, str):
        print(hasil_konversi)  # Ini adalah pesan error
    else:
        # Format output dengan satuan yang benar
        def get_symbol(unit):
            if unit.lower() == 'c': return '°C'
            if unit.lower() == 'f': return '°F'
            if unit.lower() == 'k': return '°K'
            return ''
            
        simbol_dari = get_symbol(dari)
        simbol_ke = get_symbol(ke)
        
        # Format nilai_asal untuk tampilan
        nilai_asal_str = f"{nilai}{simbol_dari}"
        
        # Format hasil konversi dengan satu desimal
        hasil_str = f"{hasil_konversi:.1f}{simbol_ke}"
        
        print(f"Hasil: {nilai_asal_str} = {hasil_str}")