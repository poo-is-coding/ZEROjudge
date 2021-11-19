selfnum= list(input())
city={"A":10,"B":11,"C":12,"D":13,"E":14,"F":15,"G":16,"H":17,"I":34,"J":18,"K":19,"L":20,"M":21,"N":22,"O":35,"P":23,"Q":24,"R":25,"S":26,"T":27,"U":28,"V":29,"W":32,"X":30,"Y":31,"Z":33}
selfnum[0]=city[selfnum[0]]
selfnum=[int(i) for i in selfnum]
summary=0
for k in range(len(selfnum)):
    if k==0:
        summary+=9*(selfnum[k]%10)
        summary+=selfnum[k]//10
    elif k==9:
        summary+=selfnum[k]
    else:
        summary+=selfnum[k]*(9-k)
if summary%10==0:
    print("real")
else:
    print("fake")