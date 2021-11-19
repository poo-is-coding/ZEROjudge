from sys import stdin
Dict={"0 1 0 1":"A","0 1 1 1":"B","0 0 1 0":"C","1 1 0 1":"D","1 0 0 0":"E","1 1 0 0":"F"}
for s in stdin:
    ans=""
    n=int(s)
    for i in range(n):
        data=stdin.readline()
        data=data.replace("\n","")
        ans+=Dict[data]
    print(ans)

        

    