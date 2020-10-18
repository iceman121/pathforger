import pyfiglet
import os
import ctypes
import msvcrt
import subprocess
from ctypes import wintypes
from core.struct.mc import MainCharacter
from core.session.whoyou import ask

kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)
user32 = ctypes.WinDLL('user32', use_last_error=True)

SW_MAXIMIZE = 3

kernel32.GetConsoleWindow.restype = wintypes.HWND
kernel32.GetLargestConsoleWindowSize.restype = wintypes._COORD  # noqa
kernel32.GetLargestConsoleWindowSize.argtypes = (wintypes.HANDLE,)
user32.ShowWindow.argtypes = (wintypes.HWND, ctypes.c_int)


def maximize_console(lines=None):
    """
    Method to maximize console
    :param lines: Max size in lines
    :return:
    """
    fd = os.open('CONOUT$', os.O_RDWR)
    try:
        hcon = msvcrt.get_osfhandle(fd)
        max_size = kernel32.GetLargestConsoleWindowSize(hcon)
        if max_size.X == 0 and max_size.Y == 0:
            raise ctypes.WinError(ctypes.get_last_error())
    finally:
        os.close(fd)
    cols = max_size.X
    hwnd = kernel32.GetConsoleWindow()
    if cols and hwnd:
        if lines is None:
            lines = max_size.Y
        else:
            lines = max(min(lines, 9999), max_size.Y)
        subprocess.check_call('mode.com con cols={} lines={}'.format(
                                cols, lines))
        user32.ShowWindow(hwnd, SW_MAXIMIZE)


def print_title():
    """
    Method to print title figlet
    :return:
    """
    result = pyfiglet.figlet_format('Pathforger', font='larry3d', width=100)
    print(result)


def main_scr():
    """
    Allow user to select new game or load game
    :return: choice- name of selected toon
    """
    main_sc = True
    choice = None
    start = None
    while main_sc:
        start = start_game()
        if int(start) == 1:
            # New game routes to create character
            main_sc = False
            choice = ask()
        elif int(start) == 2:
            # Load games routes to save selection
            main_sc = False
            choice = load_game()
        else:
            # Do it again
            print('Invalid choice! Choose again')

    return int(start), choice


def start_game():
    """
    Method to start
    :return: Choice selection for new game or load game
    """
    maximize_console()
    print_title()
    print('Do you want to start a new game (enter 1) or resume an ongoing game (enter 2)?')
    choice = input('||> ')
    print()
    return choice


def load_game():
    """
    Method to load game from file
    :return: Name of chosen character
    """
    print('Select game to load')
    saves = os.listdir('assets/character')
    count = 1
    # List all saves
    for s in saves:
        print(f'{count}. {s}')
        count += 1
    # Let user choose
    choice = input('||> ')
    choice = saves[int(choice) - 1]
    # TODO- Assert choice in list
    toon = MainCharacter()
    # Load game to class
    toon.load_game(choice)
    print()
    print(f'Your name is {toon.name}')
    print(f'Your pronouns are {toon.p1}/{toon.p2}/{toon.p3}')
    print()

    return toon
