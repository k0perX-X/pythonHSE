import random
import pip
import sys

try:
    from colorama import Fore, Back, Style
except:
    print("\033[96mУстановка необходимого ПО.\033[0m")
    pip.main(['install', 'colorama'])
    from colorama import Fore, Back, Style
    print('\n')


def int_input(input_suggestion='', more=float('-inf'), less=float('inf'), console_colour=Fore.RESET,
              error_message='Неверный формат числа\n', error_message_colour=Fore.RED,
              input_is_less_error="Число меньше допустимого\n", input_is_more_error="Число больше допустимого\n",
              input_is_less_error_colour=None, input_is_more_error_colour=None):
    if input_is_less_error_colour is None:
        input_is_less_error_colour = error_message_colour
    if input_is_more_error_colour is None:
        input_is_more_error_colour = error_message_colour
    while True:
        try:
            sys.stdout.write(input_suggestion)
            introduced = int(input().split()[0])
            if introduced <= more:
                sys.stdout.write(input_is_more_error_colour)
                sys.stdout.write('     \r')
                sys.stdout.write(input_is_more_error + console_colour)
            elif introduced >= less:
                sys.stdout.write(input_is_less_error_colour)
                sys.stdout.write('     \r')
                sys.stdout.write(input_is_less_error + console_colour)
            else:
                return introduced
        except:
            sys.stdout.write(error_message_colour)
            sys.stdout.write('     \r')
            sys.stdout.write(error_message + console_colour)


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
