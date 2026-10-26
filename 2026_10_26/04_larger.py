# 2 numbers input
# check which one is larger

n1 = int(input("enter first number:"))
n2 = int(input("enter second number:"))

if n1 > n2:
    print("first one is larger")
elif n2 > n1:
    print("second one is larger")
else:
    print("both are equal")