def main():
	names = []

	count = 0

	while count < 5:
		count += 1
		new_name = str(input('Enter a name: '))
		names.append(new_name)

	for n in names:
		print(f'{n}')

main()