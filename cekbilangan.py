while True:
    angka = int(input("masukkan angka: "))

    if angka % 2 == 0:
        print(f"{angka} adalah bilangan genap")
    else:
        print(f"{angka} adalah bilangan ganjil")

    stop = input("mau main lagi? (y/n): ")
    if stop.lower() == 'n':
        print("okeii makasih udah mampir!")
        break
