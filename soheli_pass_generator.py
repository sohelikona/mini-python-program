import string
import random

characters = list(string.ascii_letters + string.digits + "~!@#$%^&*()_+_-][}{|?/")

def generate_password():
    password_length = int(input("Welcome Soheli. How long would you like your password to be? "))
    print("Here is your password below")
    print("")
    print("")


    random.shuffle(characters)



    password = []


    for x in range(password_length):
        password.append(random.choice(characters))


    

    random.shuffle(password)



    password = "". join(password)


    print("PASSWORD:      " + password)


generate_password()

print("")
print(" Thanks fpr using Soheli Passw0=ord Generator!🥰 ")