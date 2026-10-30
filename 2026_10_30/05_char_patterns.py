for i in range(5): # 0 1 2 3 4
    for j in range(i+1): # 
        print(i, end='')
    print()
print()

# i 0 1 1
# j 0 0 1
"""
0
11
222
3333
44444
"""

for i in range(5): # 0 1 2 3 4
    for j in range(i+1): # 
        print(j, end='')
    print()
print()


for i in range(5): # 0 1 2 3 4
    for j in range(i+1): # 
        print(chr(65+i), end='')
    print()
print()

for i in range(5): # 0 1 2 3 4
    for j in range(i+1): # 
        print(chr(65+j), end='')
    print()
print()

c = 65
for i in range(5): # 0 1 2 3 4
    for j in range(i+1): # 
        print(chr(c), end='')
        c += 1
    print()
print()


"""
i 0
j 0
c 65
A
BC

"""

c = 65
for i in range(5): # 0 1 2 3 4
    for j in range(i+1): # 
        print(chr(c), end='')
    print()
    c += 1
print()


for i in range(5): # 0 1 2 3 4
    c = 65
    for j in range(i+1): # 
        print(chr(c), end='')
        c += 1
    print()
print()