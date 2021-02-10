import pip
from inputs_russian import int_input
z1 = __import__("Zadacha 1")
z2 = __import__("Zadacha 2")
z3 = __import__("Zadacha 3")
z4 = __import__("Zadacha 4")
try:
    from colorama import Fore, Back, Style
except:
    print("\033[96mУстановка необходимого ПО.\033[0m")
    pip.main(['install', 'colorama'])
    from colorama import Fore, Back, Style
    print('\n')


def menu():
    x = int_input(input_suggestion="Выберите задачу (1-4, 5 выход): ", greater=0, less=6)
    while x != 5:
        if x == 1:
            z1.main()
        elif x == 2:
            z2.main()
        elif x == 3:
            z3.main()
        else:
            z4.main()
        x = int_input(input_suggestion="Выберите задачу (1-4, 5 выход): ", greater=0, less=6)
    print("Для выхода нажмите любую клавишу...")
    input()


if __name__ == '__main__':
    menu()