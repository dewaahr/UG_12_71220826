awal=int(input("Masukan awal deret:"))
akhir=int(input('Masukan akhir deret:'))
for i in range(awal,akhir):
    if i%2==1  and i%3!=0 and i%6!=0:
        print(i, end=' ')