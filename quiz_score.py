# quiz_score.py

def main():
    print("This program provides the letter grade for a five-point quiz.")
    score = eval(input("Enter the number of correct marks (out of 5): "))

    grades = "FFDCBA"

    grade = grades[score]

    print(f"The letter grade for a score of {score} is {grade}.")

main()