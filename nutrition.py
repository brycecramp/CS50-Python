fruit = {
  "apple" : "130",
  "orange": "80",
  'strawberries' : "50"
}

choice = input("Which fruit would you like to know? ").lower()

if choice in fruit:
    print(choice, fruit[choice], sep = "=")
else:
    print("Fruit not in database")
