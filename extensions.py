#In a file called extensions.py, implement a program that prompts the user for the name of a file and then outputs that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes:

#Get user input for file
app = input("Please enter you file name with extension type: ")

#go through using only conditional statements
if app.lower().endswith("gif"):
	print("image/gif")

elif app.lower().endswith("jpg") or app.lower().endswith("jpeg"):
	print("image/jpg")
