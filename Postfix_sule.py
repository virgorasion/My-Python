import Module.Stack as st

def isValidate(strinfix):
    data = st.stack()
    kurung ={")":"(","}":"{","]":"["}
    for i in strinfix:
        if i in kurung.values():
            st.push(data, i)
        elif i in kurung.keys():
            if st.isEmpty(data):
                return "Kelebihan kurung tutup"
            else:
                a = st.peek(data)
                if a == kurung[i]:
                    st.pop(data)
                else:
                    return "Kurung tutup tidak sama"
    if st.size(data)>0:
        print("Kelebihan kurung buka")
        return False
    else:
        return True
isValidate(())

def in2Post(strinfix):
    operator = {"+":1,"-":2,"*":3,":":4}
    kurungg ={")":"(","}":"{","]":"["}
    dataa = st.stack()
    output = ""
    bagi = []
    temp = ""
    for j in strinfix:
        if j == " ":
            continue
        elif j not in operator.keys() and j not in kurungg.keys() and j not in kurungg.values():
            temp += j
        else:
            if temp != "":
                bagi.append(temp)
                temp=""
            bagi.append(j)
    if temp != "":
        bagi.append(temp)

    for y in bagi:
        if y == "":
            continue
        elif y in kurungg.values():
            st.push(dataa,y)
        elif y in operator.keys():
            if st.size(dataa)!=0:
                p = st.peek(dataa)
                if p not in operator.keys():
                    st.push(dataa,y)
                elif p in operator.keys():  
                    if operator[y] > operator[a]:
                        st.push(dataa,y)
                    elif operator[y] < operator[a]:
                        output += st.pop(dataa)
                        st.push(dataa,y)
            else:
                st.push(dataa,y)

        elif y in kurungg.keys():
            while not st.isEmpty(dataa):
                q = st.pop(dataa)
                if q in operator.keys():
                    output += " " + q
        else:
            output += " " + y
    if st.size(dataa)>0:
        while not st.isEmpty(dataa):
            output += " " + st.pop(dataa)
    return output

in2Post("{[23+56]*[12-2]:[10+20]}")

def evaluatePost(strinfix):
    operatorr = "*:+-"
    dataaa = st.stack()
    bagii = strinfix.split()

    for k in bagii:
        if k not in operatorr:
            st.push(dataaa, int(k))
        elif st.size(dataaa)>1:
            r = st.pop(dataaa)
            t = st.pop(dataaa)

            if k == ":":
                k = "/"
            hasil = eval(" {}{}{} ".format(float(t),k,float(r)))
            st.push(dataaa,float(hasil))

    return st.pop(dataaa)