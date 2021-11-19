from copy import deepcopy
data=input()
n,k=data.split()
n,k = int(n),int(k)
data=input().split()
templi=[]
li=[]
for j in data:
    if j not in templi:
        templi.append(j)
    elif j in templi:
        li.append(templi[:])
        templi=[]
        templi.append(j)
else:
    li.append(templi[:])
liraw=deepcopy(li)

for q in range(len(li)):
        if q == 0:
            if li[q+1][0] not in li[q]:
                li[q].append(li[q+1][0])
        elif q == len(li)-1:
            if li[q-1][-1] not in li[q]:
                li[q].insert(0,li[q-1][-1])
        else :
            if li[q+1][0] not in li[q]:
                li[q].append(li[q+1][0])
            if li[q-1][-1] not in li[q]:
                li[q].insert(0,li[q-1][-1])
for j in range(len(li)):
    if j==0:
        if liraw[j][-1]!= liraw[j+1][0]:
            if len(li[j])>len(li[j+1]):
                li[j+1].pop(0)
            else:
                li[j].pop(-1)
    elif j==len(li)-1:
        if liraw[j][0]!= liraw[j-1][-1]:
            if len(li[j-1])>len(li[j]):
                li[j].pop(0)
            else:
                li[j-1].pop(-1)
    else:
        if liraw[j][-1]!= liraw[j+1][0]:
            if len(li[j])>len(li[j+1]):
                li[j+1].pop(0)
            else:
                li[j].pop(-1)

li=[len(i) for i in li]
me=0
if len(li) > k:
    for i in range(k):
        me+=max(li)
        li.remove(max(li))
else:
    me=len(data)
print(me)