import numpy as np
data = [
    [12.0, 1.5, 1, 'Wine'],
    [5.0, 2.0, 0, 'Beer'],
    [40.0, 0.0, 1, 'Whiskey'],
    [13.5, 1.2, 1, 'Wine'],
    [4.5, 1.8, 0, 'Beer'],
    [38.0, 0.1, 1, 'Whiskey'],
    [11.5, 1.7, 1, 'Wine'],
    [5.5, 2.3, 0, 'Beer']
]
for i in data:
    if i[3]=='Wine':
        i[3]=0
    elif i[3]=='Beer':
        i[3]=1
    else:
        i[3]=2
z = []
for _ in [1,2,3]:
    k = float(input())
    z.append(k)
    