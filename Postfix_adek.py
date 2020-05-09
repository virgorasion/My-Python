def isValidate(strInfix):
    stack = st.stack()
    kurung = {')': '(', '}': '{', ']': '['}
    for i in strInfix:
        if i in kurung.values():
            st.push(stack, i)
        elif i in kurung.keys():
            if st.isEmpty(stack):
                return 'kelebihan kurung tutup'
            else:
                a = st.peek(stack)
                if a == kurung[i]:
                    st.pop(stack)
                else:
                    return 'kurung tidak sama'
    if st.size(stack) > 0:
        print('kelebihan kurung buka')
    else:
        return True


def compare(peek, i):
    tingkatan = {'+': 1, '-': 1, '*': 2, ':': 2, '^': 3}
    try:
        a = tingkatan[i]
        b = tingkatan[peek]
        return True if a <= b else False
    except KeyError:
        return False


def in2Post(strInfix):
    stack = st.stack()
    tingkatan = {'+': 1, '-': 1, '*': 2, ':': 2, '^': 3}
    operator = ["+", "-", ":", "*", "^"]
    kurung = {'{': '}', '[': ']', '(': ')'}
    angka = '0123456789'
    postfix = []
    temp = ''

    for i in range(len(strInfix)):
        if strInfix == ' ': continue
        elif strInfix[i] in angka:
            temp += strInfix[i]
        elif strInfix[i] in kurung.keys():
            if temp != '':
                postfix.append(temp)
                temp = ''
            st.push(stack, strInfix[i])
        elif strInfix[i] in kurung.values():
            if temp != '':
                postfix.append(temp)
                temp = ''
                j = st.pop(stack)
                while j != kurung.keys():
                    postfix.append(j)
                    j = st.pop(stack)
        else:
            if temp != '':
                postfix.append(temp)
                temp = ''
                print(st.peek(stack), "asdasd")

            while(not st.isEmpty(stack)) and compare(st.peek(stack), strInfix[i]) or not st.isEmpty(stack) and (kurung.values()):
                    postfix.append(st.pop(stack))
                st.push(stack, strInfix[i])
    while not st.isEmpty(stack):
        postfix.append(st.pop(stack))
    print('isi postfix ', str(postfix))
