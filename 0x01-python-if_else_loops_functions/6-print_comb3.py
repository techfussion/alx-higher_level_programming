#!/usr/bin/python3
for i in range(9):
    for j in range(i,10):
        if i == j:
            continue
        print('{}{}'.format(i, j), end=', ')

print('{}'.format(89))
