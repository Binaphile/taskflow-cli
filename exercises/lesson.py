student = {
    "Name": "Harvey",
    "Age": 22,
    "Course": "Computer Science",
    "University" : "Tarlac State University"
}

student["Age"] = 23

print(student["Name"])
print(student["Age"])
print(student["Course"])
print(student["University"])

print()

print(student.keys())

print(student.values())

print()

print(type(student.keys()))
print(type(student.values()))

print(f"{student['Name']} studies {student['Course']} at {student['University']}")