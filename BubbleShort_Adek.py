def bubbleSort(a, adesc="asc", data="1"):
    print('data = ', a)
    count=0
    if adesc == 'asc' and data == '1':
        for j in range(len(a)-1,-1,-1):
            count=count+1
            print ('Iterasi ke-', count,':')
            urut = True
            for i in range(j):
                if a[i]>a[i+1]:
                    temp=a[i]
                    a[i]=a[i+1]
                    a[i+1]=temp
                    urut = urut and False
                else:
                    urut = urut and True
                print(urut)
                print(a)
            if urut:
                break
        print('Data urut-',a)
a = [45,10,2,1,13,15,22,11]
res = bubbleSort(a=a)