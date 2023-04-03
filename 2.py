def manipulate_string():
    user_string = input("Введите произвольную строку: ")
    string_length = len(user_string)

    print(f"Длина строки: {string_length}")

    for index, char in enumerate(user_string):
        if index == 2:
            continue
        elif char == 'c':
            print("Строка содержит символ 'c'")
        else:
            print(char, end='')

    print()


if __name__ == '__main__':
    manipulate_string()

