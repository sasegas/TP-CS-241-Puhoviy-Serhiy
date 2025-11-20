LOG_FILE = "calculator_log.txt"

def log_custom(sign, a, b, result=None, error=None):
    
    if error:
        log_level = "ERROR"
        status_info = f"Помилка: {error}"
    else:
        log_level = "INFO"
        status_info = f"Результат: {result}"

    log_entry = f"{log_level} - Операція: {a} {sign} {b} , {status_info}\n"
    
   
    with open(LOG_FILE, "a", encoding="utf-8") as file:
       file.write(log_entry)
            

def plus(a, b):
    result = a + b
    log_custom("+", a, b, result)
    return result

def minus(a, b):
    result = a - b
    log_custom("-", a, b, result)
    return result

def multiply(a, b):
    result = a * b
    log_custom("*", a, b, result)
    return result

def divide(a, b):
    try:
        result = a / b
        log_custom("/", a, b, result)
        return result
    except ZeroDivisionError:
        error_msg = "Не можна ділити на нуль"
        log_custom("/", a, b, error=error_msg)
        return error_msg