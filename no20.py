def createQueue():
    q = []
    return (q)

def enqueue(q, data):
    q.insert(0, data)
    return(q)

def dequeue(q):
    data = q.pop()
    return(data)

def isEmpty(q):
    return (q == [])

def size(q):
    return (len(q))

def first(q):
    return q[-1]

def insert(iterasi):
    data = {}
    for i in range(iterasi):
        input_nama = input("Nama Proses: ")
        # Create child dict
        data = createQueue()
        data.enqueue(data,input("Lama Waktu Yang Dibutuhkan = "))
        data.enqueue(data,input("Resource Sharing [A-B-C] = "))
        data.enqueue(data, 0)
        # Add child dict into data
        data[input_nama] = data
    return data  # return (dict)

print(insert(3))
    