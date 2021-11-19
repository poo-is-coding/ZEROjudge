from sys import stdin
rd = stdin.readline
n,m = [int(_) for _ in rd().split()]
q=[0 for i in range(n)]
tree=[0 for i in range(200000)]
def upd(tree,node,data,left,right,l,r):
    mid = (left+right)//2
    leftnode=2*node+1
    rightnode=2*node+2
    if left>=l and right<=r:
        tree[node]+=data
        return
    if left>r or right<l:
        return
    upd(tree,leftnode,data,left,mid,l,r)
    upd(tree,rightnode,data,mid+1,right,l,r)
sea=[0 for _ in range(n)]
def search(tree,node,l,r,summ):
    summary=summ+tree[node]
    if l==r:
        sea[l]=summary
        return
    mid=(l+r)//2
    lnode=2*node+1
    rnode=2*node+2
    search(tree,lnode,l,mid,summary)
    search(tree,rnode,mid+1,r,summary)
for t in range(m):
    l,r,imf=[int(_) for _ in rd().split()]
    upd(tree,0,imf,0,n-1,l,r)
search(tree,0,0,n-1,0)
sea.sort()
weight=[int(_) for _ in rd().split()]
weight.sort()
summ=0
for i in range(n):
    summ+=weight[n-i-1]*sea[i]
print(summ)
""" for t in range(m):
    l,r,i = [int(_) for _ in rd().split()]
    l-=1 """