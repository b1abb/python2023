import random
import math

# + сложение двух чисел
# - вычитание второго и последующих чисел из первого
# * умножение двух чисел
# / деление первого числа на последующие
# ** возведение первого числа в степень, заданную вторым числом
# abs нахождение абсолютного значения числа
# rand генерация случайного числа в заданном диапазоне
# ! нахождение факториала числа
# arccos нахождение арккосинуса числа


def add(numbers):
    return sum(numbers)


def subtract(numbers):
    return numbers[0] - sum(numbers[1:])


def multiply(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result


def divide(numbers):
    result = numbers[0]
    for number in numbers[1:]:
        result /= number
    return result


def power(numbers):
    return numbers[0] ** numbers[1]


def absolute(numbers):
    return abs(numbers[0])


def random_number(numbers):
    return random.randint(numbers[0], numbers[1])


def factorial(numbers):
    return math.factorial(numbers[0])


def arccos(numbers):
    return math.acos(numbers[0])


def calculator():
    operation = input("Введите операцию (+, -, /, *, **, abs, rand, !, arccos): ")
    if operation in ['+', '-', '/', '*', '**']:
        numbers = [float(input(f"Введите число {i + 1}: ")) for i in range(2)]
        if operation == '+':
            result = add(numbers)
        elif operation == '-':
            result = subtract(numbers)
        elif operation == '*':
            result = multiply(numbers)
        elif operation == '/':
            result = divide(numbers)
        elif operation == '**':
            result = power(numbers)
    elif operation in ['abs', 'rand', '!']:
        number = float(input("Введите число: "))
        if operation == 'abs':
            result = absolute([number])
        elif operation == 'rand':
            numbers = [int(input(f"Введите минимальное число: ")), int(input(f"Введите максимальное число: "))]
            result = random_number(numbers)
        elif operation == '!':
            result = factorial([int(number)])
    elif operation == 'arccos':
        number = float(input("Введите число: "))
        result = arccos([number])
    else:
        print("Некорректная операция")
        return
    print(f"Результат: {result}")


if __name__ == '__main__':
    calculator()
