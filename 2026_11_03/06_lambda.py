ops = {'+': lambda x,y: x+y, # no return statement in lambda, the expression's outcome is auto returned
       '-': lambda x,y: x-y,
        '*': lambda x,y:x*y,
        '/': lambda x,y:x/y}

while True:
    choice = input("enter a choice(+,-,/,*). Press e to exit:")

    if choice in ops:
        a = int(input("enter first value:"))
        b = int(input("enter second value:"))
        fn = ops[choice]
        print(f'{a} {choice} {b} = ', fn(a,b))
    elif choice == 'e':
        exit()
    else:
        print("invalid input, enter again !!!!")
