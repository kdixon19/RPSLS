from human import Human
from ai import AI
from random import Random

class Game:
    def __init__(self) -> None:
        self.human_1 = Human('Player 1')
        self.human_2 = Human('Player 2')
        self.ai_1 = AI('AI 1')
        self.ai_2 = AI('AI 2')
        global gesture_list
        gesture_list = ['rock','paper','scissors','lizard','spock']


    def run_game(self):
        self.display_welcome()
        self.display_rules()
        player_count = self.determine_player_count
        if player_count == 1:
            self.battle(self.human_1, self.ai_1)

    
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
    
    def determine_player_count(self):
        user_input = input('How many players will be playing? [Enter 1, 2, or 3 for a suprise]: ')
        return user_input
    
    def player_move_choice(self):
        pass
    
    def random_integer(self):
        rand_int = Random.randint(0,4)
        return rand_int
    
    def determine_winner(self, player_1_choice, player_2_choice):
        if player_1_choice == 'rock':
            pass


    def battle(self, player_1, player_2):
        battle = True
        while battle == True:
            if player_1 == self.human_1:
                print("")
                print("Choose 0 for Rock")
                print("Choose 1 for Paper")
                print("Choose 2 for Scissors")
                print("Choose 3 for Lizard")
                print("Choose 4 for Spock")
                user_input = input("Which move would you like to do Player 1?: ")
                player_1_choice = gesture_list[user_input]
            elif player_1 == self.ai_1:
                player_1_choice = gesture_list[self.random_integer()]
            if player_2 == self.human_2:
                print("")
                print("Choose 0 for Rock")
                print("Choose 1 for Paper")
                print("Choose 2 for Scissors")
                print("Choose 3 for Lizard")
                print("Choose 4 for Spock")
                user_input_2 = input("Which move would you like to do Player 2?: ")
                player_2_choice = gesture_list[user_input_2]
            elif player_1 == self.ai_2:
                player_2_choice = gesture_list[self.random_integer()]
            