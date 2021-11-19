import sys
print(sys.getsizeof({i:0 for i in range(100000000)}))