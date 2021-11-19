n,m,k = [int(_) for _ in input().split()]
n=n-k+1
ans=0
for i in range(k):
    ans+=m
    ans=ans%n
    n+=1
print(ans+1)