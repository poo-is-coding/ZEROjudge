#範例：第一行為n m，n為資料長度,接下來一行為長度為n的數字代表資料
#接下來將會有m行，l r，請輸出[l,r]間的總和
from sys import stdin
rd = stdin.readline
n,m = [int(_) for _ in rd().split()]
data = [int(_) for _ in rd().split()]#len(data)==n
tree=[0 for i in range(2*n+3)]
#建立一棵樹
def create_tree(rawarr,tr,node,start,end):
    if start==end:
        tr[node]=rawarr[start]
    else:
        mid = (start+end)//2
        left_node=2*node+1
        right_node=2*node+2
        create_tree(rawarr,tr,left_node,start,mid)
        create_tree(rawarr,tr,right_node,mid+1,end)
        tr[node]=tr[left_node]+tr[right_node]
create_tree(data,tree,0,0,n-1)