n1 = int(input("enter first number:"))
n2 = int(input("enter second number:"))
n3 = int(input("enter third number:"))

# if n1 >= n2 and n1 >= n3:
#     l = n1
# elif n2 >= n1 and n2 >= n3:
#     l = n2
# else:
#     l = n3

l = n1
if n2 > l:
    l = n2
if n3 > l:
    l = n3


print("largest value is:", l)