import Module.Stack as st
stack = st.stack()
decimal = 64
while decimal != 0:
    hasil = decimal % 2
    st.push(stack, hasil)
    decimal = decimal // 2
for i in range(len(stack)):
    print(st.pop(stack), end="")
