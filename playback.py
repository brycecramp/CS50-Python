#In a file called playback.py, implement a program in Python that prompts the user for input and then outputs that same input, replacing each space with ... (i.e., three periods).

#obtain user input
slowDown = input("Enter you text to speak more slowly:" )

#replace each space with 3 dots to simulator speaking slower
slowDown = slowDown.replace(" ","...")
print(slowDown)
