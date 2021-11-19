from math import gcd
data=[]
try:
    while True:
        data.append([int(_) for _ in input().split()])
except EOFError:
    pass
for i in data:
    if len(i)!=2:
        continue
    print(gcd(i[0],i[1]))