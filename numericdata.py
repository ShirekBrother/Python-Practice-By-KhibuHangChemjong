# Exercise 1: Numeric Data

# Create two variables num_1 as 7, num_2 as 3.5 and:

num_1=7
num_2=3.5

# Display their data types
print(type(num_1))
print(type(num_2))

# Display their sum

total=num_1+num_2
print("The sum is ", total, ".")


# Display their difference

print(f"The difference of {num_1} and {num_2} is {num_1-num_2} .")

# Display their product

print(f"The prodecct of {num_1} and {num_2} is {num_1*num_2} .")

# Display their division

print(f"The division of {num_1} and {num_2} is {num_1/num_2} . ")

# Convert both num_1 and num_2 into string and display sum again

string_1, string_2=str(num_1), str(num_2)
total = string_1+string_2
print("The sum of the two string is ", total, "." )

# Repeat above exercise but with storing both variables with a complex number

com_1=7+3j
com_2=3+7j

print(f"The sum of the {com_1} and {com_2} is {com_1+com_2} .")
print(f'The difference of the {com_1} and {com_2} is {com_1-com_2} .')
print(f"The product of the {com_1} and {com_2} is {com_1*com_2} .")
print(f"The division of the {com_1} and {com_2} is {com_1/com_2} .")

string_3, string_4=str(com_1), str(com_2)
print(f"The sum of the {string_3} and {string_4} is {string_3+string_4} .")
print(type(string_3))
print(type(string_4))

# Create variable num_3 as 15 and num_4 as 4. Swap their values and display the result
num_3=15
num_4=4
num_3,num_4=num_4, num_3
print("The swaped number of num_3 is ", num_3, ".")
print("The swaped number of num_4 is ", num_4, ".")


# Exercise 2: Assignment Operators


# Assign mark_1, mark_2, mark_3 with value 78, 85, 92. Calculate total and average mark

mark_1=78
mark_2=85
mark_3=92
print(f"The total mark is {mark_1+mark_2+mark_3}.")
print(f"The average of the above mark is {(mark_1+mark_2+mark_3)/3}. ")

# Assign weight_1, weight_2, weight_3, weight_4 all having value as 70

weight_1=70
weight_2=70
weight_3=70
weight_4=70

# Add 5 to weight_1 and reassign to weight_1
new_weight=weight_1+5
weight_1=new_weight
print(new_weight)
print(weight_1)

# Subtract 10 from weight_2 and reassign to weight_2

new_weight=weight_2-10
print(new_weight)
weight_2=new_weight
print(weight_2)

# Multiply weight_3 by 1.1 and reassign to weight_3

new_weight=int(weight_3*1.1)
weight_3=int(new_weight)
print(new_weight)
print(weight_3)

# Divide weight_4 by 2 and reassign to weight_4

new_weight=int(weight_4/2)
weight_4=new_weight
print(weight_4)

# Assign variable my_num as 15. Find remainder when divided by 2 as reassign to itself

my_num=15
reminder=15%2
my_num=reminder
print(my_num)

# Find the value when 1.1 is raised to the power of 3 i.e. 1.1 ^ 3. Assign is to result
hello_num=1.1
power=1.1**3
hello_num=power
print(hello_num)


# Exercise 3: Comparison & Logical Operators


# Assign your age to variable my_age and:

my_age=24

# Check if your age 16

if my_age==16:
    print("You are sweet teenager.")
else:
    print("You are not sweet teenager.")   

# Check if your age is not 70

if my_age !=70:
    print("You are not the old guy.")

# Check if you are a child (age less than 13)

if my_age<=13:
    print("You are a child.")
else:
    print("You are not a child.")    

# Check if you are an adult (age 20 or above)

if my_age>=20:
    print("You are an adult.")

# Check if you are eligible to vote (18+ can vote)

if my_age>=18:
    print("You are eligible for voting.")

# Check if you are a teenager (age between 13 and 19) 

if my_age>=13 and my_age<=19:
    print("You are a teenager.")
else:
    print("You are not the teenager.")    


# Check if you lie on passive population (below 5 and over 65 considered passive)

if my_age<5 or my_age>65:
    print("You are a passive population.")
else:
    print("You are not the passive population.")    

# Check if you are eligible for driving license (age between 18 and 65)

if my_age>=18 and my_age<65:
    print("You are eligible for the driving liscence. ")


# Exercise 4: Membership Operators


# Assign variable my_name as your name and check if:

my_name="Salma"

# Letter a is in your name

print("a" in my_name)

# Letter a is not in your name

print("a" not in my_name)

# Assign variable movie_collection as a list of your favorite movies and check if:

movie_collection=["Iron_man", "Spider_man", "Shrek", "Puss_in_boot"]

# Movie Avatar is in your collection

print("avater" in movie_collection)

# Movie Avatar is not in your collection

print("avater" not in movie_collection)

# Repeat exercise 2 but creating movie_collection as a tuple

movies_collection=("Iron_man", "Spider_man", "Shrek", "Puss_in_boot")

print("avater" in movies_collection)

print("avater" not in movies_collection)

# Repeat exercise 2 but creating movie_collection as a set

movie_collections={"Iron_man", "Spider_man", "Shrek", "Puss_in_boot"}

print("avater" in movie_collections)

print("avater" not in movie_collections)