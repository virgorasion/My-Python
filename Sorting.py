def sorting(data):
    swap = True
    for i,j in enumerate(range(len(data)-1,0,-1)):
        swap = False
        print("Iterasi Ke-{0} \tJumlah Iterasi : {1}".format(i+1,j))
        for i in range(j):
            if data[i] > data[i+1]:
                swap = True
                data[i], data[i+1] = data[i+1], data[i]
            print("{0} = {1}".format(i+1,data))
        print()
    print("Data Terurut =",data)

data = [10,230,523,79,41]
sorting(data)

