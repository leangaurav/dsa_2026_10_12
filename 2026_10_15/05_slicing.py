s = '123456789'

print(s[1:3])
print(s[3:1])

print(repr(s[1:3]))
print(repr(s[3:1]))

print(s[1:7:2])
print(s[1:8:2])
print(s[3:1:-1])

# s = '123456789'
print(s[:4])
print(s[4:])
print(s[::2]) # start: end : step
print(s[-4:])
print(s[-4:-8])
print(s[-4:-8:-1])
print(s[::-1])