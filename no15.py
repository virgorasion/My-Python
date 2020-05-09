def stack():
    s = []
    return(s)


def push(s, data):
    s.append(data)


def pop(s):
    data = s.pop()
    return(data)


def peek(s):
    return(s[-1])


def isEmpty(s):
    return(s == [])


def size(s):
    return(len(s))


stack1=[45, 30, 11, 10, 8, 4]
stack2=[87, 56, 51, 40, 38, 25, 18, 12, 7, 5]
# print(sortStack(stack1,stack2)), maka hasil eksekusi adalah
# [4, 5, 7, 8, 10, 11, 12, 18, 25, 30, 38, 40, 45, 51, 56, 87]
# [4, 5, 7, 8, 10, 11, 12, 18, 25, 30, 38, 40, 45, 51, 56, 87]
# [4, 5, 7, 8, 10, 11, 12, 18, 25, 30, 38, 40, 45, 51, 56, 87]

def sortStack(stack1,stack2):
    hasil = stack()
    if size(stack1) > size(stack2):
        while not isEmpty(stack2):
            if peek(stack1) < peek(stack2) and not isEmpty(stack2):
                push(hasil, pop(stack1))
            else:
                push(hasil, pop(stack2))
        else:
            while not isEmpty(stack1):
                push(hasil, pop(stack1))
    else:
        while not isEmpty(stack1):
            if peek(stack1) < peek(stack2) and not isEmpty(stack1):
                push(hasil, pop(stack1))
            else:
                push(hasil, pop(stack2))
        else:
            while not isEmpty(stack2):
                push(hasil, pop(stack2))
    print(hasil)
        
sortStack(stack1,stack2)
