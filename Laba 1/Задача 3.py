from random import uniform

vvod_neveren = True
while vvod_neveren:
    print('Введите количество проверок: ', end='')
    tochn = input().split()[0]  # очищаем от мишуры
    try:
        tochn = int(tochn)
        if tochn <= 0:
            print("Неверный формат")
            continue
        vvod_neveren = False
    except Exception as e:
        print("Неверный формат")

popad = 0
for i in range(tochn):
    x = uniform(0, 8)
    y = uniform(0, 8)
    if x > 1 and x < 5 and y < 4 and y > 3:
        continue
    elif y < 2:
        continue
    elif y > 2.5 * x + 2:
        continue
    elif y > -5 / 6 * x + 26 / 3:
        continue
    else:
        popad += 1

print(f'Приближенное значение площади равно {popad / tochn * 64}')
