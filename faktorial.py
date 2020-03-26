s = st.stack()


def faktor(n):
    for i in range(1, n+1):
        if n % i == 0:
            st.push(s, i)
    print(s)


faktor(21)
