def iterator(n):
    if n == 1:
        return 7
    elif n == 2:
        return 13
    else:
        return iterator(n-1) + 3


def sigma(n):
    a = 0
    for b in range(1, n+1):
        a += 3*b+4
    c = 5*n
    return a/c


print(iterator(4))
# print(sigma(1))
# print(sigma(2))
# print(sigma(3))
# print(sigma(5))
# print(sigma(100))
