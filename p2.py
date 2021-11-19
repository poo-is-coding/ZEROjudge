arg = input()
a,b,c=arg.split()
a,b,c=int(a),int(b),int(c)
jud=b**2-4*a*c
if jud<0:
    print("No real root")
else:
    ans1 = (jud**0.5-b)/(2*a)
    ans2 = (-1*(jud**0.5)-b)/(2*a)
    if ans1==ans2:
        print("Two same roots x="+str(int(ans1)))
    else:
        if ans2>ans1:
            ans1,ans2=ans2,ans1
        print("Two different roots x1="+str(int(ans1))+" , x2="+str(int(ans2)))