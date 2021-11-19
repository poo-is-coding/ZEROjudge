"""
測資一
2 3 3
30 23 23
5 25 3
0 0
0 1
0 2
測資二
3 4 5
500 400 800 200
500 400 100 600
450 420 800 790
0 0 0 
0 1 2
0 2 2
2 1 2
1 1 1
"""
#流量Q[伺服器][城市] 輸入
n,m,k=input().split()
n,m,k=int(n),int(m),int(k)
Q=[0 for i in range(n)]
for p in range(n):
    Q[p]=input().split()
for i in range(n):
    for j in range(m):
        Q[i][j]=int(Q[i][j])
#方案輸入
record=0
for l in range(k):
    cost=0
    cityQ=[[0 for i in range(m)]for j in range(m)]
    c=input().split()
    c=[int(j) for j in c]
#製造一個二維陣列cityQ[i][j]代表第i個城市有多少流量要send給第j個城市
    for i in range(n):
        for j in range(m):
            cityQ[c[i]][j]+=Q[i][j]
    for p in range(m):
        for q in range(m):
            if p==q:
                cost+=cityQ[p][q]
            else:
                if cityQ[p][q]>1000:
                    cost+=2*(cityQ[p][q]-1000)+3000
                else:
                    cost+=3*cityQ[p][q]
    if record==0:
        record=cost
    else:
        if cost<record:
            record=cost
print(record)      

"""
理解錯誤的笑話(理解成每個城市收到的流量都要合併)

    for i in range(n):
        for j in range(m):
            if j==c[i]:
                selfsteady[j]+=Q[i][j]
            else:
                steady[j]+=Q[i][j]
    for h in selfsteady:
        cost+=h
    for t in steady:
        if t>1000:
            cost+=2*(t-1000)+3000
        else:
            cost+=3*t
    print("cost=",cost)
    print("selfsteady=",selfsteady)
    print("steady=",steady)

    if record==0:
        record=cost
    else:
        if cost<record:
            record=cost
print(record)

"""