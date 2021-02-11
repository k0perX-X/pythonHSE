from random import randint
from koinput import int_input


def main():
    mas = [randint(0, 999) for i in range(int_input(input_suggestion="Введите размер массива: "))]
    print(F"Созданный массив:\n {mas}")
    combsort(mas)
    print(F"Отсортированный массив:\n {mas}")


def combsort(alist):
    alen = len(alist)
    gap = (alen * 10 // 13) if alen > 1 else 0
    while gap:
        if 8 < gap < 11:
            gap = 11
        swapped = False
        for i in range(alen - gap):
            if alist[i + gap] < alist[i]:
                alist[i], alist[i + gap] = alist[i + gap], alist[i]
                swapped = True
        gap = (gap * 10 // 13) or swapped


if __name__ == '__main__':
    main()
