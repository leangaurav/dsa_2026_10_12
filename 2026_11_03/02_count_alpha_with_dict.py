d = {}
s = input("enter a string:")

for c in s:
    if c.isalpha():
        c = c.upper()
        d[c] = d.get(c,0) + 1 # Option-1
        # if c not in d:      # Option-2
        #   d[c] = 0
        # d[c] += 1


for k,v in d.items():
    print(f"{k}: ", v)
"""
s= hello world
c. h.    e.       L               L
d {H:1} {H:1,E:1} {H:1,E:1, L:1} {H:1,E:1, L:2}
"""