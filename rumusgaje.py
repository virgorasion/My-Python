def sigma(n):
    a = 0
    for b in range(1, n+1):
        a += 3*b+4
    c = 5*n
    return a/c

print(sigma(1))
print(sigma(2))
print(sigma(3))
print(sigma(5))
print(sigma(100))
