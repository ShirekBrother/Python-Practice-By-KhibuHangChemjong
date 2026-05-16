# Exercise 1: Variable


# Create a variable to store your name and print it

name="Salma"
print(name)

# Create a variable to store your age and print it

age=22
print(age)

# Create a constant to store the value of pi (3.14159) and print it

pi=3.14159
print(pi)

# Create a variable to store a boolean value (is_nepali) and print it

is_boolean="is_nepali"
print(bool(is_boolean))

# Exercise 2: Data Types and Type Conversion


# Assign num_int as 15. Display its datatype. Convert it to float and string, display again

num_int=15
print(type(num_int))
num_float=float(num_int)
num_string=str(num_int)
print(f"The floating number of {num_int} is {num_float} and the string is {num_string} .")
print(type(num_float))
print(type(num_string))

# Assign num_str as "25". Add 10 to it after data type conversion and print the result

num_str="25"
num_integer=int(num_str)
add=num_integer+10
print("Hence, the result after adding 10 is", add, ".")

# Assign float_num as 10.5. Convert it to string, add '10' and print the result

float_num=10.5
string_num=str(float_num)
adding=string_num+'10'
print("The result is ", adding, ".")

# Assign is_active as True. Convert it to string and print the result and its data type

is_active=True
is_string=str(is_active)
print(is_string)
print(type(is_string))

# Assign num_1 as '5' and num_2 as '2.5'. Convert both to float and print their sum

num_1='5'
num_2='2.5'
float_1, float_2=float(num_1), float(num_2)
sum=float_1+float_2
print(f"The sum of the {float_1} and {float_2} is {sum} .")