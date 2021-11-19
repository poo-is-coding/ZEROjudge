from sys import stdin
from itertools import accumulate
import bisect as bi
from copy import deepcopy
rd = stdin.readline
n,m = [int(i) for i in rd().split()]
circle = [int(i) for i in rd().split()]
curcircle = deepcopy(circle)
crroom=0
task = [int(i) for i in rd().split()]
def out(arr,task):
    add = list(accumulate(arr))
    ind = bi.bisect_right(add,task)
    if add[ind-1] != task:
        ind += 1
    return ind
for j in task:
    cr = out(curcircle,j)
    print(curcircle,cr)
    crroom += cr
    curcircle = circle[cr::]
    curcircle.extend(circle[:cr:])
    circle = deepcopy(curcircle)
print(crroom%n)