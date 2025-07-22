nama = input("Masukkan nama mahasiswa: ")
jml = int(input("Masukkan jumlah mata kuliah: "))

total_sks = 0
total_bobot = 0.0

def konversi_nilai(nilai):
    if nilai >= 80:
        return 4.0
    elif nilai >= 75:
        return 3.5
    elif nilai >= 65:
        return 3.0
    elif nilai >= 55:
        return 2.5
    elif nilai >= 45:
        return 2.0
    else:
        return 0.0

print("\n-- Masukkan Data Mata Kuliah --")
for i in range(jml):
    print(f"\nMata kuliah ke-{i+1}")
    nama_matkul = input("Nama mata kuliah: ")
    sks = int(input("SKS: "))
    nilai = float(input("Nilai (0-100): "))

    bobot = konversi_nilai(nilai)
    total_bobot += bobot * sks
    total_sks += sks

ipk = total_bobot / total_sks

# Grade IPK
if ipk >= 3.75:
    grade = "A"
elif ipk >= 3.0:
    grade = "B"
elif ipk >= 2.0:
    grade = "C"
elif ipk >= 1.0:
    grade = "D"
else:
    grade = "E"

print("\n=== HASIL PERHITUNGAN ===")
print(f"Nama Mahasiswa: {nama}")
print(f"Total SKS     : {total_sks}")
print(f"IPK           : {ipk:.2f}")
print(f"Grade         : {grade}")