# import pickle


def enter_name():
    print("Name your character:")
    name = input("||>")
    print(f"Your name is {name}")
    print()


def enter_pronoun():
    print("Enter your character's pronouns:")
    print("___ is awesome")
    pronoun_subject = input("||>")
    print(f"Your selected pronoun is '{pronoun_subject} is awesome'")
    print()


def ask():
    enter_name()
    enter_pronoun()
