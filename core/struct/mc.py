import pickle


class MainCharacter:
    def __init__(self):
        """
        Class to hold character information
        """
        # Main character attributes
        self.name = None
        self.p1 = None
        self.p1_is = None
        self.p2 = None
        self.p3 = None

    def new_game(self, name, p1, p1_is, p2, p3):
        """
        Start new game
        :param name: Toon name
        :param p1: Subject pronoun
        :param p1_is: Subject pronoun verb
        :param p2: Possessive pronoun
        :param p3: Object pronoun
        :return: 
        """
        self.name = name
        self.p1 = p1
        self.p1_is = p1_is
        self.p2 = p2
        self.p3 = p3

    def load_game(self, choice):
        """
        Load game from file
        :param choice: name of selected toon
        :return:
        """
        with open(f'assets/character/{choice}', 'rb') as f:
            self.__dict__ = pickle.load(f)
            f.close()

    def save(self):
        """
        Save game to file
        :return:
        """
        with open(f'assets/character/toon_{self.name}.pickle', 'wb') as f:
            pickle.dump(self.__dict__, f)
            f.close()
