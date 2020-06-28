data = [5,2,1,2,4,5,3,2,7,5,8,8,5,3,2,4,6]

def seqSearch(data,value):
    position = []
    length = len(data)
    for i in range(len(data)):
        if value == data[i]:
            position.append(i)
    if position == []:
        position = "Data tidak ada"
    return position,length
[hasil,jumlahIterasi] = seqSearch(data,0)
print("Posisi Data =",hasil)
print("Jumlah Iterasi =",jumlahIterasi)