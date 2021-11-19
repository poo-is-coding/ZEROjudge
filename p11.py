#輸入資料
n=int(input())
data=input().split()
data=[int(i) for i in data]
#計算最小值，數值總和列表
sumall=0
summarydata=[]
mini=data[0]
for j in range(n):
    sumall+=data[j]
    summarydata.append(sumall)
    if data[j]<mini:
        mini=data[j]
        m=j
#判斷
l=0
r=n-1
suml1=0
while True:
    if l==r:
        print(data[l])
        break
    else:

        
        mini=min(data[l:r+1])
        m=data.index(mini)


        if m != l and m != r:
            suml=summarydata[m-1]-suml1
            sumr=summarydata[r]-summarydata[m]
        elif m == l:
            suml=0
            sumr=summarydata[r]-summarydata[m]
        elif m==r:
            sumr=0
            suml=summarydata[m-1]-suml1
        if suml>sumr:
            r=m-1
        else:
            l=m+1
            suml1=summarydata[m]