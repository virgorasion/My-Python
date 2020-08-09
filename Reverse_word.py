import Module.Stack as st
def reverse(kata):
    a = st.stack()
    n = len(kata)
    for i in range (0,n,1):
        st.push(a,kata[i])
    hasil = ""
    for i in range (0,n,1):
        hasil+=st.pop(a)
    print(hasil)

reverse('kasur rusak')
