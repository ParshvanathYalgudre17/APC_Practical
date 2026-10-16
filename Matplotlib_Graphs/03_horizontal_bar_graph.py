import matplotlib.pyplot as plt

subjects = ["Python", "Java", "AI", "DBMS"]
marks = [85, 75, 90, 80]

plt.barh(subjects, marks)
plt.title("Horizontal Bar Graph")
plt.xlabel("Marks")
plt.ylabel("Subjects")
plt.show()
