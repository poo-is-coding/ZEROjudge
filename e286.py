from sys import stdin
rd = stdin.readline


h = [0,0]
g = [0,0]
for j in range(2):
    hsum,gsum = 0,0
    host1 = [int(i) for i in rd().split()]
    guest1  = [int(i) for i in rd().split()]
    for i in range(4):
        hsum += host1[i]
        gsum += guest1[i]
    if gsum>hsum:
        g[j]=1
    else:
        h[j]=1
    print(str(hsum)+":"+str(gsum))
if 1 not in h:
    print("Lose")
elif 0 not in h:
    print("Win")
else:
    print("Tie")
