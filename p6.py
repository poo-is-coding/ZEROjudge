try:
    while True:
        size=input()
        row,col=size.split()
        row,col=int(row),int(col)
        s=[]
        for i in range(row):
            tex=input()
            s.append(tex)
        for m in range(len(s)):
            s[m]=s[m].split()
            s[m]=[int(i) for i in s[m]]
        for j in range(col):
            for k in range(row):
                print(s[k][j],end=" ")
            print()
except:
    pass