"""
17. Write a program that serves as a basic calculator. It asks for two
numbers, then it asks for an operator. Gracefully deal with input that
doesn't cleanly convert to numbers. Deal with division by zero errors.
"""
def add(sample_num_one, sample_num_two):
    print(f"addition of number is {sample_num_one+sample_num_two}")

def mul(sample_num_one, sample_num_two):
    print(f"multiplication of number is {sample_num_one*sample_num_two}")

def sub(sample_num_one, sample_num_two):
    print(f"substraction of number is {sample_num_one-sample_num_two}")

def divide(sample_num_one, sample_num_two):
    try:
        print(f"the division of number is {sample_num_one/sample_num_two}")
    
    except ZeroDivisionError:
        print("division by zero")

sample_num_one = int(input("enter first number"))
sample_num_two = int(input("enter second number"))

operator = input("enter any operator between +, -, *, /")

if operator == "+":
    add(sample_num_one, sample_num_two)

elif operator == "-":
    sub(sample_num_one, sample_num_two)

elif operator == "*":
    mul(sample_num_one, sample_num_two)

elif operator == "/":
    divide(sample_num_one, sample_num_two)