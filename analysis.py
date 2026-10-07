import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("student_data.csv")

print("Original Data:")
print(df)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Clean missing values
df["Science"] = df["Science"].fillna(df["Science"].mean())
df["English"] = df["English"].fillna(df["English"].mean())

print("\nCleaned Data:")
print(df)

# Create Average Marks
df["Average"] = (
    df["Maths"] +
    df["Science"] +
    df["English"]
) / 3

print("\nStudent Average:")
print(df[["Name", "Average"]])

# Visualization 1 - Average Marks
plt.figure(figsize=(8,5))
plt.bar(df["Name"], df["Average"])
plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.title("Student Average Marks")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("average_marks.png")
plt.show()

# Visualization 2 - Attendance
plt.figure(figsize=(8,5))
plt.bar(df["Name"], df["Attendance"])
plt.xlabel("Students")
plt.ylabel("Attendance (%)")
plt.title("Student Attendance")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("attendance.png")
plt.show()

# Highest performing student
top_student = df.loc[df["Average"].idxmax()]

print("\nTop Performing Student:")
print(top_student["Name"])
print("Average:", round(top_student["Average"], 2))

# Save cleaned dataset
df.to_csv("cleaned_student_data.csv", index=False)

print("\nProject completed successfully!")