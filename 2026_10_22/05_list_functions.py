l1 = list()
ret = l1.append(10)
print(ret)
l1.insert(0,20)
l1.insert(10,30)  # boundary case
print(l1)

l2 = [100,200]
# l1.extend(l1)
# print(l1)

l1. extend(l2)
print(l1)
print(l2)

l1.extend('abcd')
print(l1)
