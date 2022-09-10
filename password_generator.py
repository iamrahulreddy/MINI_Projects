#Password Generator

import random

password_length = int(input("enter the length of password\n"))

alphanumericspecialchars_for_password="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!0123456789@#$%^&*()?"

password = "".join(random.sample(alphanumericspecialchars_for_password,password_length))

print(password)