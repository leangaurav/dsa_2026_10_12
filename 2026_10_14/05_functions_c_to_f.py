# Option-1
def celsius(c):
    return (c * 9/5) + 32


c1= 10
c2 = 20

f = (celsius(c1) + celsius(c2))/2

c = float(input("Enter Celsius: "))
print(celsius(c))

# Option-2
def ctof(cel):
    res=(cel*9/5)+32
    print(res)
cel=int(input("Enter celcius "))
ctof(cel)

# Option-3
def ctof():
    cel=int(input("Enter celcius "))
    res=(cel*9/5)+32
    print(res)

ctof()
