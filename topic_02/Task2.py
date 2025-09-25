a = float(input("введіть перше число: "))
b = float(input("введіть перше друге число: "))
sign = input("введіть дію(+ - * /): ")

def calculator (a, b, sign):
	if sign == "+":
		return  a + b 
	elif sign == "-":
		return a - b
	elif sign == "*":
		return  a * b 
	elif sign == "/": 
		if b != 0:
			return  a / b 
		else: 
			return "Ділити на 0 неможна"
	else: 
		return "Була задана некоректна дія"

result = calculator(a,b,sign)
print("Відповідь: ", result)