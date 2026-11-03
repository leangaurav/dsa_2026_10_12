s1 = set()
print(s1)
s1.add(1)
print(s1)

s1.add(1)
print(s1)

s1.add(2)
print(s1)

s1.pop()
print(s1)

s1.remove(2)
print(s1)

print(1 in s1)

s2= set([1,2,3])
s1= set([2,4,5])
print(s1, s2)
print(s1-s2)
print(s1, s2)
print(s1.intersection(s2))
print(s1.union(s2))
print(s1.isdisjoint(s2))
print(len(s1.intersection(s2)) == 0)

s1.remove(2)
print(s1.isdisjoint(s2))
print(len(s1.intersection(s2)) == 0)

print()
print(s1)
s1.discard(2)
s1.remove(2)