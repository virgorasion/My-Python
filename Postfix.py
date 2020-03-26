import Module.Stack as st


def in2Post(strInfix):
    operator = ["+", "-", "*", ":", "^"]
    kurung = {"{": "}", "[": "]", "(": ")"}
    stack = st.stack()
    result = ""
    for i in strInfix:
        if i in kurung.keys():
            st.push(stack, i)
        elif i in operator:
            st.push(stack, i)
            result += " "
        elif i not in kurung.values():
            result += i
        else:
            while not st.isEmpty(stack):
                temp = st.pop(stack)
                if temp in operator:
                    result += " "+temp
                elif st.isEmpty(stack):
                    break
    if not st.isEmpty(stack):
        temp = st.pop(strInfix)
        if temp in operator:
            result += temp + " "
    return(result)


def evaluatePost(strPostfix):
    stack = st.stack()
    data = strPostfix.split()
    for i in data:
        if i.isdigit():
            st.push(stack, i)
        else:
            if i == ":":
                i = "/"
            op1 = st.pop(stack)
            op2 = st.pop(stack)
            st.push(stack, str(eval(op2 + i + op1)))
    return(stack)


def isValidate(strInfix):
    stack = st.stack()
    con = 0
    for cek in strInfix:
        if cek == "(" or cek == "{" or cek == "[":
            st.push(stack, cek)
        elif cek == ")" or cek == "}" or cek == "]":
            if st.isEmpty(stack):
                print("Kelebihan Kurung Tutup")
                con = 1
                break
            elif st.peek(stack) == "(" and cek == ")" or st.peek(stack) == "{" and cek == "}" or st.peek(stack) == "[" and cek == "]":
                st.pop(stack)
            else:
                print(st.peek(stack), cek, "Kesalahan Kurung Tutup")
                con = 1
                break
    if st.isEmpty(stack) and con == 0:
        return True
    elif not st.isEmpty(stack) and con == 0:
        print("Kelebihan Kurung Buka")


strInfix = "{[23+56] *[12- 2]:[10 +20]}"
if isValidate(strInfix):
    strPostFix = in2Post(strInfix)
    print('Ekspressi Matematika PostFix = {0}'.format(strPostFix))
    print('Hasil Evaluasi = {0}'.format(evaluatePost(strPostFix)))
else:
    print('Tidak dapat dioperasikan')
