# wc.py

def main():
    print(f"This program analyses a text file.")
    
    infile_name = input("Enter the text file to analyse: ")

    infile = open(infile_name, "r")

    line_count = 0
    char_count = 0
    word_count = 0

    for line in infile:
        line_count += 1
        char_count += len(line) # Includes the newline character
        word_list = line.split()
        for word in word_list:
            word_count += 1

    print()
    print(f"{infile_name} statistics")
    print("---------------")
    print(f"Lines: {line_count}")
    print(f"Words: {word_count}")
    print(f"Characters: {char_count}")
    
    infile.close()

main()