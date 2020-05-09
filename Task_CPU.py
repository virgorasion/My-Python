import Module.Queue as q

countTask = 4
data = q.createQueue()
process = 3
i = 0
for i in range(countTask):
    temp = q.createQueue()
    temp.append(input("Nama Proses Ke-{0} : ".format(i+1)))
    temp.append(int(input("Waktu Proses Ke-{0} : ".format(i+1))))
    q.enqueue(data,temp)

print("waktu proses CPU = {0}".format(process))
print("Antrian Proses beserta waktunya = {0}".format(data))
while not q.isEmpty(data):
    i+=1
    print("Iterasi ke-{0}:".format(i))
    if q.first(data)[1] > 0:
        q.first(data)[1] -= process
        if q.first(data)[1] < 1:
            print("\tProses {} telah selesai diproses".format(q.first(data)[0]))
            q.dequeue(data)
            print("\tData Proses yang tersisa : {0}".format(data))
        else:
            print("\tProses {0} sedang diproses, dan sisa waktu proses {0} = {1}".format(q.first(data)[0],q.first(data)[1]))
            q.enqueue(data,q.dequeue(data))
            print("\tData Proses yang tersisa : {0}".format(data))
