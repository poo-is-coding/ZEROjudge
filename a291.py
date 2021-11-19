from sys import stdin
rd = stdin.readline
correctnum = rd()
while correctnum != "":
    correctnum=correctnum.split()
    dic = {str(i):0 for i in range(10)}
    for i in correctnum:
        dic[i]+=1
    n=int(rd())
    data = [[_ for _ in rd().split()]for i in range(n)]
    for i in data:
        A,B=0,0
        c=dic.copy()
        back=[]
        for j in range(4):
            if c[i[j]]:
                if i[j]==correctnum[j]:
                    A+=1
                    c[i[j]]-=1
                else:
                    back.append(i[j])
        for k in back:
            if c[k]:
                B+=1
        print(str(A)+"A"+str(B)+"B")
    correctnum=rd()