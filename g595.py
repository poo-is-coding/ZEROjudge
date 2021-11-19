from sys import stdin
rd = stdin.readline
n=int(rd())
h=[int(_) for _ in rd().split()]
summary=0
for i in range(n):
    if h[i]==0:
        if i==0:
            summary+=h[i+1]
        elif i==n-1:
            summary+=h[i-1]
        else:
            summary+=min(h[i+1],h[i-1])
print(summary)