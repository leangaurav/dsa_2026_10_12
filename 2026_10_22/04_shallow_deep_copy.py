l1= [[1,2], [10,20,30], 300]

l2 = list(l1)
l1[2] = 3000
print(l1)
print(l2)

print(id(l1), id(l2))
print(id(l1[0]), id(l2[0]))

import copy
l3 = copy.deepcopy(l1)
print(id(l1), id(l3))
print(id(l1[0]), id(l3[0]))

print(l1[0])
l1[0][0] = 100
print(l1)
print(l2)
print(l3)