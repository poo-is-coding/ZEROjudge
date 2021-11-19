
import bisect
n=int(input())
pos=[]
for j in range(n):
    pos.append([int(i) for i in input().split()])
pos.sort()
data=[pos[y][1] for y in range(n)]
#LIS
lenth=[data[0]]
l=1
for i in range(1,n):
    if data[i]>=lenth[-1]:
        lenth.append(data[i])
        l+=1
    else:
        q=bisect.bisect_right(lenth,data[i])
        lenth[q]=data[i]
print(l)