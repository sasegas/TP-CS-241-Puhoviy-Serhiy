from functions import plus, minus, divide, multiply

def get_number():
	try:
		a = float(input("Введіть перше число: "))
		b = float(input("Введіть друге число: "))
		return a, b
	except ValueError:
		print("Помилка: введіть числове значення!")
		return None, None
	
def perform_operation():
   while True:
      a, b = get_number()
      if a is None or b is None:
         continue
      sign = input("Введіть дію (+ - * /) або 'exit' для виходу: ")

      if sign == "exit":
         print("Вихід з програми.")
         break
      
      match sign:
         case "+":
            print(f"Результат: {plus(a, b)}")
         case "-":
            print(f"Результат: {minus(a, b)}")
         case "*":
            print(f"Результат: {multiply(a, b)}")
         case "/":
            print(f"Результат: {divide(a, b)}")
         case _:
            print("Була задана некоректна дія.")

