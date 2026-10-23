i = input('Enter a number: ')

total = 0
while i.isdecimal():
    total += int(i)
    i = input('Enter a number: ')

print(total)