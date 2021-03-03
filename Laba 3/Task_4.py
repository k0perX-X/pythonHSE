import os
from sys import platform
from colorama import Fore
from koinput import Menu, int_input
import requests
from hashlib import md5
from pprint import pprint
import urllib3

mn = Menu()
login = 'admin'
password = 'admin'
urllib3.disable_warnings()


def start():
    if platform == "darwin":
        print(Fore.RED + "MacOS not supported" + Fore.RESET)
        return
    print("First you need to install https://github.com/k0perX-X/GRUB")
    x = input("Is the container already running? (y/n) (to exit, enter exit): ")
    if len(x.strip()) == 0:
        x = 'x'
    if x.strip()[0].lower() == 'exit':
        return
    while x.strip()[0].upper() != 'Y' and x.strip()[0].upper() != 'N' and x.strip()[0].lower() != 'exit':
        x = input("Is the container already running? (y/n) (to exit, enter exit): ")
        if len(x.strip()) == 0:
            x = 'x'
        if x.strip()[0].lower() == 'exit':
            return
    if x.strip()[0].upper() == 'N':
        c = 0
        x = input('Enter the name of the container: ')
        if platform == "linux" or platform == "linux2":
            c = os.system(f"sudo docker start {x}")
        elif platform == "win32":
            c = os.system(f"docker start {x}")
        while c != 0:
            x = input(F'{Fore.RED}An error has occurred!{Fore.RESET}\nEnter the name of the container: ')
            if platform == "linux" or platform == "linux2":
                c = os.system(f"sudo docker start {x}")
            elif platform == "win32":
                c = os.system(f"docker start {x}")


@mn.add_to_menu_dec("Add or edit flight")
def add_airplane():
    flight_id = input("Flight ID: ")
    airplane_id = input("Airplane ID: ")
    route = input("Route: ")
    take_off_time = input("Take off time: ")
    landing_time = input("Landing time: ")
    print(requests.post("https://localhost/add", verify=False,
                        json={
                            "login": login,
                            "password": md5(password.encode('utf32')).hexdigest(),
                            "database": "flights",
                            "values":
                                {
                                    flight_id: {
                                        "airplane id": airplane_id,
                                        "route": route,
                                        "take off time": take_off_time,
                                        "landing time": landing_time
                                    }
                                }
                        }).json())


@mn.add_to_menu_dec("Add or edit passenger")
def add_passenger():
    passenger_id = input("Passenger ID: ")
    passenger_name = input("Passenger name: ")
    history = []
    for i in range(int_input("Flight history size: ", -1)):
        history.append({})
        history[i]['ticket id'] = input("Ticket ID: ")
        history[i]['flight id'] = input('Flight ID: ')
    print(requests.post("https://localhost/add", verify=False,
                        json={
                            "login": login,
                            "password": md5(password.encode('utf32')).hexdigest(),
                            "database": "passengers",
                            "values":
                                {
                                    passenger_id: {
                                        "name": passenger_name,
                                        "history": history
                                    }
                                }
                        }).json())


def database_request(database: str) -> dict or None:
    j = requests.post("https://localhost/data", verify=False,
                      json={
                          "login": login,
                          "password": md5(password.encode('utf32')).hexdigest(),
                          "database": database
                      }).json()
    if j['status'] != 'ok':
        if j['status'] == 'error':
            print(Fore.RED + "Error: " + j['type error'] + Fore.RESET)
            return None
    return j['data']


def show_database(database):
    d = database_request(database)
    if d is not None:
        pprint(d)


mn.add_to_menu("Show flights database", show_database, 'flights')
mn.add_to_menu("Show passengers database", show_database, 'passengers')


def find_in_database(database):
    d = database_request(database)
    if d is not None:
        x = input("Enter ID: ")
        if x not in d:
            print(Fore.RED + f"This ID is not present in the {database} database." + Fore.RESET)
        else:
            pprint(d[x])


mn.add_to_menu("Find in flights database", find_in_database, 'flights')
mn.add_to_menu("Find in passengers database", find_in_database, 'passengers')


@mn.add_to_menu_dec("Finding errors in the Database")
def find_errors():
    f = database_request('flights')
    if f is None:
        return
    p = database_request('passengers')
    if p is None:
        return
    p_ids = [[h['flight id'], passenger_id] for passenger_id in p for h in p[passenger_id]['history']]
    for p_id in p_ids:
        if p_id[0] in f.keys():
            del f[p_id[0]]
            p_ids.remove(p_id)
    if p_ids != []:
        print(Fore.YELLOW + "Passengers with incorrect Flight IDs in history" + Fore.RESET)
        for p_id in p_ids:
            print(f"  ID: {p_id[1]} Name: {p[p_id[1]]}")
    if f != {}:
        print(Fore.YELLOW + "Flights without passengers" + Fore.RESET)
        for f_id in f:
            print(" ", f_id)


@mn.add_to_menu_dec("Set login and password")
def set_login():
    global login
    global password
    login = input("Login: ")
    password = input("Password: ")


@mn.reassign_menu_exit()
def exit_f(a):
    def f():
        pass

    return f


def main():
    start()
    mn.show_menu("\nTask 4", Fore.BLUE)
