def circle(n):
    sum=2
    for i in range(1,n+1):
        sum+=2*(i-1)
    return sum
data=[]
try:
    while True:
        j=circle(int(input()))
        data.append(j)
except:
    pass
for i in data:
    print(i)