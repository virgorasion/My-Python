class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self, newdata):
        self.data = newdata
    def setNext(self, new_next):
        self.next = new_next

class LinkedList(Node):
    def __init__(self):
        self.head = None
    def isEmpty(self):
        return self.head==None
    def add(self, item):
        curent = self.head
        prev = None
        found = False
        while curent != None and not found:
            if curent.getData() == item:
                found = True
            else:
                prev = curent
                curent = curent.getNext()
        temp = Node(item)
        if prev == None:
            temp.setNext(self.head)
            self.head = temp
        else: # ditautkan antara prev dengan curent
            temp.setNext(curent)
            prev.setNext(temp)
    def size(self):
        curent = self.head
        count = 0
        while curent != None:
            count += 1
            curent = curent.getNext()
        return count
    def showAll(self):
        curent = self.head
        result = "[ "
        for current in range(self.size()):
            print(curent.getData())
            curent = curent.getNext()
        
        
mylist = LinkedList()
mylist.add(6)
mylist.add(8)
mylist.add(20)
mylist.add(19)
mylist.showAll()