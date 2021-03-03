from koinput import *
from colorama import Fore


# 3.	Во входной строке записана последовательность чисел через пробел. Для каждого числа выведите слово YES
# (в отдельной строке), если это число ранее встречалось в последовательности или NO, если не встречалось.


def main():
    l = int_input("Enter list: ", multiple_numbers_in_line=True)
    for i in range(len(l)):
        if l[i] in l[0:i]:
            print(Fore.GREEN + "YES ", end='')
        else:
            print(Fore.RED + "NO ", end='')
    print(Fore.RESET)
