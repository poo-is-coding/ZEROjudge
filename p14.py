data=[]
try:
    while True:
        imf=input()
        n,m=imf.split()
        n,m=int(n),int(m)
        count=1
        summary=n
        while summary<=m:
            n+=1
            summary+=n
            count+=1
        data.append(count)
except:
    pass
for i in data:
    print(i)