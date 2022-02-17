# Data Notes - Using files in Python
print("====== Example 1 ======")
# .readling() reads one line from file
in_file = open("typing_practice1.txt", "r")
line = in_file.readline()
print(line)
in_file.close()
print()

print("====== Example 2 ======")
# Iterate through the file line by line with a for loopo
in_file = open("typing_practice2.txt", "r")
for line in in_file:
	print(line)
in_file.close()
print()

print("====== Example 3 ======")
# Take out the extra lines
in_file = open("typing_practice2.txt", "r")
for line in in_file:
	print(line, end="")
in_file.close()
print()

print("====== Example 4 ======")
# Save the words to a list
in_file = open("typing_practice1.txt", "r")
line = in_file.readline()
line_list = line.split(" ")
in_file.close()
print(line_list)
print()

print("====== Example 5 ======")
# Using a loop to save words to a list (by line)
in_file = open("typing_practice2.txt", "r")
word_list = []
for line in in_file:
	word_list.append(line)
print(word_list)
in_file.close()
print()

print("====== Example 6 ======")
# .strip()
in_file = open("typing_practice2.txt", "r")
word_list = []
for line in in_file:
	line = line.strip()
	word_list.append(line)
in_file.close()
print(word_list)
print()
