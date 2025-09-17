import math

def quadraticFn():
	a = int(input('Введіть перший коефіцієнт:'))
	b = int(input('Введіть другий коефіцієнт:'))
	c = int(input('Введіть вільний член:'))
	discriminator = b**2 - 4*a*c
	if discriminator == 0:
		print ("Рівняння має один корінь")
		x = -b/(2*a)
		print(x)
	elif discriminator > 0:
		print ("Рівняння має два корінь")
		x1 = (-b - math.sqrt(discriminator))/(2*a)
		x2 = (-b + math.sqrt(discriminator))/(2*a)
		print('x1=',x1)
		print('x2=',x2)
	else:
		print("Рівняння не має дійсних коренів")



quadraticFn()