# Function that read in a file and save to a list

def file_to_int_list(file_name):
	num_list = []
	in_file = open(file_name, "r")
	for line in in_file:
		val = int(line)
		num_list.append(val)
	in_file.close()
	return num_list

print(file_to_int_list("data.txt"))