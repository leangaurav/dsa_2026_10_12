a = [10,4,6,3,88,90]
#.   0. 1 2 3 4   5
#   [10,14,20,23,111,201]
#  i 0 1


# for i in range(len(a)-1):
#     a[i+1] = a[i] + a[i+1]


for i in range(1,len(a)):
    a[i] = a[i-1] + a[i]

print(a)