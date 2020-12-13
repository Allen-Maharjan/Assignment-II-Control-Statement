#determining palindrome

def is_palindrome(sample):
    if (sample == sample[::-1]):
        print(f"{sample} is palindrome")
    else:
        print("Is not palindrome")

is_palindrome(input("Enter a string: "))
