d = {}
count = 1

while True:
    try:
        item = input("Item: ")
    except EOFError:
        break
    else:
        if item in d:
            count += 1 
        else:
            d[item] = 1

print(count, d)
