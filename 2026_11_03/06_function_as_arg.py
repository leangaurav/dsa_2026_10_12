a = [10,20,30,40]

def square(a):
    return a * a

# b = []
# for v in a:
#     b.append(square(v))
# print(b)

def apply(data):
    b = []
    for v in a:
        b.append(square(v))
    return b

print(apply(a))

def cube(a):
    return a**3

def apply_v2(data, fn):
    b = []
    for v in a:
        b.append(fn(v))
    return b

def add(a,b):
    return a+b

print(apply_v2(a, square))
print(apply_v2(a, cube))
print(apply_v2(a, add))

