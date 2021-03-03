import requests
from random import random
from pprint import pprint
from koinput import Menu, int_input, float_input
from colorama import Fore

mn1 = Menu()
mn2 = Menu()
films = {}
bool_exit = False


def make_dict_imdb():
    global films
    films = {}
    for element in requests.get("https://imdb-api.com/en/API/Top250Movies/k_yw45b9rb").json()['items']:
        films[element["title"]] = float(element["imDbRating"])


def make_dict_random():
    global films
    films = {}
    n = int_input('Enter the number of items: ', greater=0)
    for i in range(n):
        films[requests.post("https://randomall.ru/api/general/bookname",
                            json={'d': "pqvqtwpprpuwuiwbfjcjbvojsifjejg"}).json()] = round(random()*10, 1)


def manual_input():
    global films
    films = {}
    n = int_input('Enter the number of items: ', greater=0)
    for i in range(n):
        films[input('Enter the title of the movie: ')] = float_input("Enter movie rating: ", 0, 10,
                                                                     strictly_greater=False, strictly_less=False)


def print_dict():
    global films
    pprint(films, width=30)


def max_dict():
    global films
    m = max(films, key=lambda x: films[x])
    print(f"Maximum value: {m} {films[m]}")


def min_dint():
    global films
    m = min(films, key=lambda x: films[x])
    print(f"Minimum value: {m} {films[m]}")


def average_dict():
    global films
    print("Average value:", round(sum(films.values())/len(films), 2))


def delete_key():
    global films
    x = input("Enter the title of movie to be deleted: ")
    if x in films:
        del films[x]
    else:
        print(Fore.RED + "There is no such movie in the dictionary", Fore.RESET)


def special_print():
    global films
    d = [{'key': el, "value": films[el]} for el in films]
    pprint(d, width=30)
    d.sort(key=lambda x: x['value'])
    d.reverse()
    print(Fore.YELLOW, "Sorted", Fore.RESET)
    pprint(d, width=30)


def edit_element():
    global films
    x = input("Enter the title of movie to be edited: ")
    if x in films:
        films[x] = float_input("Enter movie rating: ", 0, 10, strictly_greater=False, strictly_less=False)
    else:
        print(Fore.RED + "There is no such movie in the dictionary", Fore.RESET)


def identical_elements():
    global films
    d = {}
    for k, v in films.items():
        if v not in d:
            d[v] = [k]
        else:
            d[v].append(k)
    tf = False
    for i in d:
        if len(d[i]) > 1:
            print(Fore.YELLOW + str(i) + Fore.RESET)
            for j in d[i]:
                print('  ' + j)
            tf = True
    if not tf:
        print("There are no identical meanings in the dictionary")


def exit_from_menu():
    global bool_exit
    bool_exit = True


def main():
    global bool_exit
    bool_exit = False
    mn1.add_to_menu("Make dict from top250 IMDb", make_dict_imdb)
    mn1.add_to_menu("Make random dict", make_dict_random)
    mn1.add_to_menu("Manual input", manual_input)
    mn1.add_to_menu("Exit", exit_from_menu)
    mn2.add_to_menu("Make dict from top250 IMDb", make_dict_imdb)
    mn2.add_to_menu("Make random dict", make_dict_random)
    mn2.add_to_menu("Manual input", manual_input)
    mn2.add_to_menu("Print dict", print_dict)
    mn2.add_to_menu("Maximum value", max_dict)
    mn2.add_to_menu("Minimum value", min_dint)
    mn2.add_to_menu("Average value", average_dict)
    mn2.add_to_menu("Delete element.", delete_key)
    mn2.add_to_menu("Edit element", edit_element)
    mn2.add_to_menu("Display in a special view.", special_print)
    mn2.add_to_menu('Find identical elements', identical_elements)
    mn2.add_to_menu("Exit", exit_from_menu)
    while not bool_exit:
        if films == {}:
            mn1.show_menu("\nTask 3", Fore.BLUE, enable_menu_item_exit=False)
        else:
            mn2.show_menu("\nTask 3", Fore.BLUE, enable_menu_item_exit=False)
