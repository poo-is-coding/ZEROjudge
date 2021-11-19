from sys import stdin
from copy import deepcopy
rd = stdin.readline
n,m = [int(i) for i in rd().split()]
dise = [[5,1,4,6,3,2] for j in range(n)]
def modify(disenum,method):
    if method >= 0:
        dise[disenum],dise[method] = deepcopy(dise[method]),deepcopy(dise[disenum])

    elif method == -2:
        dise[disenum] = [dise[disenum][0],dise[disenum][4],dise[disenum][1],dise[disenum][2],dise[disenum][3],dise[disenum][5]]

    elif method == -3:
        dise[disenum] = [dise[disenum][3],dise[disenum][0],dise[disenum][2],dise[disenum][5],dise[disenum][4],dise[disenum][1]]

for k in range(m):
    x,me = [int(i) for i in rd().split()]
    modify(x-1,me-1)
out=""
for p in range(n):
    out += str(dise[p][1])
    out +=" "
print(out[:-1])

