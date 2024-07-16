# This program is going to find the Highest Common Factor and the Lowest Common Multiple when two numbers are given by the user.

def hcf(num1, num2):
    if num1 == num2:
        return num1
    elif num1>num2:
        return hcf(num1-num2, num2)
    else:
        return hcf(num1,num2-num1)
    
input1, input2 = input("Enter 2 numbers: ").split()
input1, input2 = int(input1), int(input2)

print(f"The Highest Common Factor of {input1} and {input2} is {hcf(input1,input2)}")
print(f"The Lowest Common Multiple for {input1} and {input2} is {(input1*input2)//hcf(input1,input2)}")
