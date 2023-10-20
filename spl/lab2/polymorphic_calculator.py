from calculator import Calculator  # Імпортуємо базовий клас
import math

class PolymorphicCalculator(Calculator):
    def calculate_result(self):
        if self.operator == '+':
            return self.num1 + self.num2
        elif self.operator == '-':
            return self.num1 - self.num2
        elif self.operator == '*':
            return self.num1 * self.num2
        elif self.operator == '/':
            try:
                if self.num2 == 0:
                    raise ZeroDivisionError
                return self.num1 / self.num2
            except ZeroDivisionError:
                print("Помилка: ділення на 0.")
                return None
        elif self.operator == '^':
            return self.num1 ** self.num2
        elif self.operator == 'sqrt':
            if self.num1 < 0:
                print("Помилка: неможливо взяти корінь з від'ємного числа.")
                return None
            return math.sqrt(self.num1)
        elif self.operator == '%':
            return self.num1 % self.num2

# Тестування:
if __name__ == "__main__":
    calc = PolymorphicCalculator()
    calc.repeat_calculation()
