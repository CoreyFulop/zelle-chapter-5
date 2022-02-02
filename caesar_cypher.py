# caesar_cypher.py
# A simple Caesar cypher using the Unicode character set.

def main():
    print("This program encodes a message using a Caesar cypher.")
    message = input("Enter the message to encode: ")
    key = eval(input("Please enter the key for the cypher: "))

    encoded_characters = []
    for ch in message:
        encoded_characters.append(chr(ord(ch) + key))

    encoded_message = "".join(encoded_characters)

    print(f"The encoded message is {encoded_message}.")

main()