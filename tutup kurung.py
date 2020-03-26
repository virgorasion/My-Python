import Module.Stack as st
kata = "{[23+56]*[12-2]:[10+20]]"
stack = st.stack()
con = 0
for cek in kata:
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
    print("Ntaps, Wes Bener")
elif not st.isEmpty(stack) and con == 0:
    print("Kelebihan Kurung Buka")
