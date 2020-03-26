import Module.Stack as st
kata = "(){}[]"
stack = st.stack()
pencarian = {')': '(', '}': '{', ']': '['}
# con = 0
# print(pencarian.keys())
# for cek in kata:
#     if cek == pencarian.keys():
#         st.push(stack, cek)
print(pencarian['}'])
