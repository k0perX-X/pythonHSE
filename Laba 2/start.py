import pip

try:
    import colorama
except:
    print("\033[96mУстановка необходимого ПО.\033[0m")
    pip.main(['install', 'colorama'])
    print('\n')
    import colorama
from inputs_russian import Menu

z1 = __import__("Zadacha 1")
z2 = __import__("Zadacha 2")
z3 = __import__("Zadacha 3")
z4 = __import__("Zadacha 4")

mn = Menu()


@mn.add_to_menu_dec('Задача 1')
def defz1():
    z1.main()


@mn.add_to_menu_dec('Задача 2')
def defz2():
    z2.main()


@mn.add_to_menu_dec('Задача 3')
def defz3():
    z3.main()


@mn.add_to_menu_dec('Задача 4')
def defz4():
    z4.main()


@mn.reassign_menu_exit()
def menu_exit(exit_offer):
    def f():
        print("Edited")
        print(exit_offer, end='')
        input()

    return f


if __name__ == '__main__':
    # mn.add_to_menu('Задача 1', defz1)
    # mn.add_to_menu('Задача 2', defz2)
    # mn.add_to_menu('Задача 3', defz3)
    # mn.add_to_menu('Задача 4', defz4)
    mn.show_menu(title='МЕНЮ', title_colour=colorama.Fore.BLUE)
