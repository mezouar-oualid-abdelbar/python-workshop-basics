

def filter_even_numbers(numbers):
	even_numbers=[]
	for num in numbers:
		if num % 2 == 0:
			even_numbers.append(num)
	return even_numbers

test = [1, 2, 3, 4, 5, 6, 7, 8]

resault = filter_even_numbers(test)

print(resault)
