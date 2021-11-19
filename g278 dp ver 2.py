from sys import stdin
from copy import deepcopy
rd=stdin.readline
n,k=[int(i) for i in rd().split()]
data=[int(i) for i in rd().split()]
function = [0 for i in range(n)]
re = [0 for i in range(max(data)+1)]
record=0
for i in range(1,n):
    if re[data[i]]!=0:
        function[i] = re[data[i]]+1
        re[data[i]]=i
    else:
        function[i]=1
        re[data[i]]=i
    function[i]=max(record,function[i])
    record=max(record,function[i])
#滾動式dp(空間優化) 因為每一項皆來自[i]或[i-1]，只有兩行，因此可以對此進行空間優化
if k==1:
    dp = [1 for i in range(n)]
    for j in range(1,n):
        dp[j]=max(dp[j-1],j-function[j]+1)
    print(dp[-1])

else:
    dp = [[1 for b in range(n)] for m in range(2)]
    for i in range(k):
        for j in range(1,n):
            if i==0 or function[j]==0:
                dp[1][j]=max(dp[1][j-1],j-function[j]+1)
                continue
            dp[1][j]=max(dp[1][j-1],dp[0][function[j]-1]+j-function[j]+1)
        dp[0]=deepcopy(dp[1])
    print(dp[-1][-1])