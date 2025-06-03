import random
import string

def generate_password(length, use_letters=True, use_digits=True, use_symbols=True):
    chars = ""
    if use_letters:
        chars += string.ascii_letters
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation

    if not chars:
        raise ValueError("At least one character type must be selected.")

    return ''.join(random.choices(chars, k=length))

try:
    length = int(input("Enter desired password length: "))
    if length <= 0:
        raise ValueError("Password length must be positive.")
    
    password = generate_password(length)
    print(f"Your password is: {password}")

except ValueError as e:
    print(f"Invalid input: {e}")
    

