def f(n):
    if n ==1:
        return 1
    else:
        return int((n*(n+1))/2)
def g(n):
    return int((n*(n+1)*(n+2))/6)
data=[]
try:
    while True:
        imf=int(input())
        f1=f(imf)
        g1=g(imf)
        data.append([f1,g1])
except:
    pass

for i in data:
    for k in i:
        print(k,end=" ")
    print()