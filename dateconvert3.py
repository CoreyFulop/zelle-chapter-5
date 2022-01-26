# dateconvert3.py
# Converts day month and year numbers into two date formats.
# Instead of using the string-formatting method in the text, I'll just use f-strings.

def main():
    # Get the day month and year
    day, month, year = eval(input("Enter the day, month, and year numbers: "))

    date1 = f"{month}/{day}/{year}"

    months = ["January", "February", "March", "April",
              "May", "June", "July", "August",
              "September", "October", "November", "December"]

    monthStr = months[month-1]

    date2 = f"{monthStr} {day}, {year}"

    print(f"The date is {date1}, or {date2}.")

main()