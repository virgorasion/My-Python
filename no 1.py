def ganjil(n):
    ganjilprima=[]
    ganjilnotprima=[]
    for i in range (1,n,2):
        if i == 1:
            ganjilnotprima.append(i)
        else:
            prime = 0
            for j in range (1,i):
                if i % j == 0:
                    prime += 1
            if prime == 1:
                ganjilprima.append(i)
            else:
                ganjilnotprima.append(i)
    return ganjilprima, ganjilnotprima

prima, bukanprima = ganjil(20)
print ("ganjil prima =", prima)
print ("ganjil bukan prima=", bukanprima)

