import math

class Calculator:
    def __init__(self):
        self.num1 = None
        self.num2 = None
        self.operator = None

    def get_user_input(self):
        while True:
            try:
                self.num1 = float(input("Введіть перше число: "))
                self.operator = input("Введіть оператор (+, -, *, /, ^, sqrt, %): ")
                if self.operator != 'sqrt':
                    if self.operator not in ['+', '-', '*', '/', '^', 'sqrt', '%']:
                        print("Помилка: недійсний оператор.")
                        continue  # Ask for operator again if it's invalid
                    self.num2 = float(input("Введіть друге число: "))
                break  # Exit the loop when valid input is provided
            except ValueError:
                print("Помилка: введіть дійсне число.")
            except KeyboardInterrupt:
                print("\nДо побачення!")
                exit(0)

    def calculate_result(self):
        raise NotImplementedError("Метод calculate_result повинен бути реалізований у підкласі.")

    def repeat_calculation(self):
        while True:
            print("Підтримувані операції: +, -, *, /, ^ (піднесення до степеня), sqrt (квадратний корінь), % (залишок від ділення)")
            self.get_user_input()
            result = self.calculate_result()
            if result is not None:
                print(f"Результат: {result:.2f}")

            another_calculation = input("Виконати ще одне обчислення? (y/n): ")
            if another_calculation.lower() != 'y':
                break
