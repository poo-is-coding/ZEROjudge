"""
I:
3
1 1
2 5
3 2
O:
2
I:
74
5 6
21 23
42 53
80 82
60 70
38 48
15 97
27 26
39 48
64 74
8 12
13 18
48 62
76 82
95 99
69 37
17 19
32 47
73 81
2 1
86 94
27 28
79 11
92 98
40 48
59 70
91 28
85 92
60 72
63 74
66 74
33 66
84 89
53 39
32 32
47 62
32 33
20 21
33 37
36 47
53 67
78 67
43 58
34 42
72 81
91 18
21 22
24 25
54 68
43 62
84 90
28 29
6 8
47 65
88 96
10 13
11 15
41 51
95 79
83 85
68 78
98 99
98 100
38 29
68 80
88 12
87 95
89 96
22 24
94 99
6 10
66 76
16 18
5 3
O:
61
"""
from sys import stdin
rd=stdin.readline
n=int(rd())
pos=[]
for j in range(n):
    pos.append([int(i) for i in rd().split()])
pos.sort()
data=[pos[y][1] for y in range(n)]
lenth=[1 for i in range(n)]
#LIS
for i in range(n):
    for j in range(i):
        if data[i]>=data[j]:
            lenth[i]=max(lenth[i],lenth[j]+1)
print(max(lenth))
