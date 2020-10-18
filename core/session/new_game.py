import os
import json
import time
import logging

# File paths
QUOTES = 'assets/text/quotes.json'


def logging_parameters(name):
    # Logfile name
    logfile = f'assets/story/story_{name}.txt'

    # Setting logging parameters
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(message)s')

    # Logging in terminal
    hldr = logging.StreamHandler()
    hldr.setFormatter(formatter)
    hldr.terminator = ''
    logger.addHandler(hldr)

    # Logging in file
    fl_hdlr = logging.FileHandler(logfile)
    fl_hdlr.setFormatter(formatter)
    fl_hdlr.terminator = ''
    logger.addHandler(fl_hdlr)

    return logger


def print_quote():
    # Print out awesome start quote
    with open(QUOTES, 'r') as f:
        quotes = json.load(f)

    intro_quote = quotes['intro']
    logging.info('\n')
    for c in intro_quote:
        logging.info(c)
        time.sleep(.10)
    logging.info('\n')


def story_start(toon):
    # Clear screen
    os.system('cls')
    # Declare logging parameters
    logger = logging_parameters(toon.name)
    # Print intro quote
    print_quote()
