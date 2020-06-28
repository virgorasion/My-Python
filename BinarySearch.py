def binarySearch(listData, data):
    first = 0
    last = len(listData) - 1
    position = []
    count = 0
    cek = ""
    while first <= last:
        midpoint = (first + last) // 2
        print(midpoint, "mid", listData[midpoint])
        print(first,last,"iki")
        if listData[midpoint] == data:
            print(listData[midpoint], data, midpoint ,"a")
            if position == [] or position[-1] != midpoint:
                position.append(midpoint)
            count += 1
            if data < listData[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
        elif data < listData[midpoint]:
            last = midpoint - 1
            print("salah", midpoint)
        elif data > listData[midpoint]:
            first = midpoint + 1
    if position == []:
        position = "Data tidak ada"
    return position,count

a=[4,6,10,34,40,56,56,56,78,99]
[hasil,jumlah] = binarySearch(a,56)
print("Posisi Data =",hasil)
print("Jumlah Iterasi =",jumlah)