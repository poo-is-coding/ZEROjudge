from sys import stdin
rd = stdin.readline
N,K = [int(_) for _ in rd().split()]
data = [int(_) for _ in rd().split()]
if K==1:
    print(max(data))
else:
    karr = [int(_) for _ in rd().split()]
    dp = [0 for i in range(N)]
    dp[0]=data[0]
    last = 0
    prek=karr[0]
    for i in range(1,N):
        if karr[i]==prek:
            dp[i]=max(last+data[i],dp[i-1])
        else:
            dp[i]=dp[i-1]+data[i]
            prek=karr[i]
            last=dp[i-1]
    print(dp[-1])