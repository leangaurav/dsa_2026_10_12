def add(a,b):
    return a+b

def diff(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

ops = {'+': add, '-': diff, '*': mul, '/': div}

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
