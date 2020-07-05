"""
12. Create a function, is_palindrome, to determine if a supplied word is
the same if the letters are reversed.
"""

def is_palindrome(sample_str):
    reversed_str = sample_str[-1::-1]
    if sample_str==reversed_str:
        return f"{sample_str} is palindrome"
    else:
        return f"{sample_str} is not palindrome"

sample_str = "naban"
sample_str_one = "check"

print(is_palindrome(sample_str))
print(is_palindrome(sample_str_one))