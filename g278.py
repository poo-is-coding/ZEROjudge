data=input()
n,k=data.split()
n,k = int(n),int(k)
data=input().split()
templi=[]
li=[]
method1=[]
method=0


for j in data:
    if j not in templi:
        templi.append(j)
    elif j in templi:
        li.append(templi)
        templi=[]
        templi.append(j)
else:
    li.append(templi)
for i in li:
    method1.append(len(i))
for q in range(k):
    method+=max(method1)
    method1.remove(max(method1))

data.reverse()

templi=[]
li=[]
method2=[]
method_=0

for j in data:
    if j not in templi:
        templi.append(j)
    elif j in templi:
        li.append(templi)
        templi=[]
        templi.append(j)
else:
    li.append(templi)
for i in li:
    method2.append(len(i))
for q in range(k):
    method_+=max(method2)
    method2.remove(max(method2))


if method>method_:
    print(method)
else:
    print(method_)