data = [3, 5, 9, 12, 14, 15, 19]
# Default Insertion Sort
# print("Default InsertionSort")
# for i in range(1,len(data)):
#     key = data[i]
#     print("key =",key)
#     j=i-1
#     while j>=0 and data[j] >= key:
#         # print("j",j)
#         data[j+1] = data[j]
#         j -= 1
#         print(j,"=",data)
#     data[j+1] = key
#     print("Urutan",data,"\n")

# Modif Insertion Sort descending kana
print("Modif Descending InsertionSort")
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
# print("Modif Ascending InsertionSort")
# for luar in range(len(data)-2,-1,-1):
#     key = data[luar]
#     i = luar+1
#     print("Key =",key)
#     while i<=len(data)-1 and key >= data[i]:
#         # print("i",i)
#         data[i-1] = data[i]
#         i += 1
#         print(i,data)    
#     data[i-1] = key
#     print("urutan",data,"\n")
