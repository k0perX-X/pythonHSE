import math
from koinput import float_input, Menu
import colorama

menu = Menu()


@menu.add_to_menu_dec('Площадь треугольника')
def z1():
    def area_triangle(base, height):
        return 0.5 * base * height

    print(area_triangle(float_input(input_suggestion='Введите основание треугольника: '),
                        float_input(input_suggestion='Введите высоту треугольника: ')))


@menu.add_to_menu_dec('Площадь круга')
def z2():
    def area_circle(radius):
        return math.pi * radius ** 2

    print(area_circle(float_input(input_suggestion='Введите радиус круга: ')))


@menu.add_to_menu_dec('Расстояние от точки до точки')
def z3():
    def distance(x1, y1, x2, y2):
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    print(distance(float_input(input_suggestion='Введите X первой точки: '),
                   float_input(input_suggestion='Введите Y первой точки: '),
                   float_input(input_suggestion='Введите X второй точки: '),
                   float_input(input_suggestion='Введите Y второй точки: ')))


@menu.add_to_menu_dec('Capitalize')
def z4():
    def capitalize_word(word):
        return word[0].upper() + word[1::]

    def capitalize_string(s):
        ss = s.split()
        for word in ss:
            s = s.replace(word, capitalize_word(word))
        return s

    print('Введите строку для изменения: ')
    print(capitalize_string(input()))


@menu.reassign_menu_exit()
def f(a):
    def fu():
        pass

    return fu()


def main():
    menu.show_menu(title='МЕНЮ', title_colour=colorama.Fore.BLUE)


if __name__ == '__main__':
    main()
