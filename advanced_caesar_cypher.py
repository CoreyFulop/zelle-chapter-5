# advanced_caesar_cypher.py

def main():
    print("This program encodes a message using a Caesar cypher.")
    in_message = input("Enter the message to encode: ")
    key = eval(input("Enter the key for the cypher: "))

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    message = in_message.lower()

    encoded_words = []
    for word in message.split():
        encoded_word = []
        for ch in word:
            position = alphabet.index(ch) + key
            if position > 25:
                encoded_word.append(alphabet[position%26])
            else: 
                encoded_word.append(alphabet[position])
        encoded_words.append("".join(encoded_word))
    encoded_message = " ".join(encoded_words)

    print(f"The encoded message is '{encoded_message}'.")

main()