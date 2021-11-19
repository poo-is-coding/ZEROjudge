#input

from sys import stdin
rd=stdin.readline
n,k=rd().split()
n,k=int(n),int(k)
data=rd().split()
#a function represent the left index of a stall range
def function(ind):
    temparr=[]
    for m in range(ind,-1,-1):
        if data[m] in temparr:
            return m+1
        elif data[m] not in temparr:
            temparr.append(data[m])
    return 0
print(function(6))
#dinammic programming
#dp[i][j] represent there are i people and they have seen j stall
#dp[i][j]=max( dp[i][j-1] , dp[i-1][f(j)-1]+j-f(j)+1 )
#border:0<i<=k,0<j<=n
#----------------apcs不允許用ndarray----------------------#
import numpy as np
dp = np.ones((k,n),dtype=int)
#dp = [[1 for b in range(n)] for m in range(k)]

for i in range(k):
    for j in range(n):
        #border case: when j=0:
        if j==0:
            continue
        #border case: when i=0 (which means there is one person haven't eaten)
        #border case: when f(j)=0 (which means the left index of the stall range is 0)
        if i==0 or function(j)==0:
            dp[i][j]=max(dp[i][j-1],j-function(j)+1)
            continue
        #normal case
        dp[i][j]=max(dp[i][j-1],dp[i-1][function(j)-1]+j-function(j)+1)
print(dp[-1][-1])