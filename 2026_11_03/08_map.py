a = [10,20,30,40]

res = map(lambda x: x**2, a)
print(res)
print(list(res))

res = map(lambda x: x**2, a)
for v in res:
    print(v)