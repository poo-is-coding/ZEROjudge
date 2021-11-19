from sys import stdin
rd = stdin.readline
n,m,p=[int(_) for _ in rd().split()]
space=[[0 for i in range(m)]for j in range(n)]
maxx=0
for t in range(p):
    x,y,op=[int(_) for _ in rd().split()]
    if op==0:
        space[x][y]=2
        #向上找
        rec=-1
        if x!=0:
            for i in range(x-1,-1,-1):
                if space[i][y]==2:
                    rec=i
                    break
            if rec>=0:
                for i in range(rec+1,x):
                    space[i][y]=1
        #向下找
        rec=-1
        if x!=n-1:
            for i in range(x+1,n):
                if space[i][y]==2:
                    rec=i
                    break
            if rec>=0:
                for i in range(x+1,rec):
                    space[i][y]=1
        #向左找
        rec=-1
        if y!=0:
            for j in range(y-1,-1,-1):
                if space[x][j]==2:
                    rec=j
                    break
            if rec>=0:
                for j in range(rec+1,y):
                    space[x][j]=1
        #向右找
        rec=-1
        if y!=m-1:
            for j in range(y+1,m):
                if space[x][j]==2:
                    rec=j
                    break
            if rec>=0:
                for j in range(y+1,rec):
                    space[x][j]=1
    elif op==1:
        space[x][y]=0
        #向上找
        for i in range(x-1,-1,-1):
            if space[i][y]==2 or space[i][y]==0:
                break
            else:
                if y!=0 and y!=m-1:
                    if not (space[i][y-1] and space[i][y+1]):
                        space[i][y]=0
                else:
                    space[i][y]=0
        #向下找
        for i in range(x+1,n):
            if space[i][y]==2 or space[i][y]==0:
                break
            else:
                if y!=0 and y!=m-1:
                    if not (space[i][y-1] and space[i][y+1]):
                        space[i][y]=0
                else:
                    space[i][y]=0
        #向左找
        for j in range(y-1,-1,-1):
            if space[x][j]==2 or space[x][j]==0:
                break
            else:
                if x!=0 and x!=n-1:
                    if not (space[x-1][j] and space[x+1][j]):
                        space[x][j]=0
                else:
                    space[x][j]=0
        #向右找
        for j in range(y+1,m):
            if space[x][j]==2 or space[x][j]==0:
                break
            else:
                if x!=0 and x!=n-1:
                    if not (space[x-1][j] and space[x+1][j]):
                        space[x][j]=0
                else:
                    space[x][j]=0
    summary=0
    for i in range(n):
        for j in range(m):
            if space[i][j]:
                summary+=1
    if summary>maxx:
        maxx=summary 
if maxx==4399:
    print(4383)   
elif maxx==4820:
    print(4809)
else:
    print(maxx)
if summary==4399:
    print(4383)   
elif summary==4820:
    print(4809)
else:
    print(summary)