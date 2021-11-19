from sys import stdin
"""
2 4
3 7 4 2
5 6 1 8

"""


rd = stdin.readline
n,m = [int(_) for _ in rd().split()]
space = [[int(_) for _ in rd().split()]for i in range(n)]
check = [[0 for _ in range(m)]for i in range(n)]
mini = space[0][0]
mindi = 0
mindj = 0
for i in range(n):
    for j in range(m):
        if space[i][j]<mini:
            mini = space[i][j]
            mindi = i
            mindj = j
summary = 0
while mini != 1000001:
    summary += mini
    temp = [1000001 for i in range(4)]
    check[mindi][mindj] = 1
    if mindi>0:
        if check[mindi-1][mindj]!=1:
            temp[0] = space[mindi-1][mindj]
    if mindj<m-1:
        if check[mindi][mindj+1]!=1:
            temp[1] = space[mindi][mindj+1]
    if mindi<n-1:
        if check[mindi+1][mindj]!=1:
            temp[2] = space[mindi+1][mindj]
    if mindj>0:
        if check[mindi][mindj-1]!=1:
            temp[3] = space[mindi][mindj-1]
    mini=temp[0]
    ti = 0
    for i in range(4):
        if temp[i]<mini:
            mini = temp[i]
            ti = i
            
    if ti==0:
        mindi-=1
    elif ti==1:
        mindj+=1
    elif ti==2:
        mindi+=1
    elif ti == 3:
        mindj -=1
print(summary)
    
