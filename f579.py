"""
I:
3 9
2
3 9 -3 3 9 0
3 3 -3 -3 9 0
O:
1
"""
from sys import stdin
rd = stdin.readline
a,b = [int(i) for i in rd().split()]
ap,bp = a*-1,b*-1
n = int(rd())
person = 0
for i in range(n):
    data = [int(j) for j in rd().split()]
    c=[0,0]
    for k in data:
        if k == a:
            c[0] += 1
        elif k == ap:
            c[0] -= 1
        elif k==b:
            c[1] += 1
        elif k == bp:
            c[1] -= 1
    if 0 not in c:
        person += 1
print(person)
