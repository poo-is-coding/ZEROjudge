from sys import stdin
rd = stdin.readline
n = rd()
while n!="":
    data = [int(_) for _ in n.split()]
    summ = 0
    for i in data[1::]:
        summ+=i
    if summ/data[0]>59:
        print("no")
    else:
        print("yes")
    n = rd()
 
