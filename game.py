from human import Human
from ai import AI

class Gesture:
    def __init__(self) -> None:
        gesture_list = ['rock','paper','scissors','lizard','spock']

class Game:
    def __init__(self) -> None:
        self.human = Human('Player 1')
        self.human = Human('Player 2')
        self.ai = AI('AI 1')
        self.ai = AI('AI 2')


    def run_game(self):
        self.display_welcome()
        self.display_rules()
    
    def display_welcome(self):
        print("")
        print("Welcome to Rock Paper Scissors Lizards Spock")
        print("")
        print("Each mach will be best out of 3 games")
        print("Use the Number keys to enter your selection")

    def display_rules(self):
        print("")
        print("")
        print("Here are the rules:")
        print("")
        print("Rock crushes Scissors")
        print("Scissors cuts Paper")
        print("Paper covers Rock")
        print("Rock crushes Lizard")
        print("Lizard poisons Spock")
        print("Spock smashes Scissors")
        print("Scissors decapitates Lizard")
        print("Lizard eats Paper")
        print("Paper disproves Spock")
        print("Spock vaporizes Rock")
        print("")
        print("")