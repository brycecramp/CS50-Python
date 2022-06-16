total = 0
coins = 0

while total < 50:
    print("Amount due =", 50 - total)
    coins = int(input("Please enter your coins:"))
    total += coins

print("Change = ", total - 50)
