
for i in range(5):      # 0   1.   2
    for j in range(i):  # (). (0). (0,1)
        if i == j:
            continue
        print(i, end = '')
    print()

print()

for i in range(5):      # 0   1.   2
    for j in range(5):  
        if i == j:
            continue
        print(i, end = '')
    print()
"""
0000
1111
2222
3333
4444
"""

print()
for i in range(5):      # 0     1.     2
    for j in range(5):  # (0-4) (0-4)
        if i == j:
            continue
        print(j, end = '')
    print()
"""

"""

print()
for i in range(5):      # 0     1.     2
    for j in range(5):  # 
        if i == j:
            break
        print(j, end = '')
    print()
    