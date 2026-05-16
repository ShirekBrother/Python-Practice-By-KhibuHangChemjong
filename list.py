# Exercise 1: Basic Operations


# Store student info as: [[name_1, age_1], [name_2, age_2], ...]. Display 2nd student's age.

std_info=[["Salma", 22], ["Utshav", 24]]
print(std_info[0][1])

# Assign marks in five subjects to mark_list and subject names in subject_list. Display:

marks_list=[89, 65, 78, 86, 94]
subject_list=["Science", "English", "Social", "Computer", "Math"]

# total, average, highest and lowest marks obtained by student

total=sum(marks_list)
print("The total mark is",total, ".")

average=total/5
print(f"The average mark is {average} .")

highest_mark=max(marks_list)
print(f"The highest mark is {highest_mark} in {subject_list[marks_list.index(highest_mark)]} .")

lowest_mark=min(marks_list)
print(f"The lowest mark is {lowest_mark} in {subject_list[marks_list.index(lowest_mark)]} .")

# Change name of 2nd subject (1st index) to Python and display updated list

subject_list[1]="Python"
print(subject_list)

# Marks obtained in subject at 3rd position (2nd index) as Mark obtained in English is 89

print(f"The mark obtained in 3rd position ie {subject_list[2]} is {marks_list[2]} .")

# Marks obtained in subject at second last position with similar format as above.

print(f"The mark obtained in last position ie {subject_list[-1]} is {marks_list[-1]} .")

# Marks obtained in last two subjects

print(f"The marks obtained in last two subjects ie {subject_list[-2:]} are {marks_list[-2:]} .")

# Marks in first three subjects

print(f"The marks obtained in first three subjects ie {subject_list[:3]} are {marks_list[:3]} .")


# Name of subject in which student scored highest marks

print(f"The name of the subject in which student scored highest mark is {subject_list[marks_list.index(highest_mark)]} .")


# Name of subject in which student scored lowest marks


print(f"The name of the subject in which the student scored lowest mark is {subject_list[marks_list.index(min(marks_list))]}")


# Number of subjects in which student scored 80

print(f"The number of subjects that student scored 80 are {marks_list.count(80)}")


# Exercise 2: Modifying List


# Books details are stored as [harry_potter, lord_of_rings, harry_potter, ...]

book_details=['harry_potter', 'lord_of_rings', 'harry_porter']

# Find the position of first occurrence of harry_potter

print(f"The first occurance of harry_porter is {book_details.index('harry_potter')} .")

# Remove the first occurrence of harry_potter and display the list

removed_harry=book_details.remove('harry_potter')
print(book_details)

# Ask user for a book name and check if its present in list

book_name=input("Enter a book name : ")
print(book_name in book_details)


# Add the_hobbit to the end of list and display it

book_details.append('the_hobbit')
print(book_details)

# Insert game_of_thrones at index 2 and display the list

book_details.insert(2, "game_of_thrones")
print(book_details)

# Count and display how book for lord_of_rings is present in the list

print(f"The no. of book for lord_of_rings is {book_details.count('lord_of_rings')} ")


# Remove book from 2nd position. Display removed book and original list


removed_book=book_details.pop(2)
print(removed_book)
print(book_details)

# Display the total number of books in the list

print(f"The total no. of books are {len(book_details)} .")


# Display all books of list separated by comma

print(",".join(book_details))

# Assign book_2 as [math, science, history]. Add all books from it to above list and display.

book_2=['math','science', 'history']
book_details.extend(book_2)
print(book_details)

# Sort the list in descending order based on length of book name and display result.

sorted_books=book_details.sort(reverse=True,key=len)
print(book_details)