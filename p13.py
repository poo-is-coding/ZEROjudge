

def face(n):
    spadd=1+n*(n-1)*0.5
    return spadd

def space(k):
    summary = 1
    for i in range(1,k+1):
        summary += face(i)
    return summary
data=[]
try:
    while True:
        imf=int(input())
        imf=int(space(imf))
        data.append(imf)
except:
    pass

for i in data:
    print(i)
