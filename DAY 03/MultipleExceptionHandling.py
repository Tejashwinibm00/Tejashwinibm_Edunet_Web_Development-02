def add(a,b):
    return a + b
def sub(a,b):
    return a - b
def multi(a,b):
    return a * b
def div(a,b):
    try:
        return a / b 
    except ZeroDivisionError :
        return "Cannot divide number by zero"
print()

print(add(2,4))
print(sub(10,3))
print(multi(2,4))
print(div(5,6))