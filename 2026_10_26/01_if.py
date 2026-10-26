n = input("enter a number:")

if n.isdigit():
    n = int(n)
else:
    print("you did not enter a number")
    exit()

if n < 0:
    n = -n

print(n)