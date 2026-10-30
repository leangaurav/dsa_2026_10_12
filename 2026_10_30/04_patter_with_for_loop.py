for i in range(5):
    for j in range(5-i):
        print("*", end = '')
    print()


print()
for i in range(5): # 0->4
    for j in range(5-i-1): # 4, 3, 2 ,1, 0
        print(" ", end = '')
    for j in range(i+1):   # 1, 2, 3, 4, 5 
        print("*", end = '')
    print()


print()
for i in range(5): # 0->4
    for j in range(5-i-1): # 4, 3, 2 ,1, 0
        print(" ", end = '')
    for j in range(i*2+1):   # 1, 3, 5, 7, 9 
        print("*", end = '')
    print()