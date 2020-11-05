class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None
        self.prev = None
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def getPrev(self):
        return self.prev
    def setData(self, newdata):
        self.data = newdata
    def setNext(self, new_next):
        self.next = new_next
    def setPrev(self, new_prev):
        self.prev = new_prev

class LinkedList:
    def __init__(self):
        self.head = None
    def isEmpty(self):
        return self.head==None
    def add(self, item):
        curent = self.head
        if curent == None:
            temp = Node(item)
            temp.setNext(self.head)
            temp.setPrev(None)
            self.head = temp
        else:
            temp = Node(item)
            temp.setNext(self.head)
            temp.setPrev(21)
            self.head = temp
    def hapus(self,data):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == data:
                found = True
            else:
                previous = current
                current = current.getNext()
        if not found:
            print("kosong")
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
    def cek(self,item):
        cek = Node(item)
        print(cek.getData())
        print(cek.getNext())
        print(cek.getPrev())
    def size(self):
        curent = self.head
        count = 0
        while curent != None:
            count += 1
            curent = curent.getNext()
        return count
    def showAll(self):
        curent = self.head
        for current in range(self.size()):
            print(curent.getData(), end=" ")
            print("-->", end=" ")
            curent = curent.getPrev()
        
        
mylist = LinkedList()
mylist.add(21)
mylist.add(22)
mylist.add(23)
mylist.cek(22)
# mylist.showAll()