# Writing
file = open("sample.txt", "w")
file.write("Hello World\n")
file.close()

# Reading
file = open("sample.txt", "r")
print(file.read())
file.close()

# Appending
file = open("sample.txt", "a")
file.write("This is appended text\n")
file.close()
