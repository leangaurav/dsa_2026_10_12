while True:
    op = input("enter the operator (+,-,*,/). Type e to exit:")

    if op == 'e':
        exit()
        
    n1 = int(input("enter first operand:"))
    n2 = int(input("enter second operand:"))

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

    print("Answer is: ", ans)