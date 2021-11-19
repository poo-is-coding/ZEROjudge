from sys import stdin
rd=stdin.readline
n,m,t=[int(_) for _ in rd().split()]
c=0
if n and m:
    if t:
        print("AND")
        c=1
else:
    if not t:
        print("AND")
        c=1
if n or m:
    if t:
        print("OR")
        c=1
else:
    if not t:
        print("OR")
        c=1
if (n or m) and (not (n and m)):
    if t:
        print("XOR")
    c=1
else:
    if not t:
        print("XOR")
        c=1
if not c:
    print("IMPOSSIBLE")
