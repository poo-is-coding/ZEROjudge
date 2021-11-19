def rtom(rome):
    rome=list(rome)
    for i in range(len(rome)):
        if rome[i]=="I":
            rome[i]=1
        elif rome[i]=="V":
            rome[i]=5
        elif rome[i]=="X":
            rome[i]=10
        elif rome[i]=="L":
            rome[i]=50
        elif rome[i]=="C":
            rome[i]=100
        elif rome[i]=="D":
            rome[i]=500
        elif rome[i]=="M":
            rome[i]=1000
    if len(rome)==1:
        return rome[0]
    rec=rome[0]
    num=0
    for k in rome:
        if k>rec:
            num-=rec*2
        num+=k
        rec=k
    return num
def ntorome(number):
    if number==0:
        return "ZERO"
    else:
        data=["I","V","X","L","C","D","M"]
        output=[]
        times=0
        ctime=number
        while ctime//10 != 0:
            ctime=ctime//10
            times+=1
        for i in range(times+1):
            baseind=i*2
            end=number%5
            if end != 4:
                if number%10>=5:
                    end = data[baseind+1]+data[baseind]*end
                elif number%10<5:
                    end = data[baseind]*end
            elif end == 4:
                if number%10>5:
                    end = data[baseind]+data[baseind+2]
                elif number%10<5:
                    end = data[baseind]+data[baseind+1]
            number=number//10
            output.append(end)
        output.reverse()
        cout=""
        for i in output:
            cout+=str(i)
        return cout        
num=""
val=[]
while True:
    num=input()
    if num=="#":
        break
    val.append(num)
for num in val:
    num1,num2=num.split()
    num1,num2=rtom(num1),rtom(num2)
    ans=abs(num1-num2)
    print(ntorome(ans))

