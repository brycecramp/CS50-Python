groceries = {}

while True:
    try:
        item = input("Item: ").upper()
    except EOFError:
        print()
        break
    if item in groceries:
        groceries[item] += 1
    else:
        groceries[item.upper()] = 1

for item in sorted(groceries.keys()):
    print(groceries[item], item)
