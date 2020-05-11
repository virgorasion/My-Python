data = [1,11,7,5,10]
# Default Insertion Sort
# for i in range(1,len(data)):
#     key = data[i]
#     print(key)
#     j=i-1
#     while j>=0 and data[j] >= key:
#         # print("j",j)
#         data[j+1] = data[j]
#         j -= 1
#         print(j,"=",data)
#     data[j+1] = key
#     print(data)

# Modif Insertion Sort descending kanan
for luar in range(len(data)-2,-1,-1):
    key = data[luar]
    i = luar+1
    print("Key =",key)
    while i<=len(data)-1 and key <= data[i]:
        # print("i",i)
        data[i-1] = data[i]
        i += 1
        print(i,data)    
    data[i-1] = key
    print("urutan",data,"\n")

# Modif Insertion Sort ascending kanan
for luar in range(len(data)-2,-1,-1):
    key = data[luar]
    i = luar+1
    print("Key =",key)
    while i<=len(data)-1 and key >= data[i]:
        # print("i",i)
        data[i-1] = data[i]
        i += 1
        print(i,data)    
    data[i-1] = key
    print("urutan",data,"\n")
