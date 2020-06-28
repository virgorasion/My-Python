class imajiner:
    def __init__(self,real=0,imajiner=0):
        self.real = real
        self.imaj = imajiner

    def display(self):
        print("{0} + {1}i".format(self.real,self.imaj))

a = imajiner(5,6);
a.display();
