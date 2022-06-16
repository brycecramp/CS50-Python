#In a file called einstein.py, implement a program in Python that prompts the user for mass as an integer (in kilograms) and then outputs the equivalent number of Joules as an integer. Assume that the user will input an integer.

#ask user for mass in kilograms
mass = int(input("Enter your mass in kilograms: "))

#print E=mc^2 in joules
print("Enery in joules = ",mass * 300000000)
