# numeric_value_full_name.py

def main():
    print("This program determines the 'numeric value' of a full name.")
    full_name = input("Please enter the full name to analyse: ")

    alphabet ="abcdefghijklmnopqrstuvwxyz"

    sum = 0
    for name in full_name.split():
        for letter in name:
            sum += (alphabet.index(letter.lower()) + 1)

    print(f"The numeric value of {full_name} is {sum}.")

main()
