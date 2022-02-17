# improved_chaos.py

def main():
    print("This program illustrates a chaotic function.")
    
    x = eval(input("Enter a number between 0 and 1: "))
    y = eval(input("Enter another number between 0 and 1: "))
    n = eval(input("How many iterations: "))

    print()
    print(f"index          {x}         {y}")
    print("----------------------------------")
    for i in range(n):
        x = 3.9 * x * (1-x)
        y = 3.9 * y * (1-y)
        print(f" {i+1:3}         {x:.6f}     {y:.6f}")

main()
