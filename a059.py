t=int(input())
for i in range(t):
    a=int(input())
    b=int(input())
    summary=0
    for j in range(a,b+1):
        if j**0.5 == int(j**0.5):
            summary+=j
    print("Case "+str(i+1)+": "+str(summary))
            
            
