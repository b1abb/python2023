def compare_numbers():
    number = int(input("Введите произвольное число: "))
    boundary = int(input("Введите пограничное число: "))

    if number < boundary:
        print("Первое число меньше пограничного")
    elif number > boundary:
        print("Первое число больше пограничного")
        if number > boundary * 3:
            print("Первое число больше пограничного более, чем в 3 раза")
    else:
        print("Первое число равно пограничному числу")


if __name__ == '__main__':
    compare_numbers()
