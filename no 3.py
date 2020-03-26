def listgaje(n,m):
    data=[]
    if len(n) > len(m):
        for i in range(len(n)):
            if i < len(m):
                data.append(n[i]+m[i])
            else:
                data.append(n[i])
        return data
    elif len(n) < len(m):
        for i in range(len(m)):
            if i < len(n):
                data.append(n[i]+m[i])
            else:
                data.append(m[i])
        return data
    else:
        for i in range(len(n)):
            data.append(n[i]+m[i])
        return data

x=[2,1,5,6]
y=[6,7]
z=[3,7,9,0,2,4,6,2]
print (listgaje(x,y))
print (listgaje(x,z))
