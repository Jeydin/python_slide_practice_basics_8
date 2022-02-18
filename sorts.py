# Create a Selection Sort
def selection_sort(a_list):
	i = 0
	while i < len(a_list) - 1:
		j = i + 1 
		smallest = i
		while j < len(a_list):
			if (a_list[j] < a_list[smallest]):
				smallest = j
			j += 1
			# Swap
			# temp = a_list[i]
			# a_list[i] = a_list[smallest]
			# a_list[smallest] = temp
			a_list[i], a_list[smallest] = a_list[smallest], a_list[i]
		print(a_list)
		i += 1
