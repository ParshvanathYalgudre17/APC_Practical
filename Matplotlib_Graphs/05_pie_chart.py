import matplotlib.pyplot as plt

subjects = ["Python", "Java", "AI", "DBMS"]
marks = [85, 75, 90, 80]

plt.pie(marks, labels=subjects, autopct="%1.1f%%")
plt.title("Marks Distribution")
plt.show()
