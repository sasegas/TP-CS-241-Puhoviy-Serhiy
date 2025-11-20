from functions import plus, minus, divide, multiply, log_custom

def get_number():
    try:
        a = float(input("Введіть перше число: "))
        b = float(input("Введіть друге число: "))
        return a, b
    except ValueError:
        error_msg = "Помилка: введіть числове значення!"
        print(error_msg)
        log_custom("err","N/A", "N/A", error="Введено не числове значення")
        return None, None
    
def perform_operation():
    log_custom("?", "N/A", "N/A", result="Початок роботи")
    
    while True:
        a, b = get_number()
        if a is None or b is None:
            continue
            
        sign = input("Введіть дію (+ - * /) або 'exit' для виходу: ")

        if sign == "exit":
            print("Вихід з програми.")

            log_custom("?", "N/A", "N/A", result="Завершення роботи")
            break
        
        result = None
        match sign:
            case "+":
                result = plus(a, b)
            case "-":
                result = minus(a, b)
            case "*":
                result = multiply(a, b)
            case "/":
                result = divide(a, b)
            case _:
                error_msg = "Була задана некоректна дія."
                print(error_msg)
                log_custom("err", a, b, error=f"Невідома дія - {sign}")
                continue
        
        print(f"Результат: {result}")