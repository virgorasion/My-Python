inpt = int(input("Masukkan Angka: "))
iterasi = 2
prima = st.stack()
bukan = st.stack()
while iterasi != inpt:
    for i in range(2, iterasi):
        if iterasi % i == 0:
            if iterasi % 2 == 1:
                st.push(bukan, iterasi)
            break
    else:
        st.push(prima, iterasi)
    iterasi = iterasi + 1
print("Bilangan Prima", prima)
print("Bilangan Bukan Prima", bukan)
