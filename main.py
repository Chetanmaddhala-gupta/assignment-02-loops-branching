number = int(input("Enter an integer: "))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

print(f"Multiplication table for {number}:")
for multiplier in range(1, 11):
    print(f"{number} x {multiplier} = {number * multiplier}")

while True:
    answer = input("Would you like to see another table? (y/n): ").strip().lower()
    if answer == "n":
        print("Goodbye!")
        break
    if answer == "y":
        number = int(input("Enter an integer: "))
        for multiplier in range(1, 11):
            print(f"{number} x {multiplier} = {number * multiplier}")
    else:
        print("Please enter y or n.")
