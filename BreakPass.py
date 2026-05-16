import os
from random import randint
import time

password = input("Enter password: ")

keys = [
    "1","2","3","4","5","6","7","8","9","0",
    "a","b","c","d","e","f","g","h","i","j",
    "k","l","m","n","o","p","q","r","s","t",
    "u","v","w","x","y","z","@","#","$","%"
]

pwg = ""
attempts = 0
start_time = time.time()

while pwg != password:
    pwg = ""
    attempts += 1

    for i in range(len(password)):
        guessPass = keys[randint(0, len(keys)-1)]
        pwg += guessPass
        print("Attacking........please wait!")
        os.system("cls" if os.name == "nt" else "clear")
    print(pwg)

end_time = time.time()

print(f"\nPassword found: {pwg}")
print(f"Total Attempts: {attempts}")
print(f"Time taken: {end_time - start_time:.2f} seconds")