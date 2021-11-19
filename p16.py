putout=[]
try:
    while True:
        data=list(input())
        ordli=[]
        ordli1=[]
        count=[]
        if data == [""]:
            putout.append("yes !")
        else:
            for i in data:
                ordli.append(ord(i))
            for j in range(len(ordli)):
                if (64<ordli[j]<90) or (49<ordli[j]<58):
                    ordli1.append(ordli[j])
                elif 96<ordli[j]<123:
                    ordli[j]-=32
                    ordli1.append(ordli[j])
                else:
                    continue
            for m in ordli1:
                if m not in count:
                    count.append(m)
                elif m in count:
                    count.remove(m)
            if len(ordli1)%2 == 1:
                if len(count) == 1:
                    putout.append("yes !")
                else:
                    putout.append("no...")
                    
            elif len(ordli1)%2 == 0:
                if len(count)==0:
                    putout.append("yes !")
                else:
                    putout.append("no...")
except:
    pass
for i in putout:
    print(i)
