print("\n=== MINI PROJECT: KALKULATOR SEDERHANA ===")

class Kalkulator:
    def __init__(self):
        self.history = []
    
    def tambah(self, a, b):
        hasil = a + b
        self.history.append(f"{a} + {b} = {hasil}")
        return hasil
    
    def kurang(self, a, b):
        hasil = a - b
        self.history.append(f"{a} - {b} = {hasil}")
        return hasil
    
    def kali(self, a, b):
        hasil = a * b
        self.history.append(f"{a} * {b} = {hasil}")
        return hasil
    
    def bagi(self, a, b):
        if b == 0:
            return "Error: Tidak bisa dibagi nol"
        hasil = a / b
        self.history.append(f"{a} / {b} = {hasil}")
        return hasil
    
    def lihat_history(self):
        return self.history

calc = Kalkulator()
print(f"5 + 3 = {calc.tambah(5, 3)}")
print(f"10 - 4 = {calc.kurang(10, 4)}")
print(f"6 * 7 = {calc.kali(6, 7)}")
print(f"15 / 3 = {calc.bagi(15, 3)}")
print(f"History: {calc.lihat_history()}")

print("\n=== SELESAI ===")
print("Horeeee! Kamu pintar!")