def konversi_suhu(nilai, satuan):
    """
    Mengonversi suhu dari Celsius ke Fahrenheit atau sebaliknya.
    
    Parameter:
    nilai (float): Nilai suhu yang akan dikonversi.
    satuan (str): Satuan dari suhu input, 'C' untuk Celsius atau 'F' untuk Fahrenheit.
    
    Mengembalikan:
    float: Suhu yang sudah dikonversi.
    """
    if satuan == 'C' or satuan == 'c':
        # Konversi Celsius ke Fahrenheit
        return (nilai * 9/5) + 32 +"F"
    elif satuan == 'F' or satuan == 'f':
        # Konversi Fahrenheit ke Celsius
        return (nilai - 32) * 5/9 +"C"
    else:
        return "Satuan tidak valid, silakan masukkan 'C' atau 'F'."

# Input dari pengguna
nilai = float(input("Masukkan nilai suhu: "))
satuan = input("Masukkan satuan suhu (C untuk Celsius, F untuk Fahrenheit): ").upper()

# Pemanggilan fungsi dan menampilkan hasil
hasil = konversi_suhu(nilai, satuan)
print(f"Suhu setelah konversi: {hasil}")
