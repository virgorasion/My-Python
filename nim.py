def elva(size):
    # ./Start Script Nol
    #for untuk atap nol
    for i in range(0, size):
        print("x",end="")
    print()

    #for untuk body nol
    for i in range(0, size - 1):
        print("x",end="")
        for j in range(1, size -1):
            print(" ",end="")
        print("x")

    #for untuk lantai nol
    for i in range(0, size):
        print("x",end="")
    print()
    # ./End Script Nol

    print()

    # ./Start Script Empat
    #for untuk atasan empat
    for i in range(0, int(size/2) ):
        print("x",end="")
        for j in range(0, size -3):
            print(" ",end="")
        print("x")

    #for untuk garis tengah empat
    for i in range(0,size):
        print("x",end="")
    print()

    #for untuk kaki empat
    for i in range(int(size/2)+1, size):
        for j in range(0, size -2):
            print(" ",end="")
        print("x")
    # ./End Script Sembilan

    print()

    # ./Start Script Sembilan
    #for untuk atap nol
    for i in range(0,size):
        print("x",end="")
    print()

    #for untuk body nol
    for i in range(0, int(size/3) - 1):
        print("x",end="")
        for j in range(0, size - 2):
            print(" ",end="")
        print("x")

    #for untuk alas nol
    for i in range(0,size):
        print("x",end="")
    print()

    #for untuk kaki sembilan
    for i in range(int(size/3) + 1, size -1):
        for j in range(0, size -1):
            print(" ",end="")
        print("x")

    #for untuk alas sembilan
    for i in range(0,size):
        print("x",end="")
    print()
    # ./End Script Sembilan

size = int(input("Masukkan Size : "))
elva(size)
