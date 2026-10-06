import csv
import json

# Assignment 9: Student Records Processing

# Step 1: Store student details in a CSV file
students = [
    {"Roll": 101, "Name": "Amit", "Branch": "CSE", "Marks": [85, 90, 78]},
    {"Roll": 102, "Name": "Sneha", "Branch": "IT", "Marks": [88, 76, 92]},
    {"Roll": 103, "Name": "Rahul", "Branch": "ECE", "Marks": [70, 65, 80]},
]

# Write to CSV
with open("students.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    # Header
    writer.writerow(["Roll", "Name", "Branch", "Marks"])
    # Rows
    for s in students:
        writer.writerow(
            [
                s["Roll"],
                s["Name"],
                s["Branch"],
                ",".join(map(str, s["Marks"])),
            ]
        )

print("Student details written to students.csv")

# Step 2: Read CSV and process records
processed_records = []
with open("students.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        marks = list(map(int, row["Marks"].split(",")))
        total = sum(marks)
        # Assuming each subject is out of 100
        percentage = total / (len(marks) * 100) * 100

        # Grade logic
        if percentage >= 80:
            grade = "A"
        elif percentage >= 60:
            grade = "B"
        elif percentage >= 40:
            grade = "C"
        else:
            grade = "F"

        processed_records.append({
            "Roll": int(row["Roll"]),
            "Name": row["Name"],
            "Branch": row["Branch"],
            "Total Marks": total,
            "Percentage": round(percentage, 2),
            "Grade": grade
        })

# Step 3: Store processed records in JSON
with open("students.json", "w") as jsonfile:
    json.dump(processed_records, jsonfile, indent=4)

print("Processed student records written to students.json")
