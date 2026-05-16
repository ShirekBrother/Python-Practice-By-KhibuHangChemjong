import os
from random import randint
import time 

#step 1: take password from the user

password = input("Send the password : ")

# Step 2: Define all possible character

keys = [
    "1","2","3","4","5","6","7","8","9","0",
    "a","b","c","d","e","f","g","h","i","j",
    "k","l","m","n","o","p","q","r","s","t",
    "u","v","w","x","y","z","@","#","$","%"
]
 #Step 3: Initialize variable
pwg=""
attempts=0
start_time=time.time()

#Step 4: Keep guessing until password match
while pwg!= password:
    pwg=""
    attempts +=1


    #Step 5: generate the random password of same length
    for i in range(len(password)):
        guessPass = keys[randint(0, len(keys)-1)]        
        pwg=str(guessPass)+str(pwg)
        print(pwg)
        print("Attacking........please wait!")
        os.system("cls")

#step 6: Calculate total time
end_time=time.time()
total_time=end_time-start_time


#Step 7: Show final result

print(f"The password is : {pwg}")
print(f"Total Attempts: {attempts}")
print(f"Total time taken : {total_time:.2f} seconds")