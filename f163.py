import sys

rd = sys.stdin.readline
n,k = [int(_) for _ in rd().split()]
mess = [int(_) for _ in rd().split()]
things = [int(_) for _ in rd().split()]
sub = [[] for _ in range(n)]
mom = [[] for _ in range(2*n+1)]
for i in range(n-1):
    a,b,c = [int(_) for _ in rd().split()]
    sub[a].append(b)
    sub[a].append(c)
    mom[b] = a
    mom[c] = a
messtree=[0 for _ in range(n)]
c = [0 for _ in range(n-1)]
for i in range(2*n-1,n-1,-1):
    messtree[mom[i]] += mess[i-n]
    c[mom[i]-1]+=1
while 1 in c:
    for i in range(n-1,1,-1):
        if c[i-1]==1:
            for j in sub[i]:
                if j<n:
                    messtree[i]+=messtree[j]
            c[i-1]+=1
while 0 in c:
    for i in range(n-1,0,-1):
        cc=0
        if c[i-1]==0:
            for j in sub[i]:
                if c[j-1]:
                    cc+=1
            if cc==2:
                c[i-1]=2
                for j in sub[i]:
                    messtree[i]+=messtree[j]
messtree.extend(mess)
def compare(th,cur):

    if cur>=n:
        return str(cur)+" "
    elif messtree[sub[cur][0]]<=messtree[sub[cur][1]]:
        messtree[sub[cur][0]]+=th
        return compare(th,sub[cur][0])
    else:
        messtree[sub[cur][1]]+=th
        return compare(th,sub[cur][1])
out=""
for i in things:
    out+=compare(i,1)
print(out[:-1])