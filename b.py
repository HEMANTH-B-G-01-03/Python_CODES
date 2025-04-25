# import pandas as pd 

# df = pd.read_csv('student.csv')

# print(df.describe())
op = input("Enter the operator (+, -, *, /): ")

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

if op == "+":
    print("Sum of", a, "and", b, "is", a + b)
elif op == "-":
    print("Difference of", a, "and", b, "is", a - b)
elif op == "*":
    print("Product of", a, "and", b, "is", a * b)
elif op == "/":
    if b != 0:
        print("Division of", a, "by", b, "is", a / b)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operator")




# typecasting 

a = "1"
b ="2"
c = int(a)
d = int(b)
# a = "1"
# b ="2"
print(c+d)