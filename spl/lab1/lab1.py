import math
import re

def calculate(num1, num2, operator, decimal_places):
    result = None
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            print("Ділення на 0 неможливе.")
            return None
        else:
            result = num1 / num2
    elif operator == '^':
        result = num1 ** num2
    elif operator == 'sqrt':
        if num1 < 0:
            print("Неможливо взяти корінь з від'ємного числа.")
            return None
        else:
            result = math.sqrt(num1)
    elif operator == '%':
        result = num1 % num2
    else:
        print("Невідомий знак оператор")
        return None

    return round(result, decimal_places) if result is not None else result

#CREATED Get_input function for code optimization and easy reading
def get_input():
    try:
        num1 = float(input("Введіть перше число: "))
    except ValueError:
        print("Помилка: недійсне число.")
        return None, None, None

    valid_operators = ['+', '-', '*', '/', '^', 'sqrt', '%']
    operator = input(f"Введіть знак оператор ({', '.join(valid_operators)}): ")

    while operator not in valid_operators:
        print("Помилка: недійсний знак оператор.")
        operator = input(f"Введіть дійсний знак оператор ({', '.join(valid_operators)}): ")

    num2 = 0
    if operator != 'sqrt':
        try:
            num2 = float(input("Введіть друге число: "))
        except ValueError:
            print("Помилка: недійсне число.")
            return None, None, None

    return num1, operator, num2

memory = None
history = []
decimal_places = 2  # Кількість десяткових розрядів за замовчуванням

while True:
    # Налаштування користувача
    settings = input("Зайти у налаштування? (y/n): ")
    if settings.lower() == 'y':
        decimal_places = int(input("Введіть кількість десяткових розрядів для відображеня: "))

    num1, operator, num2 = get_input()
    
    if num1 is not None:
        result = calculate(num1, num2, operator, decimal_places)
        if result is not None:
            history.append(f"{num1} {operator} {num2 if operator != 'sqrt' else ''} = {result}")
            print(f"Результат: {result}")

            mem_option = input("Зберегти результат у пам'яті? (y/n): ")
            if mem_option.lower() == 'y':
                memory = result

        if memory is not None:
            use_mem = input(f"Використати збережене значення {memory} як перше число? (y/n): ")
            if use_mem.lower() == 'y':
                num1 = memory

        view_history = input("Переглянути історію операцій обчислень? (y/n): ")
        if view_history.lower() == 'y':
            for i, entry in enumerate(history):
                print(f"{i + 1}. {entry}")

        repeat = input("Виконати ще одне обчислення? (y/n): ")
        if repeat.lower() != 'y':
            break