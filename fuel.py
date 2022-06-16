def main():
	c = get_int()
	if 0.99 <= c <= 1:
		print("F")
	elif 0 <= c <= 0.01:
		print("E")
	else:
		c = round(c * 100,)
		print(f"{c}%")


def get_int():
	while True:
		try:
			x, y = input("Enter your fraction: ").split("/")
			x = int(x)
			y = int(y)
			if x < y:
				z = x / y
				return z
		except ValueError:
			print("x or y is not an integer!")
		except ZeroDivisionError:
			print("Cannot divide by 0!")

main()

