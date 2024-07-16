# This program is going to find the whether a number is a triangular number
import math

def sqrtFunc(num):
    sqrtValue = math.sqrt(num)
    return math.floor(sqrtValue)**2 == num

def main():
    userInput = int(input("Guess the triangular number: "))
    test_value = 1+8*userInput
    if sqrtFunc(test_value):
        print(f"{test_value} - This is a Triangular Number")
    else:
        print(f"{test_value} - This is NOT a Triangular Number")


if __name__ == "__main__":
    main()