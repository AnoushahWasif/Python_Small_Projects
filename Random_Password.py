import string
import random

characters = list(string.ascii_letters + string.digits + string.punctuation)

def random_password(length):
    password = ""
    for i in range(length):
        password += random.choice(characters)
    return password

length = int(input("Enter the length of the password: "))
print("Your password is: " + random_password(length))