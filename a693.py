from sys import stdin
from itertools import accumulate
rd = stdin.readline
try:
    nm=rd()
    while True:
        if nm=="":
            break
        n,m = [int(_) for _ in nm.split()]
        data = [int(_) for _ in rd().split()]
        add = [0]+list(accumulate(data))
        for i in range(m):
            l,r=[int(_)for _ in rd().split()]
            l-=1
            print(add[r]-add[l])
except EOFError:
    pass