from koinput import Menu
from colorama import Fore
if __name__ != '__main__':
    __import__(f"{__name__}.Subtask_3")
    __import__(f"{__name__}.Subtask_5")
else:
    import Subtask_3
    import Subtask_5


mn = Menu()


def main():
    mn.add_to_menu("Subtask 3", Subtask_3.main)
    mn.add_to_menu("Subtask 5", Subtask_5.main)

    @mn.reassign_menu_exit()
    def menu_exit(exit_offer):
        def f():
            pass

        return f

    mn.show_menu("\nTask 2", Fore.BLUE)
