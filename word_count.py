# word_count.py

def main():
    print("This program counts the number of words in a sentence.")
    sentence = input("Please enter the sentence: ")

    count = 0
    for word in sentence.split():
        count += 1

    print(f"The numbers of words in the sentence is {count}.")

main()