try:
    while True:
        k = 0
        d = input()
        n = len(d)
        num = int(d)
        numlist = [int(_) for _ in list(d)]
        for i in range(n):
            a=True
            if numlist[i]%2==1:
                k += numlist[i]*(10**(n-i-1))
            else:
                if i==n-1:
                    k+=numlist[i]+1
                    k1=k-2
                    a=False
                    
                else:
                    if numlist[i]==0:
                        if numlist[i-1]==1 and i-1==0 and numlist[i+1]<5:
                                k=0
                                for j in range(n-1):
                                    k+=9*(10**(n-1-j-1))
                                break
                        else:
                            k += 1*(10**(n-i-1))  
                    else:
                        if numlist[i+1]>5:
                            k += (numlist[i]+1)*(10**(n-i-1))
                            for j in range(n-i-1):
                                k+=1*(10**(j))
                            break
                        elif numlist[i+1]<5:
                            k += (numlist[i]-1)*(10**(n-i-1))
                            for j in range(n-i-1):
                                k+=9*(10**(j))
                            break
                        else:
                            r=2
                            s=True
                            while i+r<n-1:
                                if numlist[i+r]>5:
                                    k += (numlist[i]+1)*(10**(n-i-1))
                                    for j in range(n-i-1):
                                        k+=1*(10**(j))
                                        s=False
                                    break
                                elif numlist[i+r]<5:
                                    k += (numlist[i]-1)*(10**(n-i-1))
                                    for j in range(n-i-1):
                                        k+=9*(10**(j))
                                        s=False
                                    break
                                else:
                                    r+=1
                            if s:
                                k += (numlist[i]+1)*(10**(n-i-1))
                                for j in range(n-i-1):
                                    k+=1*(10**(j))
                                break
                            else:
                                break
                            
        if a:    
            print(abs(k-num))
        else:
            print(min(abs(k-num),abs(k1-num)))
except EOFError:
    pass