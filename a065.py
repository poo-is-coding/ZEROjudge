try:
    while True:
        string=list(input())
        string=[ord(j) for j in string]
        for m in range(len(string)-1):
            imf = abs(string[m+1]-string[m])
            print(imf,end="")
        print()
except EOFError:
    pass
