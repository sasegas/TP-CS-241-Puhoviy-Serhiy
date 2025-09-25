def plus(a,b):
	return a+b
def minus(a,b):
	return a-b
def multiply(a,b):
	return a*b
def divide(a,b):
	if b!= 0:
		return a/b
	else:
		return "Ділити на 0 неможна"
	
a = float(input("введіть перше число: "))
b = float(input("введіть перше друге число: "))
sign = input("введіть дію(+ - * /): ")



match(sign):
	case "+":
		result = plus(a,b)
		
	case "-":
		result = minus(a,b)
		
	case "*":
		result = multiply(a,b)
	
	case "/":
		result = divide(a,b)
	case _:
		result = "Була задана некоректна дія"

print("Відповідь: ", result)
