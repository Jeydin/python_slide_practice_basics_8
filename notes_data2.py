print("====== Output to a File ======")
import random
file_name = "random_num.dat"
out_file = open(file_name, "w")
count = 0
while count < 10:
	value = random.randint(1, 101)
	print(value, file = out_file)
	print(value)
	count += 1
out_file.close()
print()

print("====== Move .dat file to list ======")
in_file = open(file_name, "r")
count = 0
sum = 0
val_list = []
for line in in_file:
	val = int(line)
	val_list.append(val)
	sum += val
	count += 1
avg = sum / count
in_file.close()
print("Sum:", sum)
print("Count:", count)
print("Average:", avg)
print(val_list)

print("====== Selection Sort Applied ======")
from sorts import *
selection_sort(val_list)
print(val_list)