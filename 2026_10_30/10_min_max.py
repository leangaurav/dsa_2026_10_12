from typing import List
"""
[10, 20,3,5, 80, 7]
 0.  1. 2 3. 4.  5

m   10 20 20 20 80 80
val 10 20 3. 5. 80 7
"""
def operate(data: List): #using type hint for Linter
    if len(data) == 0: # edge case check
        return None

    m = data[0]
    for val in data:
        if val < m:
            m = val

    return m

print(operate([10, 20,3,5,80,7]))
print(operate([-1,-2,-3]))
print(operate([]))
print(operate([10]))

def operate2(data: List): #using type hint for Linter
    if len(data) == 0: # edge case check
        return None

    m = 0
    for i in range(len(data)):
        if data[i] > data[m]:
            m = i

    return m

print()
print(operate2([10, 20,3,5,80,7]))
print(operate2([-1,-2,-3]))
print(operate2([]))
print(operate2([10]))