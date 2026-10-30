s = 0
while True:
    choice = input("Enter e to exit. Else enter a number: ")

    if choice == 'e':
        break

    if not choice.isnumeric():
        print("you must only enter a number !!")
        continue

    s += int(choice)

print("total sum of all numbers:", s)