from sys import stdin
rd = stdin.readline
n,m = [int(_) for _ in rd().split()]
q=[0 for i in range(n)]
for t in range(m):
    l,r,i = [int(_) for _ in rd().split()]
    l-=1
    for j in range(l,r):
        q[j]+=i
oper=[int(_) for _ in rd().split()]
q.sort()
oper.sort()
summary=0
for i in range(n):
    summary+=q[n-1-i]*oper[i]
print(summary)