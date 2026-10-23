s = input('enter a string: ')

count = 0
for c in s:
    count += (c.lower() in 'aeiou')

print(count)