s = "i = %d" % 10
print(s)

s = "i = %o" % 10
print(s)

s = "i = %4d" % 10
print(s)

s = "i = %f" % 10
print(s)


s = "i = %s" % 10
print(s)


s = "i = %d, s=%s" % (10,10)
print(s)


# s = "i = %d, s=%s" % ('10',10) # error  TypeError: %d format: a real number is required, not str
# print(s)

i = 10
s = 'abcd'

print(f"{i}, {s}")

# print(f"{i}, {d}") # Error d is not defined

f = 1.99

print(f"{f}")


print(f"{f*2}")

print(f"{len(s)}")