from operation import Operator

def main():
    app = Operator()
    
    try:
        num1 = float(input("Введіть перше число: "))
        num2 = float(input("Введіть друге число: "))
        sign = input("Введіть дію (+ - * /): ")

        result = app.perform_calculation(num1, num2, sign)

        print(f"Відповідь: {result}")

    except ValueError as e:
        print(f"Виникла помилка: {e}")

if __name__ == "__main__":
    main()