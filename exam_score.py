# exam_score.py

def main():
    print("This program determines the letter grade from an exam score.")
    score = eval(input("Enter the exam score (out of 100): "))

    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else: # score < 60
       grade = "F"

    print(f"The grade for a score of {score} is {grade}.")

main()