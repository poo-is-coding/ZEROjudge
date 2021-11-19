from sys import stdin
rd = stdin.readline
n = int(rd())
data = [int(_) for _ in rd().split()]

bier = lambda x:(x&-x) 
bit = [0 for _ in range(2*n+1)]

def upd(ind,value):
    while ind <= 2*n:
        bit[ind] += value
        ind += bier(ind)

def summary(ind):
    s = 0
    while ind:
        s += bit[ind]
        ind -= bier(ind)
    return s

left = [0 for _ in range(n+1)]
right = [0 for _ in range(n+1)]
for x in range(1+2*n):
    if left[data[x-1]]:
        right[data[x-1]] = x
    else:
        left[data[x-1]] = x
ans = 0
for i in range(1,n+1):
    ans += summary(right[i])-summary(left[i])
    upd(left[i],1)
    upd(right[i],1)

print(ans)