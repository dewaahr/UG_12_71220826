batas=int(input("Masukan angka pembatas:"))
larang=int(input("Masukkan angka yang dilarang:"))

for i in range(batas+1):
    if i==larang:
        continue
    print(i,end=" ")