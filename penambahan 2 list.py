import Module.Stack as st
import random
x = [2, 4, 2, 5, 1, 2]
y = [2, 2, 4]
z = [2, 2, 4, 51, 2, 5, 2, 1, 2]


def addList(x, y):
    cekX = st.size(x)
    cekY = st.size(y)
    hasil = st.stack()
    if cekX >= cekY:
        for i in range(cekX):
            if i < cekY:
                st.push(hasil, x[i] + y[i])
            else:
                st.push(hasil, x[i])
    else:
        for i in range(cekY):
            if i < cekX:
                st.push(hasil, x[i] + y[i])
            else:
                st.push(hasil, y[i])
    print(hasil)


addList(y, x)
addList(x, z)
