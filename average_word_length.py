# average_word_length.py

def main():
    print("This program finds the average word length in a sentence.")
    in_sentence = input("Enter a sentence: ")
    
    word_list = in_sentence.split()

    letter_count = 0
    for word in word_list:
        for letters in word:
            letter_count += 1

    average_word_length = letter_count / len(word_list)

    print(f"The average word length in that sentence is {average_word_length}.")

main()
