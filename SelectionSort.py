data = [10,3,9,1,2]
# for luar in range(len(data)-1):
#     flag = luar
#     for dalam in range(luar+1,len(data)):
#         if data[flag] > data[dalam]:
#             flag = dalam
#     data[luar],data[flag] = data[flag],data[luar]
#     print(data)

# Modified 
# sort = "max"
# for luar in range(len(data)-1,0,-1):
#     flag = luar
#     for dalam in range(luar-1,-1,-1):
#         if data[flag] < data[dalam]:
#             flag = dalam
#     data[luar],data[flag] = data[flag],data[luar]
#     print(data)

# sort = "min"
# for luar in range(len(data)-1,0,-1):
#     flag = luar
#     for dalam in range(luar-1,-1,-1):
#         if data[flag] > data[dalam]:
#             flag = dalam
#     data[luar],data[flag] = data[flag],data[luar]
#     print(data)

sort = "minmax"
for i,luar in enumerate(range(len(data)-1,0,-1)):
    bigFlag = luar
    lowFlag = len(data)-luar-1
    urut = True
    print("Iterasi ke -",i)
    for minimal in range(len(data)-luar,len(data)):
        if data[lowFlag] > data[minimal]:
            lowFlag = minimal
    data[len(data)-luar-1],data[lowFlag] = data[lowFlag],data[len(data)-luar-1]
    print("data Minimal =",data)
    for maximal in range(luar-1,-1,-1):
        if data[bigFlag] < data[maximal]:
            bigFlag = maximal
    data[luar],data[bigFlag] = data[bigFlag],data[luar]
    print("data Maximal =",data)
    for cek in range(len(data)-1):
        if data[cek] < data[cek+1]:
            urut = urut and True
        else:
            urut = urut and False
    if urut:
        break
