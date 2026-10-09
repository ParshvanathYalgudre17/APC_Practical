roll = input("Enter roll number to search: ")

found = False

with open("students.txt", "r") as file:
    for line in file:
        data = line.split()

        if data[0] == roll:
            print("\nStudent Record Found!")
            print("Roll No:", data[0])
            print("Name:", data[1])
            print("Marks:", data[2])
            found = True
            break

if not found:
    print("Student record not found!")
