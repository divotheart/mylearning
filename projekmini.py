# gabungan input, variabel, dictionary, perbandingan dan boolean
print("=== Formulir Pendaftaran ===")
nama = input("Masukan Nama Lengkap: ")
umur = int(input("Masukan Umur: "))
alamat = input("Masukan Alamat: ")

data_peserta = {
    "nama": nama,
    "umur": umur,
    "alamat": alamat
}

print("\n=== Data Peserta ===")
print("Nama: ", data_peserta['nama'])
print("Umur: ", data_peserta['umur'])
print("Alamat: ", data_peserta['alamat'])

print("\n=== Terimakasih Telah Mendftar ===")