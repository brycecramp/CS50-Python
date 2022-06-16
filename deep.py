#In deep.py, implement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything, outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No.

#obtain user input and assign to variable answer
answer = input("What is the Answer to the Great Question of Life, the Universe and Everything?" )

#compare input to answer to the universe via conditional and print yes/no
if answer.lower() == "forty two" or answer.lower() == "forty-two" or answer.lower() == "42":
	print("Yes")
else:
	print("No")
