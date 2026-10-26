def my_max(arr):
    if len(arr) == 0:
        raise ValueError("array must not be empty")

    res = arr[0]

    for i in arr:
        if i > res:
            res = i
    return res

print(my_max([1,2,3,6,4]))
print(my_max([1,2,3,60,4]))
print(my_max([1]))
print(my_max([-1]))
print(my_max([]))