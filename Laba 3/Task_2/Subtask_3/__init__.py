import os


# 3.	Считать результаты игроков из файла results.txt  и вывести на экран лучшего игрока по количеству баллов.


def main():
    with open(os.path.dirname(os.path.abspath(__file__)) + "\\results.txt", 'r') as f:
        lines = [line.split() for line in f]
        while [] in lines:
            lines.remove([])
        print(max(lines, key=lambda x: x[1])[0], max(lines, key=lambda x: x[1])[1])