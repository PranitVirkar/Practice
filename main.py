def add(a,b):
    return a+b

def multiply(a,b):
    return a*b  

def divide(a,b):
    return a/b

def modulus(a,b):
    return a%b

def exponent(a,b):
    return a**b

def floor_divide(a,b):  
    return a//b

from sub import sub 

def main():
    x = 10
    y = 5

    print("Addition:", add(x, y))
    print("Subtraction:", sub(x, y))
    print("Multiplication:", multiply(x, y))
    print("Division:", divide(x, y))
    print("Modulus:", modulus(x, y))
    print("Exponentiation:", exponent(x, y))
    print("Floor Division:", floor_divide(x, y))
if __name__ == "__main__":
    main()
def sub (a,b):
    return a-b