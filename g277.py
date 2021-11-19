from itertools import accumulate
from sys import stdin
rd=stdin.readline
n=int(rd())
data=[int(i) for i in rd().split()]
mindi=dict(zip(data,[i for i in range(n)]))
mindi_re={v:k for k,v in mindi.items()}
summarydata=[0]+list(accumulate(data))
data.sort()
l=0
r=n-1
for i in data:

    indexi=mindi[i]
    if indexi<l or indexi>r:
        continue
    lsum=summarydata[indexi]-summarydata[l]
    rsum=summarydata[r+1]-summarydata[indexi+1]
    if lsum>rsum:
        r=indexi-1
    if rsum>lsum:
        l=indexi+1
    if l==r:
        print(mindi_re[l])
        break



        