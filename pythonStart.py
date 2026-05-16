# Exercise 1: For Colab


# Write a code to display Hello, Python!

print("Hello, Python!")

# Initialize a as -5 and b as 10.45

a=-5
b=10.45

# Display their sum

print(f"The sum of a and b is {a+b}.")

# Display their difference

print(f"The difference of a and b is {a-b}.")

# Display their product

print(f"The product of a and b is {a*b}.")

# Display their division

print(f"The division of a and b is {a/b}.")

# # Display their remainder

print(f"The reminder is {a%b}.")


# Exercise 2: For VS-Code

# Create a folder PythonBasics. Inside it create separate file for each questions

# Normal human temperature is 98.6 °F. Convert it to Celsius. C = (F - 32)/1.8

farenight=98.6
celsius=(farenight-32)/1.8
print(f"98.6 F is equivalent to {celsius}. ")

# Calculate simple interest for Rs. 50,000 at rate 6.5% p.a for 4 years. SI = PTR/100

principal=50000
rate=6.5
time=4
SI=(principal*rate*time)/100
print(f"The simple interrest is {SI}.")

# Calculate area & perimeter of circle with diameter 12 cm. A=πr², P=2πr

d=12
r=d/2
pi=22/7
area=pi*r*r
perimeter=2*pi*r
print(f"Hence, The area is {area} and the perimeter is {perimeter}.")

# Calculate the total seconds in 3 hours, 20 minutes and 45 seconds.

print(f"The total seconds in 3 hours 20 minutes and 45 seconds is {3*60*60+20*60+45}seconds. ")

# Calculate the average of 5 subjects where marks are: 78, 85, 62, 90, 88.

print(f"The average of the 5 subjects where the marks are 78,85,62,90 and 88 is {(78+85+62+90+88)/5}.")

# Convert the distance of 15 kilometers to miles. 1 km = 0.621371 miles

print(f"15 kilometers is equivalent to {15*0.621371} miles.")

# Calculate the BMI for a person with weight 70 kg and height 1.75 m. BMI = wt / ht²)

weight=70
height=1.75
BMI=weight/(height*height)
print("The BMI of the person is", BMI, ".")