from koinput import *
import Task_1
import Task_2
import Task_3
import Task_4
from colorama import Fore


if __name__ == '__main__':
    mn = Menu()
    mn.add_to_menu("Task 1", Task_1.main)
    mn.add_to_menu("Task 2", Task_2.main)
    mn.add_to_menu("Task 3", Task_3.main)
    mn.add_to_menu("Task 4", Task_4.main)
    mn.show_menu("\nMain menu", Fore.BLUE)
