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

q = createQueue()
enqueue(q,8)
enqueue(q,dequeue(q))
enqueue(q,dequeue(q))
dequeue(q)
print(q)