from Module import Deque as deq

def isPalindrome(katas):
    palindrome =  deq.createDeque()
    for kata in katas:
        deq.addFront(palindrome, kata)

    cek = True
    while deq.size(palindrome) > 1:
        if deq.removeFront(palindrome) == deq.removeRear(palindrome):
            cek = cek and True
        else:
            cek = cek and False
    return cek
for i in range(3):
    kata = input("Masukkan kata : ")
    if isPalindrome(kata):
        print("Ini Kata Palindrom")
        print(isPalindrome(kata))
    else:
        print("Bukan Kata Palindrom")
        print(isPalindrome(kata))
