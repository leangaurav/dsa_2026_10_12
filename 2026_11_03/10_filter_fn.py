import random as r
a = [r.randint(10,20) for _ in range(5)] # list comprehension

# a = []
# for _ in range(5):
#     a.append(r.randint(10,20) )

print(a)
f = filter(lambda x: x%2 == 0, a)
print(list(f))