s = input('enter a string: ')

i = 0
count = 0
while i < len(s):
    count += (s[i].lower() in 'aeiou')
    i += 1

print("count of vowels", count)


count = s.lower().count('a') + s.lower().count('e') + s.lower().count('i') + \
    s.lower().count('o') + s.lower().count('u')