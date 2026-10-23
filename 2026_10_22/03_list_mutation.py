l1 = [10,20]
l2 = l1

l1[0] = 100
print(l1)
print(l2)

l3 = list(l1)
l1[1] *= 10
print(l1)
print(l2)
print(l3)