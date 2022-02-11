
def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def div(a,b):
    return a/b


def calculator(func):
    # storing the function in a variable
    logic = func(25,2)
    print(logic)


calculator(add)
calculator(sub)
calculator(div)
