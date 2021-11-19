#資料輸入
n = int(input())
data=[]

for i in range(n):
    seq = input().split()
    seq = [int(k) for k in seq]
    data.append(seq)
#判斷數列是何種數列
for m in data:
#等差 
    if m[1]-m[0]==m[2]-m[1]:
        d=m[1]-m[0]
        m.append(m[-1]+d)
#等比
    elif m[1]/m[0]==m[2]/m[1]:
        d=m[1]/m[0]
        m.append(m[-1]*d)
#輸出
for k in data:
    for i in k:
        print(int(i),end=" ")
    print()