# Learned

# Creating dictionaries
# Reading values
# Updating values
# Adding new keys
# .keys()
# .values()
# .items()
# Checking if a key exists (in)
# .get()
# .update()
# .pop()

book = {
    "Title": "Atomic Habits",
    "Author": "James Clear",
    "Pages": 320
}

book.pop("Pages")

removedValue = 320

print(removedValue)

print(book)


book = {
    "Title" : "Atomic Habits",
    "Author" : "James Clear",
    "Pages" : 320
}

if "Author" in book:
    print("It exist")

print(book.get("Publisher", "Unknown"))


book = {
    "Title": "Atomic Habits",
    "Author": "James Clear"
}

book.update({
    "Author" : "John Doe",
    "Pages" : 320
})

print(book)

movie = {
    "Name": "Interstellar",
    "Year": 2014,
    "Genre": "Sci-Fi",
    "Rating": "8.7"
}

print("Movie Information")

print()

for key, item in movie.items():
    print(f"{key} : {item}")



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