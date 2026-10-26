n1 = int(input("enter first operand:"))
n2 = int(input("enter second operand:"))

op = input("enter the operator (+,-,*,/):")


if op == "+":
    ans = n1 + n2
elif op == "-":
    ans = n1 + n2
elif op == "/":
    ans = n1/n2
elif op == "*":
    ans = n1*n2
else:
    print("invalid operator")
    exit()

print("Answer is: ", ans)