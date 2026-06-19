import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("students.csv")

print(data)

plt.bar(data["Name"], data["Marks"])
plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.show()