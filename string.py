# Exercise 1: Storing String


# Create a variable that stores your name and display it.

your_name="Utshav"
print(your_name)

# Store text I'm learning Python in a variable and display it.

variable="I'm learning Python in a variable"
print(variable)

# Store text Ram said, "I've a pen." in a variable and display it.

text='''Ram said, "I've a pen."'''
print(text)

# Store below text in a variable (as multiline) and display it.
# Dear Manager,
# I am on leave!
# Thanks

multiline="""Dear Manager
I am on leave!
Thanks"""
print(multiline)

# Store \n and \t are special character. We use \ to escape in a variable and display it.

greet="Dear\tManager"
print(greet)
tab="I am on leave!\nThanks"
print(tab)

# Exercise 2: Indexing and Slicing


# Create a variable my_str that stores We are learning Python and it's fun! and

my_str="We are learning Python and it's fun!"

# Find and display the first character.

print(my_str[0])

# Find and display the character at index 8.

print(my_str[8])

# Find and display the last character (using negative indexing).

print(my_str[-1])

# Find word Python using slicing and display it.

print(my_str[16:23])

# Find word fun using negative slicing and display it.

print(my_str[-4:-1])

# Find text lrn (i.e. only some part of text learning) and display it.

print(my_str[7:15:3])

# Reverse the string and display it.

print(my_str[::-1])

# Find sub-string that lies from 5th index till end and display it.

sub_index=my_str[5:]
print(sub_index)

# Find sub-string that lies from start till 10th index and display it.

sub_indexes=my_str[:10]
print(sub_indexes)

# Exercise 3: Generic functions


# Create a variable str_1 that stores Hello, str_2 that stores World and:

str_1="Hello"
str_2="World"

# Display HelloWorld by concatenating both strings.

print(str_1+str_2)


# Assign greetings variable as Hello World by concatenating both strings and display it.

greetings=str_1 + " "+ str_2
print(greetings)

# Assign my_str as HelloHelloHello using str_1 repetition.

my_str=str_1*3
print(my_str)

# Find and display number of characters in string my_str.

length=len(my_str)
print("The number of the characters in sstring my_str is ",length, ".")

# Change value of greetings variable to uppercase and display it.

upperCase=greetings.upper()
print(upperCase)

# Change value of greetings variable to lowercase and display it.

lowerCase=greetings.lower()
print(lowerCase)

# Change value of greetings variable to title case and display it.

title=greetings.title()
print(title)

# Swap the case of characters in greetings variable and display it.

swapped=greetings.swapcase()
print(swapped)

# Exercise 4: Data Check Functions


# Assign str_1 as "Hello", str_2 as "12345", str_3 as "##abc123##" and str_4 as " "

str_1="Hello"
str_2="12345"
str_3="###abc123###"
str_4=" "

# Check and display if str_1 has alphabetic characters only.

is_alpha=str_1.isalpha()
print(is_alpha)

# Check and display if str_1 has numeric characters only.

is_numeric=str_1.isnumeric()
print(is_numeric)

# Check and display if str_2 has alphanumeric characters only.

is_alphanumeric=str_2.isalnum()
print(is_alphanumeric)

# Check and display if str_4 is empty.

if str_4=="":
    print("The sting 4 is empty.")
else:
    print("The string 4 is not empty.")  

# Check and display if str_3 starts with abc

start_abc=str_3.startswith("abc")
print(start_abc)

# Check and display if str_3 ends with 3

end_three=str_3.endswith("3")
print(end_three)

# Check and display if str_1 starts with He and ends with lo

is_really=str_1.startswith("He") and str_1.endswith("lo")
print(is_really)

# Remove leading and trailing # from str_3 and display the result

removing=str_3.strip("#")
print(removing)

# Remove leading # from str_3 and display the result

removed_value=str_3.lstrip("#")
print(removed_value)

# Exercise 5: Data Manipulation & Cleanup


# Assign file_name as report_2026.pdf. Split it to get file name and extension and display them.

file_name="report_2026.pdf"
split_file=file_name.split(".")
print(split_file)

# Store my_date as 2026-03-05. Split it into list of year, month, day and display result

my_date="2026-03-05"
new_date=my_date.split("-")
print(new_date)

# Store my_str as PYTHON. Use join function to display P.Y.T.H.O.N

my_str="PYTHON"
new_str=".".join(my_str)
print(new_str)

# Store laptop_names as ['Dell', 'HP', 'Apple']. Use join function to display Dell-HP-Apple

laptop_names=['Dell', 'HP', 'Apple']
new_names="-".join(laptop_names)
print(new_names)

# Assign str_1 as Hello, World!. Replace World with Python and display the result.

str_1="Hello, World!"
new_str=str_1.replace("World", "Python")
print(new_str)

# Assign str_2 as 2026-03-01.csv. Replace - with / and display the result.

str_2="2026-03-01.csv"
replacing=str_2.replace("-", "/")
print(replacing)

# Assign str_3 as Pineapple. Find at which index apple starts and display the result.

str_3="Pineapple"
find_apple=str_3.find("apple")
print(find_apple)

# Assign my_name as your name. Count the number of vowels in it and display the result.

my_name="salmachemjong"
vowel=my_name.lower()
num_vowel=vowel.count("a")+vowel.count("e")+vowel.count("i")+vowel.count("o")+vowel.count("u")
print(num_vowel)

# Assign my_str as Hello, World!. Count and display occurrence of letter l in it.

my_str="Hello, World!"
letter=my_str.count("l")
print(letter)