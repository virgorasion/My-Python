def sorting(data):
    for j in range(len(data)):
        for i in range(j+1,len(data)):
            if data[j] > data[i]:
                swap = data[j]
                data[j] = data[i]
                data[i] = swap
                

data = []
for i in range(10):
    inputan = int(input("Masukkan Bilangan: "))
    data.append(inputan)
    
print("Data Awal:", data)
sorting(data)
print("Data Akhir:",data)
print("Nilai Tengahnya Adalah:",data[4],"dan",data[5])
hasil = (data[4] + data[5]) / 2
print("Hasil Nilai Tengahnya Adalah:",float(hasil))
