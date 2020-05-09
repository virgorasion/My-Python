def createDeque():
    d = []
    return d
def addFront(d,data):
    d.insert(0,data)
    return d
def addRear(d,data):
    d.append(data)
    return d
def removeRear(d):
    data = d.pop()
    return data
def removeFront(d):
    data = d.pop(0)
    return data
def isEmpty(d):
    return d==[]
def size(d):
    return len(d)