n=int(input())
data=input().split()
data=[int(i) for i in data]
L=0
R=len(data)-1
sumall=0
if L==R:
    print(data[0])
else:
    mini=data[0]
    m=0
    for j in data:
        if j<mini:
            mini=j
            m=data.index(mini)
        sumall+=j
    if m != L and m != R:
        if m>=int(len(data)):
            sumr=sum(data[m+1:])
            suml=sumall-sumr-mini
        elif m<int(len(data)):
            suml=sum(data[:m])
            sumr=sumall-suml-mini
    elif m == L:
        suml=0
        sumr=sumall-mini
    elif m==R:
        sumr=0
        suml=sumall-mini
    if suml>sumr:
        data=data[:m]
        sumall=suml
    else:
        data=data[m+1:]
        sumall=sumr
while True:
    L=0
    R=len(data)-1
    mini=data[0]
    if L==R:
        print(mini)
        break
    else:
        mini=min(data)
        m=data.index(mini)
        if m != L and m != R:
            if m>=int(len(data)):
                sumr=sum(data[m+1:])
                suml=sumall-sumr-mini
            elif m<int(len(data)):
                suml=sum(data[:m])
                sumr=sumall-suml-mini
        elif m == L:
            suml=0
            sumr=sumall-mini
        elif m==R:
            sumr=0
            suml=sumall-mini
        if suml>sumr:
            data=data[:m]
            sumall=suml
        else:
            data=data[m+1:]
            sumall=sumr
