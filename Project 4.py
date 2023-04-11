def ask_user():
	rent = float(input('Enter the rent for last month: '))
	gas = float(input('Enter the gas payments for last month: '))
	food = float(input('Enter the food payments for last month: '))
	clothing = float(input('Enter the clothing payments for last month: '))
	car = float(input('Enter the car payments for last month: '))

	write_file(rent,gas,food,clothing,car)

def write_file(rent,gas,food,clothing,car):
	file = open('monthly payments.txt','w')

	file.write (f'Rent = ${rent}\n')
	file.write (f'Gas = ${gas}\n')
	file.write (f'Food = ${food}\n')
	file.write (f'Clothing = ${clothing}\n')
	file.write (f'Car Payments = ${car}\n')

	file.close()

	read_file()

def read_file():
	file = open('monthly payments.txt','r')
	contents = file.read()
	file.close()

	print(contents)

ask_user()