n=int(input())
rec=n
output=""
for i in range(2,n+1):
    if rec%i==0:
        rec=rec/i
        output=output+str(i)
        if rec%i==0:
            times=1
            while rec%i==0:
                rec=rec/i
                times+=1
            output=output+"^"+str(times)
        output=output+" * "
print(output[:-3])