from copy import deepcopy
from sys import stdin
rd=stdin.readline
n,k=rd().split()
n,k=int(n),int(k)
data=rd().split()
#lft=[0 for i in range(n)]
""" stmap={v:0 for v in data}
left=0
stmap[data[1]]=1
stmap[data[0]]=0
print(stmap) """
def function(ind):
    temparr=[]
    for m in range(ind,-1,-1):
        if data[m] in temparr:
            return m+1
        elif data[m] not in temparr:
            temparr.append(data[m])
    return 0
lft=[function(i) for i in range(n)]
""" print(lft) """
if k==1:
    st=[i-lft[i]+1 for i in range(n)]
    print(max(st))
else:
    dp = [[1 for b in range(n)] for m in range(2)]
    for i in range(k):
        for j in range(1,n):
            if i==0 or lft[j]==0:
                dp[1][j]=max(dp[1][j-1],j-lft[j]+1)
                continue
            dp[1][j]=max(dp[1][j-1],dp[0][lft[j]-1]+j-lft[j]+1)
        dp[0]=deepcopy(dp[1])
    print(dp[-1][-1])