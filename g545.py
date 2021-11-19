from sys import stdin
import queue
rd = stdin.readline
N = int(rd())
q=queue.Queue(maxsize=N/2)
data = rd()
def run_str(string,l,st):
    print(string)
    for i in range(l):
        if string[i] =="[":
            if st.full():
                return 0
            print("here[")
            st.put(1)
        elif string[i]=="]":
            if st.empty():
                return 0
            print("here]")
            st.get()
        elif string[i]=="?":
            return run_str("["+string[i+1::],N-i,st)+run_str("]"+string[i+1::],N-i,st)
    if st.empty():
        print("here1")
        return 1
    else:
        print("here0")
        return 0
print(run_str(data,N,q))