from sys import  stdin
rd = stdin.readline
n,m = [int(i) for i in rd().split()]
value = [int(i) for i in rd().split()]
task = [int(i) for i in rd().split()]
room = 0
for i in range(m):
    summary = 0
    for j in range(n):
        index = (room+j)%n
        summary += value[index]
        if task[i] <= summary:
            room = (index+1)%n
            break
print(room)
