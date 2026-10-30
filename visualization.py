import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student-mat.csv", sep=";")

# 1. Final Grade Distribution
plt.figure(figsize=(8, 5))
plt.hist(df["G3"], bins=11)
plt.title("Distribution of Final Mathematics Grades")
plt.xlabel("Final Grade")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.savefig("grade_distribution.png")
plt.show()

# 2. Study Time vs Final Grade
plt.figure(figsize=(8, 5))
df.groupby("studytime")["G3"].mean().plot(kind="bar")
plt.title("Average Final Grade by Study Time")
plt.xlabel("Study Time Category")
plt.ylabel("Average Grade")
plt.tight_layout()
plt.savefig("studytime_vs_grade.png")
plt.show()

# 3. Previous Failures vs Final Grade
plt.figure(figsize=(8, 5))
df.groupby("failures")["G3"].mean().plot(kind="bar")
plt.title("Average Final Grade by Previous Failures")
plt.xlabel("Previous Failures")
plt.ylabel("Average Grade")
plt.tight_layout()
plt.savefig("failures_vs_grade.png")
plt.show()

# 4. Absences vs Final Grade
plt.figure(figsize=(8, 5))
plt.scatter(df["absences"], df["G3"], alpha=0.6)
plt.title("Absences vs Final Grade")
plt.xlabel("Absences")
plt.ylabel("Final Grade")
plt.tight_layout()
plt.savefig("absences_vs_grade.png")
plt.show()

# 5. Gender vs Final Grade
plt.figure(figsize=(8, 5))
df.groupby("sex")["G3"].mean().plot(kind="bar")
plt.title("Average Final Grade by Gender")
plt.xlabel("Gender")
plt.ylabel("Average Grade")
plt.tight_layout()
plt.savefig("gender_vs_grade.png")
plt.show()

print("Data Visualization completed successfully!")