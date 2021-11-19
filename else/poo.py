oper=input().split()
def func(arr):
    count=-1
    array=[]
    if len(arr)==1:
        print(arr[0],end="")
        return
    for i in range(len(arr)):
        array.append(arr[i])
        if len(arr[i])==1 and (ord(arr[i])>57 or ord(arr[i])<48):
            count=0
        elif count==0 or count==1:
            count+=1
        if count==2:
            count=-1
            array.pop()
            array.pop()
            array.pop()
            array.append(arr[i-1]+" "+arr[i]+" "+arr[i-2])
    func(array)
func(oper)