
from sys import stdin
rd = stdin.readline
r,c,k,m = [int(i) for i in rd().split()]
cityspace = [[int(i) for i in rd().split()]for i in range(r)]

for d in range(m):
    modify = [[0 for i in range(c)]for j in range(r)]

    for i in range(r):
        for j in range(c):
            if cityspace[i][j]==-1:
                continue
            else:
                adj = cityspace[i][j]//k
                if i-1 >= 0:
                    if cityspace[i-1][j] != -1:
                        modify[i][j] -= adj
                        modify[i-1][j] += adj
                if i+1 < r:
                    if cityspace[i+1][j] != -1:
                        modify[i][j] -= adj
                        modify[i+1][j] += adj
                if j-1 >= 0:
                    if cityspace[i][j-1] != -1:
                        modify[i][j] -= adj
                        modify[i][j-1] += adj
                if j+1 < c:
                    if cityspace[i][j+1] != -1:
                        modify[i][j] -= adj
                        modify[i][j+1] += adj
    for i in range(r):
        for j in range(c):
            cityspace[i][j] += modify[i][j]
mi=cityspace[0][0]
mx=cityspace[0][0]
for i in range(r):
        for j in range(c):
            if cityspace[i][j] < mi and cityspace[i][j] != -1 :
                mi = cityspace[i][j]
            if cityspace[i][j] > mx:
                mx = cityspace[i][j]
print(mi)
print(mx)
