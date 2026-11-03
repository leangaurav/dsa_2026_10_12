def add(a,b):
    return a+b

def diff(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

fn = div
print(fn(10,20))
fn = mul
print(fn(10,20))

# d = {'+': add, '-': diff, '*': mul, '/': div}