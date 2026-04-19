numbers = (10, 20, 30, 40, 50)
print("Tuple:", numbers)

print("First element:", numbers[0])
print("Last element:", numbers[-1])

# 
print("Slice (1 to 3):", numbers[1:4])

for item in numbers:
    print("Item:", item)


student = (
    "Rahul",
    20,
    ("B.Tech", "Computer Science"),
    ("Maths", "Physics", "Programming")
)

print("Student Name:", student[0])
print("Degree:", student[2][0])
print("Department:", student[2][1])
print("First Subject:", student[3][0])

student_scores = {
    ("Rahul", "Maths"): 90,
    ("Rahul", "Physics"): 85
}

print("Tuple as dictionary key:", student_scores)


print("Hash of tuple:", hash(numbers))



tuple_a = (1, 2, 3)
tuple_b = (4, 5)

combined_tuple = tuple_a + tuple_b
print("Concatenated Tuple:", combined_tuple)


repeated_tuple = tuple_a * 3
print("Repeated Tuple:", repeated_tuple)
