import Module.Stack as st

# Constanta
kurung = {"}": "{", "]": "[", ")": "("}
operator = {"+":1,"-":1,"*":2,":":2,"^":3}

def in2Post(strInfix):
    stack = st.stack()
    result = ""
    # Loop each strInfix
    for i in strInfix:
        # to skip iteration if found space
        if i == " ":
            continue
        # check if i is a number
        elif i.isdigit():
            result += i
        # check if i is kurung buka
        elif i in kurung.values():
            st.push(stack,i)
        # check if i operator
        elif i in operator.keys():
            # to separate each number
            result += " "
            # loop if stack is not empty and check level of operator
            while not st.isEmpty(stack) and st.compareOperator(operator, stack, i):
                # pop operator if current operator more higher level 
                result += st.pop(stack)+" "
            # to push current operator after poping lower level operator
            st.push(stack,i)
        # to catch kurung tutup
        else:
            # loop if stack is not empty and check if kurung buka == kurung tutup
            while not st.isEmpty(stack) and st.dataCheck(kurung,st.peek(stack), i):
                # poping everything in the kurung :v
                result += " "+st.pop(stack)
            # last, pop kurung buka
            st.pop(stack)
    # check if stack is not empty
    while not st.isEmpty(stack):
        # pop everything remaining from the stack
        result += " "+st.pop(stack)
    return(result)


def evaluatePost(strPostfix):
    stack = st.stack()
    data = strPostfix.split()
    for i in data:
        # check is i a number
        if i.isdigit():
            # then push to stack
            st.push(stack, i)
        # is not a number then ...
        else:
            # change : to / to eval the number
            if i == ":":
                i = "/"
            op1 = st.pop(stack)
            op2 = st.pop(stack)
            # to calculate the number then convert to str and push to stack
            st.push(stack, str(eval(op2 + i + op1)))
    return(stack)


def isValidate(strInfix):
    stack = st.stack()
    con = 0
    for cek in strInfix:
        if cek in kurung.values():
            st.push(stack, cek)
        elif cek in kurung.keys():
            if st.isEmpty(stack):
                print("Kelebihan Kurung Tutup")
                con = 1
                break
            elif not st.dataCheck(kurung,st.peek(stack),cek):
                st.pop(stack)
            else:
                print(st.peek(stack), cek, "Kesalahan Kurung Tutup")
                con = 1
                break
    if st.isEmpty(stack) and con == 0:
        return True
    elif not st.isEmpty(stack) and con == 0:
        print("Kelebihan Kurung Buka")


strInfix = "( 1 + 2 ) / ( 3 - 4 )"
if isValidate(strInfix):
    strPostFix = in2Post(strInfix)
    print('Ekspressi Matematika PostFix = {0}'.format(strPostFix))
    print('Hasil Evaluasi = {0}'.format(evaluatePost(strPostFix)))
else:
    print('Tidak dapat dioperasikan')
