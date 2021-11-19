from sys import stdin
from itertools import accumulate
import bisect as bi
#input
rd = stdin.readline
n,m = [int(i) for i in rd().split()]
value = [int(i) for i in rd().split()]
val_acum = list(accumulate(value))
task = [int(i) for i in rd().split()]
crroom = 0
#走訪各任務
for t in task:

    if crroom == 0:
        search = t
    else:
    #如果當前房間並非第一個房間，則房間累計分數(val_acum)陣列需要經過一連串平移，但與其讓陣列平移，不如反過來讓任務平移
        search = t+val_acum[crroom-1]
        if search > val_acum[-1]:
            search -= val_acum[-1]
    #二分搜
    crroom = bi.bisect_right(val_acum,search)
    #假設n是能完成任務的房間，n+1會是新的位置，但若n是剛好完成任務的房間(即任務的累計分數在val_acum陣列裡)，則二分搜出來的結果已經是n+1了
    if search != val_acum[crroom-1]:
        crroom += 1
    #房間繞一圈後要回到一開始
    crroom = crroom%n
print(crroom)