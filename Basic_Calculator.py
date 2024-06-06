def add(a,b):
    answer = a + b
    print(str(a) + " + " + str(b) + " = " + str(answer))
    
def subtract(a,b):
    answer = a - b
    print(str(a) + " - " + str(b) + " = " + str(answer))

def multiply(a,b):
    answer = a * b
    print(str(a) + " * " + str(b) + " = " + str(answer))

def divide(a,b):
    answer = a / b
    print(str(a) + " / " + str(b) + " = " + str(answer))

print("A. Add")
print("B. Subtract")
print("C. Multiply")
print("D. Divide")
print("E. Exit")

choice = input("Input your choice: ")

if choice == "A" or choice == "a":
    print("Addition")
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    add(a,b)
elif choice == "B" or choice == "b":
    print("Subtraction")
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    subtract(a,b)
elif choice == "C" or choice == "c":
    print("Multiplication")
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    multiply(a,b)
elif choice == "D" or choice == "d":
    print("Division")
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    divide(a,b)
elif choice == "E" or choice == "e":
    print("Program terminated")
    quit()
else:
    print("Invalid choice")
