from sys import stdin
rd = stdin.readline
m,n = [int(i) for i in rd().split()]
data = [int(i) for i in rd().split()]
inddic = dict(zip(data,[v for v in range(n)]))
l = 0
prer = 0
r = m
beauty = 0
while r <= n:
    rec = 0
    for i in range(prer,r):
        curnum = data[i]
        if inddic[curnum] != i:
            if inddic[curnum]<r and inddic[curnum]>=l:
                rec = max(min(inddic[curnum],i),rec)
            inddic[curnum] = i
    if rec:
        l = rec+1
        prer = r
        r = l+m
    else:
        l += 1
        prer = r
        r += 1
        beauty += 1
else:        
    print(beauty)       
