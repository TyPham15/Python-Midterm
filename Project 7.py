def main():
	numbers = [[1,2,3],
			[4,5,6],
			[7,8,9,10]]

	print(numbers)

	search = 0

	for n in range(len(numbers)):
		for x in range(len(numbers[n])):
			search = numbers[n][x]
			if search == 7:
				print(f'\nThe lucky number has been found: 7')

main()