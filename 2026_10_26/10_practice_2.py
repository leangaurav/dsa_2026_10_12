a = [10,19,22,33,4,5,6]\
#.   0.  1. 2. 3 4 5 6

for i in range(len(a)):
    if a[i]%2:
        a[i] *= 2
    else:
        a[i] %= 2

print(a)