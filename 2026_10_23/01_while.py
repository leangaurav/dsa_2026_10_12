s = ''

while s.lower() != 'exit':
    s = input('enter a string. Enter "exit" to exit loop:')
    print(f"you entered {repr(s)}")

print("after loop")