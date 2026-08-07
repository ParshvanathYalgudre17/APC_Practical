#Write a Python program to create a list of five fruits and display the list.

list=["Apple","Banana","pineapple","Orange","Mango"]
print("List odf Five Fruits:",list)

print("---------------------------------------------------------------------------------------------------------------------------------------------------")
#Create a list of five integers. Display: First element  Last element  Third element"""

numbers = [10, 20, 30, 40, 50]
print("First Element:", numbers[0])
print("Last Element:", numbers[-1])
print("Third Element:", numbers[2])


print("---------------------------------------------------------------------------------------------------------------------------------------------------")

#Create a list of colors Replace the third color with another color and display the updated list.

color=["red","Pink","Yellow","Blue","Black"]
print("Befor replace list:", color)
color[2]="White"
print("After replacing the color: ", color)

print("---------------------------------------------------------------------------------------------------------------------------------------------------")

#Create a list of numbers. Add: One element at the end , One element at the beginning  ,One element at a specified position  Display the updated list.

numbers = [10, 20, 30]

numbers.append(40)
numbers.insert(0, 5)
numbers.insert(2, 15)
print(numbers)

print("---------------------------------------------------------------------------------------------------------------------------------------------------")

#Create a list of student names. Remove: First student  Last student  A specific student by name  Display the remaining list.

students = ["Amit", "Rahul", "Priya", "Neha", "Riya"]

students.pop(0)
students.pop()

name = input("Enter student name to remove: ")

if name in students:
    students.remove(name)

print(students)

print("---------------------------------------------------------------------------------------------------------------------------------------------------")

# Write a program to find the largest and smallest number in a list without using max() or min().

numbers = [25, 40, 10, 55, 5]

largest = numbers[0]
smallest = numbers[0]

for i in numbers:
    if i > largest:
        largest = i
    if i < smallest:
        smallest = i

print("Largest =", largest)
print("Smallest =", smallest)


print("---------------------------------------------------------------------------------------------------------------------------------------------------")

#Accept 10 numbers from the user and store them in a list. Calculate:Sum  Average 

numbers = []

for i in range(10):
    n = int(input("Enter number: "))
    numbers.append(n)

total = sum(numbers)
average = total / len(numbers)

print("Sum =", total)
print("Average =", average)

print("---------------------------------------------------------------------------------------------------------------------------------------------------")

#Store 15 integers in a list. Count how many numbers are:Even  Odd

numbers = []

for i in range(15):
    numbers.append(int(input("Enter number: ")))

even = 0
odd = 0

for i in numbers:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even =", even)
print("Odd =", odd)

print("---------------------------------------------------------------------------------------------------------------------------------------------------")

#Create a list of cities. Ask the user to enter a city name and check whether it exists in the list.

cities = ["Pune", "Mumbai", "Delhi", "Chennai", "Goa"]

city = input("Enter city name: ")

if city in cities:
    print("City Found")
else:
    print("City Not Found")


print("---------------------------------------------------------------------------------------------------------------------------------------------------")

#Write a program to reverse a list without using the reverse() method.

numbers = [10,20,30,40,50]

rev = []

for i in range(len(numbers)-1,-1,-1):
    rev.append(numbers[i])

print(rev)


print("---------------------------------------------------------------------------------------------------------------------------------------------------")

#Create a list of 10 numbers and display:First 5 elements , Last 5 elements , Middle 4 elements , Alternate elements , Reverse list using slicing

numbers = [1,2,3,4,5,6,7,8,9,10]

print("First 5:", numbers[:5])
print("Last 5:", numbers[-5:])
print("Middle 4:", numbers[3:7])
print("Alternate:", numbers[::2])
print("Reverse:", numbers[::-1])

print("---------------------------------------------------------------------------------------------------------------------------------------------------")

#Display all elements present at even index positions.

numbers = [10,20,30,40,50,60,70]

for i in range(0,len(numbers),2):
    print(numbers[i])

print("---------------------------------------------------------------------------------------------------------------------------------------------------")

#Accept 10 numbers and sort them in:Ascending order , Descending order

numbers = []

for i in range(10):
    numbers.append(int(input("Enter number: ")))

numbers.sort()
print("Ascending:", numbers)

numbers.sort(reverse=True)
print("Descending:", numbers)

print("---------------------------------------------------------------------------------------------------------------------------------------------------")

#Create a list containing duplicate values and display only unique elements.

numbers = [10,20,10,30,20,40,50]

unique = []

for i in numbers:
    if i not in unique:
        unique.append(i)

print(unique)


print("---------------------------------------------------------------------------------------------------------------------------------------------------")

#Find the second largest element in a list.

numbers = [10,20,60,40,80,70]

largest = second = numbers[0]

for i in numbers:
    if i > largest:
        second = largest
        largest = i
    elif i > second and i != largest:
        second = i

print("Second Largest =", second)


print("---------------------------------------------------------------------------------------------------------------------------------------------------")

#Create a nested list storing:Student Name , Roll Number , Marks .Display all student details.

students = [
    ["Amit",101,85],
    ["Rahul",102,90],
    ["Priya",103,88]
]

for s in students:
    print("Name:",s[0],"Roll:",s[1],"Marks:",s[2])


print("---------------------------------------------------------------------------------------------------------------------------------------------------")

#Create two 3 × 3 matrices using nested lists and perform matrix addition

A = [[1,2,3],[4,5,6],[7,8,9]]
B = [[9,8,7],[6,5,4],[3,2,1]]

C=[]

for i in range(3):
    row=[]
    for j in range(3):
        row.append(A[i][j]+B[i][j])
    C.append(row)

print(C)


print("---------------------------------------------------------------------------------------------------------------------------------------------------")

#Create a shopping cart using a list.Perform:1.Add item ,2.Remove item ,3.Search item ,4.Display cart ,5.Count total items

cart=["Milk","Bread","Rice"]

cart.append("Sugar")
cart.remove("Bread")

item=input("Search item: ")

if item in cart:
    print("Found")
else:
    print("Not Found")

print(cart)
print("Total Items:",len(cart))


print("---------------------------------------------------------------------------------------------------------------------------------------------------")

#Store names of students present in class. Display:1.Total students , 2.Search a student's attendance , 3.Add a new student , 4.Remove an absent student 

students=["Amit","Rahul","Neha"]

print("Total:",len(students))

name=input("Search Student: ")

if name in students:
    print("Present")
else:
    print("Absent")

students.append(input("Add Student: "))

students.remove(input("Remove Student: "))

print(students)


print("---------------------------------------------------------------------------------------------------------------------------------------------------")

#Create a list of books. Implement:1.Add a new book , 2.Search a book , 3.Remove a book , 4.Display all books , 5.Count total books

books=["Python","Java","C","C++"]

books.append(input("Add Book: "))

book=input("Search Book: ")

if book in books:
    print("Found")
else:
    print("Not Found")

books.remove(input("Remove Book: "))

print(books)
print("Total Books:",len(books))


print("---------------------------------------------------------------------------------------------------------------------------------------------------")

#Accept two lists and merge them into a single list.

list1=[1,2,3]
list2=[4,5,6]

list3=list1+list2

print(list3)


print("---------------------------------------------------------------------------------------------------------------------------------------------------")

#Find common elements between two lists.

list1=[1,2,3,4]
list2=[3,4,5,6]

for i in list1:
    if i in list2:
        print(i)

print("---------------------------------------------------------------------------------------------------------------------------------------------------")


#Count the frequency of each element in a list.


numbers=[10,20,10,30,20,10]

for i in numbers:
    print(i,"=",numbers.count(i))


print("---------------------------------------------------------------------------------------------------------------------------------------------------")

#Rotate a list:1.Left by one position , 2.Right by one position

numbers=[1,2,3,4,5]

left=numbers[1:]+numbers[:1]
right=numbers[-1:]+numbers[:-1]

print("Left:",left)
print("Right:",right)



print("---------------------------------------------------------------------------------------------------------------------------------------------------")

#Remove all duplicate elements while preserving the original order.

numbers=[1,2,3,2,4,1,5]

result=[]

for i in numbers:
    if i not in result:
        result.append(i)

print(result)


print("---------------------------------------------------------------------------------------------------------------------------------------------------")

#Store marks of 20 students in a list and determine:1.Highest marks ,2.Lowest marks ,3.Average marks ,4.Number of students scoring above average ,5.Number of students scoring below average

marks=[]

for i in range(20):
    marks.append(int(input("Enter Marks: ")))

highest=max(marks)
lowest=min(marks)
average=sum(marks)/20

above=0
below=0

for i in marks:
    if i>average:
        above+=1
    elif i<average:
        below+=1

print(highest,lowest,average,above,below)


print("---------------------------------------------------------------------------------------------------------------------------------------------------")

#Store salaries of employees and determine:1.Highest salary ,2.Lowest salary ,3.Average salary ,4.Employees earning above ₹50,000 ,5.Employees earning below ₹30,000 


salary=[]

n=int(input("Number of Employees: "))

for i in range(n):
    salary.append(int(input("Salary: ")))

print("Highest:",max(salary))
print("Lowest:",min(salary))
print("Average:",sum(salary)/n)

above=0
below=0

for i in salary:
    if i>50000:
        above+=1
    if i<30000:
        below+=1

print("Above 50000:",above)
print("Below 30000:",below)



print("---------------------------------------------------------------------------------------------------------------------------------------------------")

#Store scores of a batsman in 10 matches and calculate:1.Highest score 2.Lowest score 3.Total runs 4.Average runs 5.Number of centuries (≥100) 6.Number of half-centuries (50–99

score=[]

for i in range(10):
    score.append(int(input("Score: ")))

print("Highest:",max(score))
print("Lowest:",min(score))
print("Total:",sum(score))
print("Average:",sum(score)/10)

century=0
half=0

for i in score:
    if i>=100:
        century+=1
    elif i>=50:
        half+=1

print("Centuries:",century)
print("Half Centuries:",half)


print("---------------------------------------------------------------------------------------------------------------------------------------------------")

#Store the temperature of 30 days and determine:1.Hottest day 2.Coldest day 3.Average temperature 4.Days above average temperature 5.Days below average temperature

temp=[]

for i in range(30):
    temp.append(float(input("Temperature: ")))

avg=sum(temp)/30

print("Hottest:",max(temp))
print("Coldest:",min(temp))
print("Average:",avg)

above=0
below=0

for i in temp:
    if i>avg:
        above+=1
    elif i<avg:
        below+=1

print("Above Average:",above)
print("Below Average:",below)


print("---------------------------------------------------------------------------------------------------------------------------------------------------")

#Store patient names and ages using lists.Perform:1.Add a patient 2.Delete a patient 3.Search a patient 4.Display all patients 5.Count total patients

names=["Amit","Rahul","Neha"]
ages=[25,40,32]

names.append(input("Patient Name: "))
ages.append(int(input("Age: ")))

delete=input("Delete Patient: ")

if delete in names:
    index=names.index(delete)
    names.pop(index)
    ages.pop(index)

search=input("Search Patient: ")

if search in names:
    i=names.index(search)
    print(names[i],ages[i])
else:
    print("Patient Not Found")

print("Patients:")

for i in range(len(names)):
    print(names[i],ages[i])

print("Total Patients:",len(names))















