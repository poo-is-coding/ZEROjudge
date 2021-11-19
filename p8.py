rag=input()
num1,num2=rag.split()
num1,num2=int(num1),int(num2)
summary=0
rec=True
for i in range(num1,num2+1):
    k=i
    n=len(str(i))
    for j in range(n):
        summary+=(k%10)**n
        k=k//10
    if i == summary:
        print(i,end=" ")
        rec=False
    summary=0
if rec:
    print("none")