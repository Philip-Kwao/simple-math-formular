# This is a sepearte file that will use the formula function in the perfectSquare.py file

from perfectSquare import perfect__square_func

number = int(input("Guess the perfect number: "))
if perfect__square_func(number):
    print("Yes! This is a perfect number")
else:
    print("Naah! This number ain't perfect, try again")