masuk=input("Masukan Nama:")
# print(len(masuk))
x=0
for i in range(len(masuk)):
    x=x+1
    print(masuk[:x])
for i in range(len(masuk)):
    x=x-1
    print(masuk[:x])