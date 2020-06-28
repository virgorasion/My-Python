# def faktorial(x):
#     hasil = 1
#     for i in range(2, x + 1):
#         hasil *= i
#     return hasil

# print(faktorial(10))

def towerOfHanoi(n, asal, bantuan, tujuan):
    if n == 1:
        print("Pindahkan Lempengan 1 dari {0} ke {1}".format(asal,tujuan))
    else:
        towerOfHanoi(n-1, asal, tujuan, bantuan)
        print("Pindahkan Lempengan {2} dari {0} ke {1}".format(asal,tujuan,n))
        towerOfHanoi(n-1, bantuan, asal, tujuan)
towerOfHanoi(3,"A","B","C")