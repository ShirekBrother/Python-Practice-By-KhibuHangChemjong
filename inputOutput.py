# Exercise 1: Output and Formatting


# Ask user for name and price of a pen. display in format: Ram bought a pen for $ 10.56

your_name=input("Enter your name : ")
price=input("Enter a price of pen : ")
print(f"{your_name} bought a pen for $ {price} .")

# Ask user for name, price of three product. Display it in format as:
# Item        Price
# --------------------
# Apple       Rs.   3
# Banana      Rs.  10
# Orange      Rs. 200

name=input("Enter  your name : ")
apple_price=int(input("Enter a price of an apple : "))
banana_price=int(input("Enter a price of a banana : "))
orange_price=int(input("Enter a price of an orange : "))

print(f"{'Item':<12} {'Price':>5} ")
print("-"*22)
print(f"{'Apple':<12} Rs. {apple_price:>5}")
print(f"{'Banana':<12} Rs. {banana_price:>5}")
print(f"{'Orange':<12} Rs. {orange_price:>5}")

# Note: Item is left aligned with width of 12 and price is right aligned with width of 3

# Ask user for current year, month and day. Display it in format: Today's Date: 2023-03-12

current_year=int(input("Enter current year : "))
current_month=int(input("Enter current month : "))
current_day=int(input("Enter current day : "))
current_date="-".join([str(current_year), str(current_month), str(current_day)])
print(f"Today's date : {current_date} ")

# Ask user for name and marks in 3 subject. Display result as: Hari scored 85.5% in exam.

name=input("Enter your name : ")
math_marks=int(input("Enter a marks in maths : "))
science_marks=int(input("Enter a marks in science : "))
english_marks=int(input("Enter a marks in english : "))
percent=(math_marks+science_marks+english_marks)/3
print(f"{name} scored {percent}% in exam . ")

# Exercise 2: User Input


# Ask user for his/her name and display: Hello, <name>!

user_name=input("Enter your name : ")
print(f"Hello, {user_name }!")

# Ask user for his/her birth year. Calculate and display his/her age

birth_year=int(input("Enter your birth year : "))
print(f"You are {2026-birth_year} years old .")

# Ask user for mass and length of a cube. Calculate and display its density (d = m/v)

mass_of_cube=int(input("Enter a mass : "))
length_of_cube=int(input("Enter a length : "))
density=mass_of_cube/length_of_cube
print("The density of the cube is", density, ".")

# Ask user for length in feet and convert and display its value in meter (1 ft = 0.3048 m)

length_in_feet=int(input("Enter a length in feet : "))
meter=length_in_feet*0.3048
print(f"{length_in_feet} feets is equivalent to {meter} meters .")

# Ask user for a file name in format file.ext. Extract and display file extension from it

file_name="file.ext"
file_split=file_name.split(".")
print(file_split[-1])

# Ask user for a sentence and display number of words in it.

user_sentence=input("Enter a sentence : ")
sentence_split=user_sentence.split(" ")
count_sentence=len(sentence_split)
print(f"The number of the words in the given sentences are {count_sentence} . ")

# Ask user for two numbers and display their sum, difference, product and quotient.

num_1=int(input("Enter First Number : "))
num_2=int(input("Enter Second Number : "))
operation=input("Enter a opertion(+,-,/,*) : ")

if operation=="+":
    print(f"The addition of {num_1} and {num_2} = {num_1+num_2} . ")
elif operation=="-":
    print(f"The subtraction of {num_1} and {num_2} = {num_1-num_2} .")
elif operation=="/":
    print(f"The division of {num_1} and {num_2} = {num_1/num_2} .")
elif operation =="*":
    print(f"The multiplication of {num_1} and {num_2} = {num_1*num_2} . ")
    
# Note: Output displayed should be in proper human interpretable format not just number