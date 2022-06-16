word = input("What is your word? ")

for letter in word:
    if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
        None
    else:
        print(letter, end="")

def main():
    word = input("What is your word? ")
    letter_in_word(word)

def letter_in_word(word):
    for letter in word:
        if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
            None
        else:
            print(letter, end = "")

main()
