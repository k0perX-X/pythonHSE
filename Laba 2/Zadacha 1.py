import random
from koinput import int_input


def main():
    score = 0
    number = random.randint(1, 10)
    plays = 0
    print("Программа загадывает число от 1 до 10. Пробуйте отгадать его. Для выхода введите 0.")
    x = int_input()
    while x != 0:
        attempt = 1
        while x != number and x != 0:
            print('Вы не угадали попробуйте снова.')
            if attempt > 2:
                if x > number:
                    print("Ну хорошо, вот подсказка: загаданное число меньше.")
                else:
                    print("Ну хорошо, вот подсказка: загаданное число больше.")
            attempt += 1
            x = int_input()
        if x == 0:
            break
        print(f'Поздравляем вы правы, загаданное число {x}!\nЕсли хотите выйти введите 0.')
        number = random.randint(1, 10)
        score += attempt
        plays += 1
        x = int_input()
    if plays != 0:
        print(f"Вы угадывали число с {round(score / plays * 100) / 100} попытки в среднем.")


if __name__ == '__main__':
    main()
