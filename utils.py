def konversi_suhu(nilai, dari, ke):
    
    # case sensitive
    dari = dari.lower()
    ke = ke.lower()

    # Validasi Input
    valid_units = ['c', 'f', 'k']
    if dari not in valid_units or ke not in valid_units:
        return "Error: Satuan tidak valid. Gunakan 'c', 'f', atau 'k'."

    # Validasi nilai suhu
    if dari == 'k' and nilai < 0:
        return "Error: Suhu Kelvin tidak boleh negatif."

    # Proses Konversi
    if dari == ke:
        return nilai

    # Konversi ke Celsius
    if dari == 'f':
        celsius = (nilai - 32) * 5/9
    elif dari == 'k':
        celsius = nilai - 273.15
    else:
        celsius = nilai

    # Konversi dari Celsius 
    if ke == 'f':
        return (celsius * 9/5) + 32
    elif ke == 'k':
        return celsius + 273.15
    else: # ke == 'c'
        return celsius