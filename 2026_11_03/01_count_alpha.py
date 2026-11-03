# hello worLd
# H 1
# E 1
# L 3
# O 2
# ....
arr = [0]*26

s = input("enter a string:")

for c in s:
    if c.isalpha():
        c = c.upper()
        int_val = ord(c)        # (65-90)
        arr[int_val-65] += 1    # (0-25)

# for i in range(len(arr)):
#     if arr[i] > 0:
#         print(f"{chr(65+i)}: ", arr[i])

for i, count in enumerate(arr):
    if count > 0:
        print(f"{chr(65+i)}: ", count)

"""
s Abc ABdb.

arr 2 3 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0
    0 1 2 3 4 5 6..
"""