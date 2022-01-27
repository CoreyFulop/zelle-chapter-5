# numeric_value.py

def main():
    print("This program produces the 'numeric value' of a name.")
    name = input("Please enter the name to analyse: ")

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    count = 0
    for letter in name:
        count += (alphabet.index(letter.lower()) + 1)

    print(f"The 'numeric value' of {name} is {count}.")

main()