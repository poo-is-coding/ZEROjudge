decoder=-7
char=input()
asciilist=[]
for k in char:
    asciilist.append(ord(k))
for i in asciilist:
    i+=decoder
    i=chr(i)
    print(i,end="")
