#Get user input
expression = input("Expression: ")

#Split string into components
x, y, z = expression.split(" ")
#Change strings to floats
x = float(x)
z = float(z)

#Conditions for each possible operation
if y == "+":
    print(x + z)
elif y == "-":
    print(x - z)
elif y == "x":
    print(x * z)
elif y == "/":
    if z == 0:
        print("Cannot divide by 0!")
    else:
        print(x / z)
