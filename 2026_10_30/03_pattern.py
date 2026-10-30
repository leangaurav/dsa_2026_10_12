
i = 0
while i < 5: # outer
    i+=1
    j = 0
    while j < i: # inner
        print("*", end='')
        j += 1
    print()

# i 0 1 1 2
# j.  0 1 0
