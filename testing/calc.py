def add(x,y):
    return x+y
def mult(x,y):
    return x*y
def div(x,y):
    if y==0:
        raise ValueError("a number cannot be divided by zero,so pick another value of y")
    return x/y
def subt(x,y):
    return x-y