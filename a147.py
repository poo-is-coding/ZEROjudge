from sys import stdin
rd = stdin.readline
n = int(rd())
while n:
    for i in range(1,n):
        if i%7 != 0:
            print(i,end=" ")
    n = int(rd())
    print()
