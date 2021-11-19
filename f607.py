"""
測資
I:
3 7
2 2
3 1
5 3
O:
14
"""
#處理輸入
from sys import stdin
import bisect
n,l=input().split()
n,l=int(n),int(l)
sli=[0,l]
rd=stdin.readline
cut={}
for j in range(n):
    u,v=rd().split()
    u,v=int(u),int(v)
    cut[v]=u
lenth=0
for p in range(1,n+1):
    bisect.insort_left(sli,cut[p])
    q=bisect.bisect_left(sli,cut[p])
    lenth+=sli[q+1]-sli[q-1]
print(lenth)