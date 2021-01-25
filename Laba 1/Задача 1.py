# Ход слона. Шахматный слон ходит по диагонали. Даны две различные клетки шахматной доски, определите, может ли
# слон попасть с первой клетки на вторую одним ходом.

# Ввод

vvod_neveren = True
while vvod_neveren:
    print("Введите клетку на которой находится слон в формате БукваЧисло (E2): ", end='')
    nachalo = input().lower().split()[0]  # очищаем от мишуры
    try:
        if not nachalo[0].isalpha() or not nachalo[1::].isnumeric():
            print("Неверный формат")
        else:
            nachalo = [ord(nachalo[0]) - 96, int(nachalo[1::])]
            if nachalo[0] < 1 or nachalo[0] > 8 or nachalo[1] < 1 or nachalo[1] > 8:
                print('Клетка вне доски')
            else:
                vvod_neveren = False
    except Exception as e:
        print("Неверный формат")

vvod_neveren = True
while vvod_neveren:
    print("Введите клетку на которой будет находится слон в формате БукваЧисло (E2): ", end='')
    konec = input().lower().split()[0]
    print()
    try:
        if not konec[0].isalpha() or not konec[1::].isnumeric():
            print("Неверный формат")
        else:
            konec = [ord(konec[0]) - 96, int(konec[1::])]
            if konec[0] < 1 or konec[0] > 8 or konec[1] < 1 or konec[1] > 8:
                print('Клетка вне доски')
            else:
                vvod_neveren = False
    except Exception as e:
        print("Неверный формат")

if (nachalo[0] + 2 == konec[0] and nachalo[1] + 1 == konec[1]) or \
        (nachalo[0] + 2 == konec[0] and nachalo[1] - 1 == konec[1]) or \
        (nachalo[0] - 2 == konec[0] and nachalo[1] + 1 == konec[1]) or \
        (nachalo[0] - 2 == konec[0] and nachalo[1] - 1 == konec[1]) or \
        (nachalo[1] + 2 == konec[1] and nachalo[0] + 1 == konec[0]) or \
        (nachalo[1] + 2 == konec[1] and nachalo[0] - 1 == konec[0]) or \
        (nachalo[1] - 2 == konec[1] and nachalo[0] + 1 == konec[0]) or \
        (nachalo[1] - 2 == konec[1] and nachalo[0] - 1 == konec[0]):
    print("Ход возможен")
else:
    print('Ход невозможен')
