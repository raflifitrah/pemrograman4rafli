bil1 = int(input("masukkan bilangan 1: "))
bil2 = int(input("masukkan bilangan 2: "))
bil3 = int(input("masukkan bilangan 3: "))

if bil1 > bil2 and bil3 > bil2:
    print(f"angka {bil2} lebih kecil dari angka {bil1} dan {bil3}")
elif bil2 > bil1 and bil3 > bil1:
     print(f"angka {bil1} lebih kecil dari angka {bil2} dan {bil3}")
elif bil1 > bil3 and bil2 > bil3:
    print(f"angka {bil3} lebih kecil dari angka {bil1} dan {bil2}")
else:
    print("angka yang anda masukkan tidak valid")