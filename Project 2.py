def read_file():
	file = open('Coffee.txt','r')
	contents = file.read()
	file.close()
	print(contents)

read_file()
