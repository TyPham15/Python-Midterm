def write_file():
	coffee_brand = str(input('Enter the name of your favorite coffee brand: '))

	write = open('Coffee.txt','a')
	write.write (f'\n{coffee_brand},99-8888,9.88')

	write.close()

	read_file()

def read_file():
	file = open('Coffee.txt','r')
	contents = file.read()

	file.close()

	print(contents)

write_file()