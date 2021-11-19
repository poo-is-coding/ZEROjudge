from sys import stdin
for s in stdin:
    if s=="":
        break
    n,m=[int(i) for i in s.split()]
    dp=[[0 for i in range(n)] for j in range(n)]
    dp[0]=[int(i) for i in stdin.readline().split()]
    for i in range(1,n):
        dp[0][i]+=dp[0][i-1]
    for j in range(1,n):
        temp=[int(k) for k in stdin.readline().split()]
        for i in range(n):
            if i==0:
                dp[j][i]=dp[j-1][i]+temp[i]
            else:
                dp[j][i]=dp[j-1][i]+dp[j][i-1]-dp[j-1][i-1]+temp[i]
    for t in range(m):
        x1,y1,x2,y2=[int(_) for _ in stdin.readline().split()]
        if x1==1:
            if y1==1:
                print(dp[x2-1][y2-1])
            else:
                print(dp[x2-1][y2-1]-dp[x2-1][y1-2])
        elif y1==1:
            print(dp[x2-1][y2-1]-dp[x1-2][y2-1])
        else:
            print(dp[x2-1][y2-1]-dp[x1-2][y2-1]-dp[x2-1][y1-2]+dp[x1-2][y1-2])