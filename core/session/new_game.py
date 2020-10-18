import os
import json
import time

QUOTES = 'assets/text/quotes.json'


def print_quote():
    with open(QUOTES, 'r') as f:
        quotes = json.load(f)

    intro_quote = quotes['intro']
    print()
    for c in intro_quote:
        print(c, end='', flush=True)
        time.sleep(.25)
    print()


def story_start():
    os.system('cls')
    print_quote()
