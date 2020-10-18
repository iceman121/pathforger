#! /usr/bin/env python
import core.startup.check_dep  # noqa
from core.session.game_start import start_game
from core.session.char_create.whoyou import ask


def main():
    start_game()
    ask()


if __name__ == '__main__':
    main()
