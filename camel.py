camel = input("Please input your camel name: ")

build = ""

for c in camel:
    if c.isupper() == True:
        c = "_" + c.lower()
    build += c

print("Snakename: " + build)
