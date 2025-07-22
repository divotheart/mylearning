import random
import time

print("=== SELAMAT DATANG DI MINI GAME DIVA! ===\n")
nama = input("masukkan nama kamu dulu atuh: ").title()
print(f"\nhalo {nama}, siap-siap main game dan belajar bareng python ya!\n")

time.sleep(3)

karakter = ["print", "variable", "loop", "function", "string"]
karakter_rahasia = random.choice(karakter)
clue = {
    "print": "aku digunakan untuk menampilkan sesuatu di layar...",
    "variable": "aku tempat menyimpan data, bisa angka, teks, dll...",
    "loop": "aku bisa mengulang-ngulang sesuatu terus-menerus...",
    "function": "aku bagian kode yang bisa dipanggil berkali-kali...",
    "string": "aku tipe data berisi huruf, bisa diapit tanda kutip..."
}

print("aku punya satu karakter rahasia dari dunia Python...")
print("clue-nya:")
print(clue[karakter_rahasia])
tebakan = input("\ncoba tebak karakter python yang kumaksud: ").lower()

if tebakan == karakter_rahasia:
    print("\n KEREN! kamu bener banget! kamu mulai jadi master python nih!")
else:
    print(f"\n YAAAHH! jawabannya adalah '{karakter_rahasia}'. tapi tenang, kamu tetap hebat!")