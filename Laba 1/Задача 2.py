# В первый день спортсмен пробежал X километров, а затем он каждый день увеличивал пробег на 10% от предыдущего
# значения. По данному числу Y определите номер дня, на который пробег спортсмена составит не менее Y километров.

vvod_neveren = True
while vvod_neveren:
    print('Введите X: ', end='')
    x = input().split()[0]  # очищаем от мишуры
    try:
        x = float(x)
        if x == 0:
            print("Неверный формат")
            continue
        vvod_neveren = False
    except Exception as e:
        print("Неверный формат")

vvod_neveren = True
while vvod_neveren:
    print('Введите Y: ', end='')
    y = input().split()[0]  # очищаем от мишуры
    try:
        y = float(y)
        vvod_neveren = False
    except Exception as e:
        print("Неверный формат")

i = 0
while x < y:
    x = x * 1.1
    i += 1
if i == 0: i = 1
print(f'Пробег составит не менее Y на {i} день')
