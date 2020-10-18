#! /usr/bin/env python
import core.startup.check_dep  # noqa
from core.session.game_start import main_scr
from core.session.new_game import story_start


def main():
    """
    Main execution
    :return:
    """
    # Start main screen
    start, choice = main_scr()
    if int(start) == 1:
        story_start()
    else:
        pass


if __name__ == '__main__':
    main()
