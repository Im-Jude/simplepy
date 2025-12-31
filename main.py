import os

def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

def main():
    env_number = os.getenv("TEST_NUMBER")

    if env_number is not None:
        try:
            number = int(env_number)
        except ValueError:
            print("Environment variable TEST_NUMBER must be an integer.")
            return
    else:
        try:
            number = int(input("Enter a number: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            return

    result = check_number(number)
    print(f"The number {number} is: {result}")

if __name__ == "__main__":
    main()
