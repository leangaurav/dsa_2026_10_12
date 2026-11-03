a = [10,20,30,40]

def apply_v2(data, fn):
    b = []
    for v in a:
        b.append(fn(v))
    return b

print(apply_v2(a, lambda x: x**2))
print(apply_v2(a, lambda x: x**3))
print(apply_v2(a, lambda x: -x))

import math
print(apply_v2(a, math.sqrt))