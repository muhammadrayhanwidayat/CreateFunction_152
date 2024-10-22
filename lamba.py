import math#library untuk operasi matematika

# Fungsi lambda untuk menghitung luas lingkaran
luas_lingkaran = lambda r: math.pi * r**2
#lambda r : Bagian ini mendefinisikan fungsi anonim yang menerima satu parameter, yaitu r (jari-jari lingkaran).
#math.pi * r**2: Bagian ini adalah ekspresi yang dievaluasi dan dikembalikan sebagai hasil dari fungsi. 
# Ini adalah rumus untuk menghitung luas lingkaran (π * r²).

# memasukan jari-jari lingkaran dari pengguna dan mengkonvertnya ke float
nilai = float(input("Masukkan jari-jari lingkaran: "))

# Menghitung dan menampilkan luas lingkaran
print(f"Luas lingkaran dengan jari-jari {nilai} adalah {luas_lingkaran(nilai)}")

