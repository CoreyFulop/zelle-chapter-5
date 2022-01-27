# acronym_generator.py

def main():
    print("This program produces an acronym from a given phrase.")
    
    phrase = input("Please enter a phrase: ")
    
    words = phrase.split()

    acronym_list = []
    for word in words:
        acronym_list.append(word[0])

    acronym = "".join(acronym_list)
    
    upper_acronym = acronym.upper()

    print(f"The acronym for {phrase} is {upper_acronym}.")

main()