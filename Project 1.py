def ask():
	fat = float(input('Enter how much fat grams was consumed in one day: '))
	carb = float(input('Enter how much carbohydrate grams was consumed in one day: '))

	calculate(fat,carb)

def calculate(fat,carb):
	caloriesFat = fat * 9

	caloriesCarb = carb * 4

	print(f'The calories from {fat} grams of fat is {caloriesFat}.')

	print(f'The calories from {carb} grams of carbohydrates is {caloriesCarb}.')

ask()