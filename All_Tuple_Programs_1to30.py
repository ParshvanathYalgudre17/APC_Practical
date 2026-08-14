#1. Write a Python program to create a tuple of five integers and display it.
t = (10, 20, 30, 40, 50)
print("Tuple:", t)

print("---------------------------------------------------------------------------------------------------------------------------------------------")



#2. Create a tuple containing five city names. Display:
#•  First city 
#•  Last city 
#•  Third city
cities = ("Pune", "Mumbai", "Kolhapur", "Solapur", "Sangli")

print("First city:", cities[0])
print("Last city:", cities[-1])
print("Third city:", cities[2])
print("---------------------------------------------------------------------------------------------------------------------------------------------")

#3. Create a tuple of student names and display the total number of students using the len() function.
students = ("Rahul", "Amit", "Sneha", "Priya", "Neha")

print("Students:", students)
print("Total students:", len(students))
print("---------------------------------------------------------------------------------------------------------------------------------------------")


#4. Create a tuple of colors. Check whether a given color exists in the tuple

colors = ("Red", "Blue", "Green", "Yellow", "Black")

color = input("Enter a color: ")

if color in colors:
    print("Color exists in the tuple")
else:
    print("Color does not exist")
print("---------------------------------------------------------------------------------------------------------------------------------------------")



#5. Create a tuple of fruits and display each fruit using a loop.
fruits = ("Apple", "Mango", "Banana", "Orange", "Grapes")

for fruit in fruits:
    print(fruit)
print("---------------------------------------------------------------------------------------------------------------------------------------------")



#6. Create a tuple with repeated numbers and count how many times a particular number appears.
numbers = (10, 20, 10, 30, 10, 40, 10)

n = int(input("Enter number: "))

print(n, "appears", numbers.count(n), "times")
print("---------------------------------------------------------------------------------------------------------------------------------------------")



#7. Create a tuple of employee IDs and find the index of a given ID.
employee_ids = (101, 102, 103, 104, 105)

id = int(input("Enter employee ID: "))

if id in employee_ids:
    print("Index:", employee_ids.index(id))
else:
    print("ID not found")
print("---------------------------------------------------------------------------------------------------------------------------------------------")



#8. Create two tuples of numbers and concatenate them into a single tuple.
t1 = (10, 20, 30)
t2 = (40, 50, 60)

t3 = t1 + t2

print("Combined tuple:", t3)
print("---------------------------------------------------------------------------------------------------------------------------------------------")




#9. Create a tuple containing three elements and repeat it four times.
t = (10, 20, 30)

result = t * 4

print(result)
print("---------------------------------------------------------------------------------------------------------------------------------------------")




#10.Create a tuple of 10 numbers and display:
#•  First five elements 
#•  Last five elements 
#•  Middle four elements 
#•  Alternate elements 
#•  Reverse tuple
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print("First five:", numbers[:5])
print("Last five:", numbers[5:])
print("Middle four:", numbers[3:7])
print("Alternate elements:", numbers[::2])
print("Reverse tuple:", numbers[::-1])
print("---------------------------------------------------------------------------------------------------------------------------------------------")




#11.Convert a tuple into a list and add a new element.
t = (10, 20, 30, 40)

lst = list(t)
lst.append(50)

print("List:", lst)
print("---------------------------------------------------------------------------------------------------------------------------------------------")




#12.Accept five numbers from the user, store them in a list, and convert the list into a tuple.
numbers = []

for i in range(5):
    n = int(input("Enter number: "))
    numbers.append(n)

t = tuple(numbers)

print("Tuple:", t)
print("---------------------------------------------------------------------------------------------------------------------------------------------")




#13.Modify a tuple by converting it into a list and then back into a tuple.
t = (10, 20, 30, 40)

lst = list(t)
lst[1] = 100

t = tuple(lst)

print("Modified tuple:", t)
print("---------------------------------------------------------------------------------------------------------------------------------------------")





#14.Create a tuple and delete it completely.
t = (10, 20, 30, 40)

print("Before deleting:", t)

del t

print("Tuple deleted successfully")
print("---------------------------------------------------------------------------------------------------------------------------------------------")





#15.Create a nested tuple containing student details and display each record.
students = (
    (101, "Rahul", 85),
    (102, "Amit", 90),
    (103, "Sneha", 88)
)

for student in students:
    print("Roll No:", student[0])
    print("Name:", student[1])
    print("Marks:", student[2])
    print()
print("---------------------------------------------------------------------------------------------------------------------------------------------")




#16.Store ten numbers in a tuple and calculate their sum.
numbers = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)

total = 0

for n in numbers:
    total += n

print("Sum:", total)
print("---------------------------------------------------------------------------------------------------------------------------------------------")




#17.Find the largest and smallest number in a tuple without using max() and min().
numbers = (25, 10, 45, 5, 30)

largest = numbers[0]
smallest = numbers[0]

for n in numbers:
    if n > largest:
        largest = n

    if n < smallest:
        smallest = n

print("Largest:", largest)
print("Smallest:", smallest)
print("---------------------------------------------------------------------------------------------------------------------------------------------")




#18.Calculate the average of elements stored in a tuple.
numbers = (10, 20, 30, 40, 50)

total = 0

for n in numbers:
    total += n

average = total / len(numbers)

print("Average:", average)
print("---------------------------------------------------------------------------------------------------------------------------------------------")




#19.Store 15 integers in a tuple and count:
#•  Even numbers 
#•  Odd numbers
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)

even = 0
odd = 0

for n in numbers:
    if n % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even numbers:", even)
print("Odd numbers:", odd)
print("---------------------------------------------------------------------------------------------------------------------------------------------")



#20.Accept a number from the user and determine whether it exists in the tuple.
numbers = (10, 20, 30, 40, 50)

n = int(input("Enter number: "))

if n in numbers:
    print("Number exists")
else:
    print("Number does not exist")
print("---------------------------------------------------------------------------------------------------------------------------------------------")



#21.Store student details in a tuple:
#•  Roll Number 
#•  Name 
#•  Department 
#•  Marks 
#Display all the details.
student = (101, "Rahul", "Computer Science", 85)

print("Roll Number:", student[0])
print("Name:", student[1])
print("Department:", student[2])
print("Marks:", student[3])
print("---------------------------------------------------------------------------------------------------------------------------------------------")



#22.Create tuples containing:
#•  Employee ID 
#•  Name 
#•  Salary 
#Display all employee information.
employees = (
    (101, "Rahul", 30000),
    (102, "Amit", 35000),
    (103, "Sneha", 40000)
)

for emp in employees:
    print("Employee ID:", emp[0])
    print("Name:", emp[1])
    print("Salary:", emp[2])
    print()
print("---------------------------------------------------------------------------------------------------------------------------------------------")




#23.Store item prices in a tuple and calculate:
#•  Total bill 
#•  Average price 
#•  Highest-priced item 
#•  Lowest-priced item
prices = (100, 250, 150, 500, 300)

total = sum(prices)
average = total / len(prices)
highest = max(prices)
lowest = min(prices)

print("Total bill:", total)
print("Average price:", average)
print("Highest price:", highest)
print("Lowest price:", lowest)
print("---------------------------------------------------------------------------------------------------------------------------------------------")




#24.Store temperatures of seven days in a tuple and determine:
#•  Maximum temperature 
#•  Minimum temperature 
#•  Average temperature 
temperatures = (32, 35, 31, 34, 36, 33, 30)

total = sum(temperatures)
average = total / len(temperatures)

print("Maximum temperature:", max(temperatures))
print("Minimum temperature:", min(temperatures))
print("Average temperature:", average)
print("---------------------------------------------------------------------------------------------------------------------------------------------")



#25.Store runs scored in 10 matches and calculate:
#•  Total runs 
#•  Highest score 
#•  Lowest score 
#•  Average score
runs = (45, 78, 32, 90, 55, 67, 100, 40, 85, 60)

total = sum(runs)
average = total / len(runs)

print("Total runs:", total)
print("Highest score:", max(runs))
print("Lowest score:", min(runs))
print("Average score:", average)
print("---------------------------------------------------------------------------------------------------------------------------------------------")




#26.Create two tuples and find the common elements between them.
t1 = (10, 20, 30, 40, 50)
t2 = (30, 40, 50, 60, 70)

common = ()

for n in t1:
    if n in t2:
        common += (n,)

print("Common elements:", common)
print("---------------------------------------------------------------------------------------------------------------------------------------------")



#27.Merge two tuples and remove duplicate elements.
t1 = (10, 20, 30, 40)
t2 = (30, 40, 50, 60)

merged = t1 + t2

result = tuple(set(merged))

print("Merged tuple without duplicates:", result)
print("---------------------------------------------------------------------------------------------------------------------------------------------")




#28.Count the frequency of each element in a tuple.
numbers = (10, 20, 10, 30, 20, 10, 40, 30)

for n in set(numbers):
    print(n, ":", numbers.count(n))
print("---------------------------------------------------------------------------------------------------------------------------------------------")




#29.Convert a tuple into a sorted tuple in ascending and descending order.
numbers = (50, 20, 40, 10, 30)

ascending = tuple(sorted(numbers))
descending = tuple(sorted(numbers, reverse=True))

print("Ascending:", ascending)
print("Descending:", descending)
print("---------------------------------------------------------------------------------------------------------------------------------------------")




#30.Create a tuple containing patient records:
#•  Patient ID 
#•  Name 
#•  Age 
#•  Blood Group 
#Perform the following operations:
#•  Display all records 
#•  Search for a patient by ID 
#•  Count the total number of patients 
#•  Display patients with a specific blood group
patients = (
    (101, "Rahul", 25, "A+"),
    (102, "Amit", 30, "B+"),
    (103, "Sneha", 22, "O+"),
    (104, "Priya", 28, "A+")
)

print("All Patient Records:")
for patient in patients:
    print(patient)

pid = int(input("\nEnter Patient ID to search: "))

found = False

for patient in patients:
    if patient[0] == pid:
        print("Patient Found:", patient)
        found = True

if not found:
    print("Patient not found")

print("\nTotal patients:", len(patients))

blood = input("\nEnter blood group: ")

print("Patients with blood group", blood, ":")

for patient in patients:
    if patient[3] == blood:
        print(patient)


























