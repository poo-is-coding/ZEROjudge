def cd(num):
    for a in range(2,int(num*0.5)+2):
        if num%a==0:
            return 0
    return 1
try:
    while True:
        a,b=input().split()
        a,b=int(a),int(b)
        data=[i for i in range(a,b+1) if i!=1]
        count=0
        for j in data:
            if j==2 or j==3 or j==5 or j==7 or j==11 or j==13:
                count+=1
                continue
            elif j%2==0 or j%3==0 or j%5==0 or j%7==0 or j%11==0 or j%13==0: continue
            if cd(j):
                count+=1

        print(count)
except EOFError:
    pass