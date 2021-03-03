from colorama import Fore
import os


# 5.	Для каждого файла известно, с какими действиями можно к нему обращаться: запись W, чтение R, запуск X. В первой
# строке содержится число N — количество файлов содержащихся в данной файловой системе. В следующих N строчках
# содержатся имена файлов и допустимых с ними операций, разделенные пробелами. Далее указано число M — количество
# запросов к файлам. В последних M строках указан запрос вида Операция Файл. К одному и тому же файлу может быть
# применено любое количество запросов. Вам требуется восстановить контроль над правами доступа к файлам (ваша программа
# для каждого запроса должна будет возвращать OK если над файлом выполняется допустимая операция, или же Access denied,
# если операция недопустима.


i=0
def last_line(l):
    global i
    i += 1
    return l[i-1]


def main():
    lines = []
    with open(os.path.dirname(os.path.abspath(__file__)) + "\\operations.txt", 'r') as f:
        lines = [line.split() for line in f]
        # print(lines)
    files = {}
    n = int(last_line(lines)[0])
    for i in range(n):
        line = last_line(lines)
        files[line[0]] = list(map(str.upper, line[1:]))
    # print(files)
    m = int(last_line(lines)[0])
    for i in range(m):
        line = last_line(lines)
        if line[0] == 'read':
            if "R" in files[line[1]]:
                print(Fore.GREEN + "OK")
            else:
                print(Fore.RED + "Access denied")
        elif line[0] == 'write':
            if "W" in files[line[1]]:
                print(Fore.GREEN + "OK")
            else:
                print(Fore.RED + "Access denied")
        elif line[0] == 'run':
            if "X" in files[line[1]]:
                print(Fore.GREEN + "OK")
            else:
                print(Fore.RED + "Access denied")