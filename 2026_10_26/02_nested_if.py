n = input("enter a number:")

if n.isnumeric():
    n = int(n)
else:
    if n.startswith("-") and n[1:].isnumeric():
        n = -int(n)
    else:
        print('did not enter a number')
        exit()

print("absolute value is: ", n)

