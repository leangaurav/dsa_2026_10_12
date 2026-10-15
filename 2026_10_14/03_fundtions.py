def Def():
    print("hello")

Def() # calling
a = Def
a()

print(type(a), type(Def), id(a), id(Def))
Def = 10
Def = a
Def()