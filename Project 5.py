def main():
	list = (20,21,22,23,24,25,26,27,28,29,30)

	total = 0

	for n in list:
		total += n

	avg = total / len(list)

	print(f'Total: {total}')
	print(f'Average: {avg}')

main()