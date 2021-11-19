imf= input()
n,m,k=imf.split()
n,m,k=int(n),int(m),int(k)
space=[[0 for i in range(m)] for k in range(n)]
data=[]
for i in range(k):
    da=input().split()
    data.append(da)
dicar=[[int(data[j][0]),int(data[j][1])] for j in range(k)]
pas=["0" for i in range(k)]







while "0" in pas:
    bombremove=[]
    for l in range(k):
        if pas[l]=="1":
            continue
        space[dicar[l][0]][dicar[l][1]]=1
        dicar[l][0]+=int(data[l][2])
        dicar[l][1]+=int(data[l][3])
    for j in range(k):
        if pas[j]=="1":
            continue
        if dicar[j][0] >= n or dicar[j][1] >= m or dicar[j][0]<0 or dicar[j][1] <0:
            pas[j]="1"
            continue
        if space[dicar[j][0]][dicar[j][1]]==1:
            pas[j]="1"
            bombremove.append([dicar[j][0],dicar[j][1]])
    for q in bombremove:
        space[q[0]][q[1]]=0




#輸出
summary=0
for h in space:
    for i in h:
        summary+=i
print(summary)
