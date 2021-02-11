import sys
import pip
from colorama import Fore


def int_input(input_suggestion='', greater=float('-inf'), less=float('inf'), console_colour=Fore.RESET,
              error_message='Неверный формат числа.\n', error_message_colour=Fore.RED,
              input_is_greater_than_less_error="Число больше допустимого.\n",
              input_is_less_than_greater_error="Число меньше допустимого.\n",
              input_is_less_error_colour=None, input_is_greater_error_colour=None,
              strictly_greater=True, strictly_less=True):
    if input_is_less_error_colour is None:
        input_is_less_error_colour = error_message_colour
    if input_is_greater_error_colour is None:
        input_is_greater_error_colour = error_message_colour
    while True:
        try:
            sys.stdout.write(input_suggestion)
            introduced = int(input().split()[0])
            if introduced <= greater and strictly_greater:
                sys.stdout.write(input_is_greater_error_colour)
                sys.stdout.write('     \r')
                sys.stdout.write(input_is_less_than_greater_error + console_colour)
            elif introduced < greater and not strictly_greater:
                sys.stdout.write(input_is_greater_error_colour)
                sys.stdout.write('     \r')
                sys.stdout.write(input_is_less_than_greater_error + console_colour)
            elif introduced >= less and strictly_less:
                sys.stdout.write(input_is_less_error_colour)
                sys.stdout.write('     \r')
                sys.stdout.write(input_is_greater_than_less_error + console_colour)
            elif introduced > less and not strictly_less:
                sys.stdout.write(input_is_less_error_colour)
                sys.stdout.write('     \r')
                sys.stdout.write(input_is_greater_than_less_error + console_colour)
            else:
                return introduced
        except:
            sys.stdout.write(error_message_colour)
            sys.stdout.write('     \r')
            sys.stdout.write(error_message + console_colour)


def float_input(input_suggestion='', greater=float('-inf'), less=float('inf'), console_colour=Fore.RESET,
                error_message='Неверный формат числа.\n', error_message_colour=Fore.RED,
                input_is_greater_than_less_error="Число больше допустимого.\n",
                input_is_less_than_greater_error="Число меньше допустимого.\n",
                input_is_less_error_colour=None, input_is_greater_error_colour=None,
                strictly_greater=True, strictly_less=True):
    if input_is_less_error_colour is None:
        input_is_less_error_colour = error_message_colour
    if input_is_greater_error_colour is None:
        input_is_greater_error_colour = error_message_colour
    while True:
        try:
            sys.stdout.write(input_suggestion)
            introduced = float(input().split()[0])
            if introduced <= greater and strictly_greater:
                sys.stdout.write(input_is_greater_error_colour)
                sys.stdout.write('     \r')
                sys.stdout.write(input_is_less_than_greater_error + console_colour)
            elif introduced < greater and not strictly_greater:
                sys.stdout.write(input_is_greater_error_colour)
                sys.stdout.write('     \r')
                sys.stdout.write(input_is_less_than_greater_error + console_colour)
            elif introduced >= less and strictly_less:
                sys.stdout.write(input_is_less_error_colour)
                sys.stdout.write('     \r')
                sys.stdout.write(input_is_greater_than_less_error + console_colour)
            elif introduced > less and not strictly_less:
                sys.stdout.write(input_is_less_error_colour)
                sys.stdout.write('     \r')
                sys.stdout.write(input_is_greater_than_less_error + console_colour)
            else:
                return introduced
        except:
            sys.stdout.write(error_message_colour)
            sys.stdout.write('     \r')
            sys.stdout.write(error_message + console_colour)


class Menu:
    items = {}

    def __init__(self):
        pass

    def add_to_menu(self, name, func, *args):
        self.items[name] = (func, args)

    def add_to_menu_dec(self, name, *args):
        def decorator(func):
            self.items[name] = (func, args)
            return func

        return decorator

    def menu_exit(self, exit_offer):
        def f():
            print(exit_offer, end='')
            input()

        return f

    def reassign_menu_exit(self):
        def decorator(func):
            self.menu_exit = func
            return func

        return decorator

    def show_menu(self, title=None, title_colour=None, number_of_leading_spaces_title=2, console_colour=Fore.RESET,
                  order_of_items=None, number_of_leading_spaces=4, separator='-',
                  input_suggestion='Выберите пункт меню: ', enable_menu_item_exit=True, menu_item_exit='Выход',
                  exit_offer='Нажмите Enter для выхода...'):
        if enable_menu_item_exit:
            self.add_to_menu(menu_item_exit, self.menu_exit(exit_offer))
        while True:
            # Title
            if title is not None:
                if title_colour is not None:
                    sys.stdout.write(title_colour)
                    sys.stdout.write('     \r')
                sys.stdout.write(' ' * number_of_leading_spaces_title + title + console_colour + '\n')

            # Menu
            number = 1
            if order_of_items is None:
                for name in list(self.items.keys()):
                    print(' ' * number_of_leading_spaces + f'{number} {separator} {name}')
                    number += 1
                x = int_input(input_suggestion=input_suggestion, greater=0, less=number)
                if x == number - 1:
                    enable_menu_item_exit = False
                item = self.items[list(self.items.keys())[x - 1]]
                item[0](*item[1])

            elif type(order_of_items) == tuple:
                for i in order_of_items:
                    print(' ' * number_of_leading_spaces + f'{number} {separator} {list(self.items.keys())[i]}')
                    number += 1
                x = int_input(input_suggestion=input_suggestion, greater=0, less=number)
                if x == number - 1:
                    enable_menu_item_exit = False
                item = self.items[list(self.items.keys())[order_of_items[x - 1]]]
                item[0](*item[1])

            else:
                raise TupleException('order_of_items is not tuple')

            if not enable_menu_item_exit:
                break


class TupleException(Exception):
    def __init__(self, message):
        self.message = message
