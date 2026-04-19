student = {
    "name": "Rahul",
    "age": 20,
    "course": "B.Tech"
}


student2 = dict(name="Amit", age=21, course="B.Sc")


empty_dict = {}

mixed_dict = {
    1: "One",
    "two": 2,
    (3, 4): "Tuple as key"
}


print("Name:", student["name"])


print("Age:", student.get("age"))
print("Marks (default):", student.get("marks", 0))


print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())



print("Student Details:")
for key, value in student.items():
    print(key, ":", value)
