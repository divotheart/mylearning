# Latihan input, variabel, dan operator perbandingan

# Input data dari user
nama = (input("Masukan Nama: "))
tahun_lahir = int(input("Masukan Tahun Lahir: "))

# hitung umur
tahun_sekarang = 2024
umur = tahun_sekarang - tahun_lahir

# cek status 
if umur >= 17:
    status = "Dewasa"
else:
    status = "Anak-anak"
print("Status: ", status)

# output hasil
print(f"\nHalo! {nama}, Umur kamu, {umur}, Tahun")
print(f"Status: {status}")