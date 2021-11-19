"""
I:
1 5
2 1 4 -7 4
O:
7
"""
from sys import stdin
rd = stdin.readline
m,n = [int(e) for e in rd().split()]

sp = [[int(e) for e in rd().split()] for l in range(m)]
dp = [[0 for e in range(n)] for l in range(m)]

for i in range(m):
    r_l = [0 for e in range(n)]
    l_r = [0 for e in range(n)]
    
    if i == 0:
        r_l[0] = sp[i][0]
        l_r[n-1] = sp[i][n-1]
        for j in range(1,n):
            r_l[j] = max(r_l[j-1]+sp[i][j],sp[i][j])
            l_r[n-j-1] = max(l_r[n-j]+sp[i][n-j-1],sp[i][n-j-1])
    else:
        r_l[0] = sp[i][0]+dp[i-1][0]
        l_r[n-1] = sp[i][n-1]+dp[i-1][n-1]
        for j in range(1,n):
            r_l[j] = max(r_l[j-1]+sp[i][j],sp[i][j]+dp[i-1][j])
            l_r[n-j-1] = max(l_r[n-j]+sp[i][n-j-1],sp[i][n-j-1]+dp[i-1][n-j-1])
    for j in range(n):
        dp[i][j] = max(r_l[j],l_r[j])
print(max(dp[-1]))
