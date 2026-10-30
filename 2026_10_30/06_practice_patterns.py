"""
5
44
333
2222
11111
"""

for i in range(5,0,-1):
    for j in range(5,i-1,-1):
        print(i,end='')
    print()

print()
i = 5
while i > 0:
    j = 5
    while j >= i:
        print(i, end='')
        j-=1
    i-=1
    print()
