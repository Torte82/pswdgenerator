import random
import string
import pyperclip

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")


def random_gen():
    length = int(input("Enter password length: "))
    random.shuffle(characters)
    password = []
    for i in range(length):
        password.append(random.choice(characters))
    random.shuffle(password)
    print("".join(password))
    pyperclip.copy("".join(password))

def print_last():
    print("password has been copied to clipboard")

spam = pyperclip.paste()
random_gen()
print_last()