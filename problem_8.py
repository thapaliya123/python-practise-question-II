"""
8. Write a function, is_prime, that takes an integer and returns True if
the number is prime and False if the number is not prime.
"""

def is_prime(sample_number):
    prime = "prime"
    for i in range(2, (sample_number//2)+1):
        if(sample_number%i==0):
            prime = "not prime"
            break
    return f"The number is {prime}"

sample_number = int(input("Enter any number you want to check prime"))
print(is_prime(sample_number))