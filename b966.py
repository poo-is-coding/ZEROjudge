from functools import lru_cache
from sys import stdin
rd=stdin.readline
n=int(rd())
line=[0 for i in range(10000000)]
def upd(line,node,l,r,left,right):
    if l==r:
        line[l]=1
    leftnode=2*node+1
    rightnode=2*node+2
    mid=(l+r)//2
