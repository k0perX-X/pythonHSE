import math
from inputs_russian import int_input, float_input


def area_triangle(base, height):
    return 0.5 * base * height


def area_circle(radius):
    return math.pi * radius ** 2


def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def capitalize_string(s):
    ss = s.split()
    for word in ss:
        s = s.replace(word, capitalize_word(word))
    return s


def capitalize_word(word):
    return word[0].upper() + word[1::]


def main():
    x = int_input(input_suggestion="Выберите задание: ")
    if x == 1:
        print(area_triangle(float_input(input_suggestion='Введите основание треугольника: '),
                            float_input(input_suggestion='Введите высоту треугольника: ')))
    if x == 2:
        print(area_circle(float_input(input_suggestion='Введите радиус круга: ')))
    if x == 3:
        print(distance(float_input(input_suggestion='Введите X первой точки: '),
                       float_input(input_suggestion='Введите Y первой точки: '),
                       float_input(input_suggestion='Введите X второй точки: '),
                       float_input(input_suggestion='Введите Y второй точки: ')))
    if x == 4:
        print('Введите строку для изменения: ')
        print(capitalize_string(input()))


if __name__ == '__main__':
    main()
