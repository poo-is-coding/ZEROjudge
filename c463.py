from sys import stdin
from copy import deepcopy
rd = stdin.readline
n = int(rd())
tree=[[] for i in range(n+1)]
momind = [0 for i in range(n+1)]
h=0
rou=[]
rou2=[]
height = [-1 for i in range(n+1)]
for i in range(1,n+1):
    imf = [int(_) for _ in rd().split()]
    if imf[0] == 0:
        height[i]=0
        rou.append(i)
    else:
        for j in range(1,imf[0]+1):
            tree[i].append(imf[j])
            momind[imf[j]] = i

root=momind[1::].index(0)+1

while len(rou)!=1 or rou[0]!=root:
    h+=1
    for i in rou:
        if momind[i]==0:
            continue
        height[momind[i]]=h
        if momind[i] not in rou2:
            rou2.append(momind[i])
    rou=deepcopy(rou2)
    rou2=[]
h=0
for i in height[1::]:
    h+=i
print(root)
print(h)

                
