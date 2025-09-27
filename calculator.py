import math
def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y==0:
        return "Error! Cant divide by zero"
    return x/y
def power(x,y):
    return math.pow(x,y)
def square_root(x):
    if x<0:
        return "Error! Square root cant be negative"
    return math.sqrt(x)
def logarithm(x,base=10):
    if x<0:
        return "Error! Log uundefined for negative numbers"
    return math.log(x,base)
def calculator():
    while True:
        print("\n--- Simple Calculator ---")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power (x^y)")
        print("6. Square Root")
        print("7. Logarithm (base 10)")
        print("8. Exit")

        choice = input("Enter choice (1-8): ")

        if choice == '1':
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
            print("Result:", add(x, y))

        elif choice == '2':
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
            print("Result:", subtract(x, y))

        elif choice == '3':
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
            print("Result:", multiply(x, y))

        elif choice == '4':
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
            print("Result:", divide(x, y))

        elif choice == '5':
            x = float(input("Enter base number: "))
            y = float(input("Enter exponent: "))
            print("Result:", power(x, y))

        elif choice == '6':
            x = float(input("Enter number: "))
            print("Result:",square_root(x))

        elif choice == '7':
            x = float(input("Enter number: "))
            print("Result:", logarithm(x))

        elif choice == '8':
            print("Exiting calculator. Goodbye!")
            break

        else:
            print("Invalid input! Please choose between 1-8.")


if __name__ == "__main__":
    calculator()




    