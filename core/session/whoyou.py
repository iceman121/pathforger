from core.struct.mc import MainCharacter


def enter_name():
    """
    Enter your name
    :return: name
    """
    # Get name
    print("Name your character:")
    name = input("||>")
    print(f"Your name is {name}")
    print()
    return name


def enter_pronoun():
    """
    Enter your pronouns
    :return:
    """
    # Subject
    print("Enter your character's pronouns:")
    print()
    print("1. ___ is/are awesome")
    p1 = input("||> ").lower().strip()
    print("1a. Do you prefer 'is' or 'are'?")
    p1_is = input("||> ").lower().strip()
    print(f"Your selected pronoun is '{p1.title()} {p1_is} awesome'.")
    print()

    # Possessive
    print("2. ___ dog is awesome")
    p2 = input("||> ").lower().strip()
    print(f"Your selected pronoun is '{p2.title()} dog is awesome'.")
    print()

    # Object
    print("3. This awesome dog belongs to ___")
    p3 = input("||> ").lower().strip()
    print(f"Your selected pronoun is 'This awesome dog belongs to {p3}'.")
    print()
    return p1, p1_is, p2, p3


def ask():
    # Get name
    name = enter_name()
    # Get pronouns
    p1, p1_is, p2, p3 = enter_pronoun()

    # Save to class
    toon = MainCharacter()
    toon.new_game(name, p1, p1_is, p2, p3)

    # Save game
    toon.save()
    return toon
