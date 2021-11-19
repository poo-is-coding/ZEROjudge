n,m=[int(_) for _ in input().split()]
space=[[0 for i in range(m)] for j in range(n)]
for i in range(n):
    for j in range(m):
        if i==0:
            space[i][j]=1
        elif j==0:
            space[i][j]=1
        else:
            space[i][j]=space[i-1][j]+space[i][j-1]+space[i-1][j-1]
print(space[n-1][m-1])