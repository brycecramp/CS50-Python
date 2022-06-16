def main():
	time = input("What is the time? ")
	if 7.0 <= convert(time) <= 8.0:
		print("Breakfast time")
	if 12.0 <= convert(time) <= 13.0:
		print("Lunch time")
	if 18.0 <= convert(time) <= 19.0:
		print("Dinner time")

def convert(time):
	hours, minutes = time.split(":")
	hours = float(hours)
	minutes = float(minutes)
	minutes = minutes / 60.0
	return hours + minutes

if __name__ == "__main__":
	main()		
