import random as rand
import time 

data = []
for i in range(10000):
    data.append(rand.randint(1,9999))

start_time = time.time()
def BubbleShort(data, decision=2, short="asc"):
    for i,j in enumerate(range(len(data),0,-1)):
        # print("Iterasi Ke-{0} \tJumlah Iterasi : {1}".format(i+1,j-1))
        if decision == 1:
            for i,x in enumerate(range(len(data)-1,len(data)-j,-1)):
                if short == "asc":
                    if data[x] < data[x-1]:
                        data[x], data[x-1] = data[x-1], data[x]
                elif short == "desc":
                    if data[x] > data[x-1]:
                        data[x], data[x-1] = data[x-1], data[x]
                # print("{0} = {1}".format(i+1,data))
        elif decision == 2:
            for i in range(j-1):
                if short == "asc":
                    if data[i] < data[i+1]:
                        data[i], data[i+1] = data[i+1], data[i]
                elif short == "desc":
                    if data[i] > data[i+1]:
                        data[i], data[i+1] = data[i+1], data[i]
                        # print("{0} = {1}".format(i+1,data))
                urut = urut and False
    # print("Data Terurut =",data)
BubbleShort(data,decision=1)
print("--- %s seconds ---" % round(time.time() - start_time,3))

start_time = time.time()
def ModifiedBubbleShort(data, decision=2, short="asc"):
    for i,j in enumerate(range(len(data),0,-1)):
        # print("Iterasi Ke-{0} \tJumlah Iterasi : {1}".format(i+1,j-1))
        if decision == 1:
            urut = True
            for i,x in enumerate(range(len(data)-1,len(data)-j,-1)):
                if short == "asc":
                    if data[x] < data[x-1]:
                        data[x], data[x-1] = data[x-1], data[x]
                        urut = urut and False
                    else:
                        urut = urut and True
                elif short == "desc":
                    if data[x] > data[x-1]:
                        data[x], data[x-1] = data[x-1], data[x]
                        urut = urut and False
                    else:
                        urut = urut and True
                # print("{0} = {1}".format(i+1,data))
            if urut:
                break
        elif decision == 2:
            for i in range(j-1):
                if short == "asc":
                    if data[i] < data[i+1]:
                        data[i], data[i+1] = data[i+1], data[i]
                        urut = urut and False
                    else:
                        urut = urut and True
                elif short == "desc":
                    if data[i] > data[i+1]:
                        data[i], data[i+1] = data[i+1], data[i]
                        urut = urut and False
                    else:
                        urut = urut and True
                # print("{0} = {1}".format(i+1,data))
            if urut:
                break
    # print("Data Terurut =",data)

# data = [10,2,1,13,15,22,11,45]

ModifiedBubbleShort(data,decision=1)
print("--- %s seconds ---" % round(time.time() - start_time,3))