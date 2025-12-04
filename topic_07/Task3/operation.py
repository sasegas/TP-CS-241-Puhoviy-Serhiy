from function import MathOperations

class Operator: 
    def __init__(self):
        self.engine = MathOperations()

    def perform_calculation(self, a, b, sign):
        match sign:
            case "+":
                return self.engine.plus(a, b)
            case "-":
                return self.engine.minus(a, b)
            case "*":
                return self.engine.multiply(a, b)
            case "/":
                return self.engine.divide(a, b)
            case _:
                error_msg = "Була задана некоректна дія."
                print(error_msg)
               
  