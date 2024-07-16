# This is a program to find if the inputted number is a perfect square

# Importting Math in order to use square root method
import math

# This function defines the formula to be used for the computation and returns a boolean result to be used by other functions
def perfect__square_func(num):
    squared_value = math.sqrt(num)
    # print(squared_value)
    return (math.ceil(squared_value)**2)  == num

# This function recieves the user input and performs a boolean condition to check if the statement is true or false
def main():
# Receive user input here
    number = int(input("Guess the perfert square number: "))
    if (perfect__square_func(number)):
        print("TRUE! This is a perfect number")
    else:
        print("SORRY, This is NOT a perfect number")

# This line of code is to prevent the main function to run when perfect__square_func() is called in the other file.
if __name__ == "__main__":
    main()