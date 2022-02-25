# Program: Adds two numbers. 
def add(num1, num2):
    return (num1 + num2)

# Program: Subtracts two numbers. 
def subtract(num1, num2):
    return (num1 - num2)

# Program: Multiplies two numbers. 
def multiply(num1, num2):
    return (num1 * num2)

# Program: Divides two numbers. 
def divide(num1, num2):
    if num2 == 0:
        return "Error: Division by 0."
    
    else:
        return (num1 / num2)

# Program: Gets remainder when deviding two numbers. 
def remain(num1, num2):
    if num2 == 0:
        return "Error: Division by 0."
    
    else:
        return (num1 % num2)

# Program: Gets quotiont when deviding two numbers. 
def int_div(num1, num2):
    if num2 == 0:
        return "Error: Division by 0."
    
    else:
        return (num1 // num2)

# Program: Creats main function.
def main():
    list = [(0, 0), (1, 0), (0, -1), (1.4, -5), (10, -3.4), (4.32, 2.2)]
    
    print("add: ")    
    for test in list:               # 0, 1, -1, -3.6, 6.6, 6.52
        test1 = test[0]
        test2 = test[1]
        print(add(test1, test2))
        
    print("\nsubtract: ")    
    for test in list:               # 0, 1, 1, 6.4, 13.4, 2.12
        test1 = test[0]
        test2 = test[1]
        print(subtract(test1, test2))

    print("\nmultiply: ")           # 0, 0, 0, -7, -34, 9.504
    for test in list:
        test1 = test[0]
        test2 = test[1]
        print(multiply(test1, test2))

    print("\ndivide: ")             # Error, Error, 0, -0.28 -2.941176471,
    for test in list:               # 1.963636364
        test1 = test[0]
        test2 = test[1]
        print(divide(test1, test2))

    print("\nremain: ")             # Error, Error, 0, -3.6, -0.12, 2.12
    for test in list:
        test1 = test[0]
        test2 = test[1]
        print(remain(test1, test2))

    print("\nint_div: ")            # Error, Error, 0, -1, -3, 1
    for test in list:
        test1 = test[0]
        test2 = test[1]
        print(int_div(test1, test2))


# Main program     
if __name__ == "__main__":
    main()
