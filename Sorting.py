def sorting(data):
    for j in range(len(data)):
        for i in range(j+1,len(data)):
            if data[j] > data[i]:
                swap = data[j]
                data[j] = data[i]
                data[i] = swap

data = []
for i in range(5):
    inputBilangan = int(input("Masukkan Bilangan: "))
    data.append(inputBilangan)

sorting(data)
print(data)

