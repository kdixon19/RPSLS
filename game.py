from human import Human
from ai import AI
import random

class Game:
    def __init__(self) -> None:
        self.human_1 = Human('Player 1')
        self.human_2 = Human('Player 2')
        self.ai_1 = AI('AI 1')
        self.ai_2 = AI('AI 2')
        global gesture_list
        gesture_list = ['rock','paper','scissors','lizard','spock']

    def run_game(self):
        game_run = True
        while game_run == True:
            self.display_welcome()
            self.display_rules()
            player_count = int(self.determine_player_count())
            if player_count == 1:
                self.battle(self.human_1, self.ai_2)
            elif player_count == 2:
                self.battle(self.human_1, self.human_2)
            elif player_count == 3:
                self.battle(self.ai_1, self.ai_2)
            game_run = self.repeat_game()
        print('')
        print('Thanks for playing!')

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
    
    def random_integer(self):
        rand_int = random.randint(0,4)
        return rand_int
    
    def player_choice(self, player_1_choice, player_2_choice):
        if player_1_choice == 'rock':
            if player_2_choice == 'rock':
                return 3
            elif player_2_choice == 'paper':
                return 2
            elif player_2_choice == 'scissors':
                return 1
            elif player_2_choice == 'lizard':
                return 1
            elif player_2_choice == 'spock':
                return 2
        elif player_1_choice == 'paper':
            if player_2_choice == 'rock':
                return 1
            elif player_2_choice == 'paper':
                return 3
            elif player_2_choice == 'scissors':
                return 2
            elif player_2_choice == 'lizard':
                return 2
            elif player_2_choice == 'spock':
                return 1
        elif player_1_choice == 'scissors':
            if player_2_choice == 'rock':
                return 2
            elif player_2_choice == 'paper':
                return 1
            elif player_2_choice == 'scissors':
                return 3
            elif player_2_choice == 'lizard':
                return 1
            elif player_2_choice == 'spock':
                return 2
        elif player_1_choice == 'lizard':
            if player_2_choice == 'rock':
                return 2
            elif player_2_choice == 'paper':
                return 1
            elif player_2_choice == 'scissors':
                return 2
            elif player_2_choice == 'lizard':
                return 3
            elif player_2_choice == 'spock':
                return 1
        elif player_1_choice == 'spock':
            if player_2_choice == 'rock':
                return 1
            elif player_2_choice == 'paper':
                return 2
            elif player_2_choice == 'scissors':
                return 1
            elif player_2_choice == 'lizard':
                return 2
            elif player_2_choice == 'spock':
                return 3

    def battle(self, player_1, player_2):
        round_counter = 0
        win_counter_1 = 0
        win_counter_2 = 0
        while round_counter < 3:
            if player_1 == self.human_1:
                print("")
                print("Choose 0 for Rock")
                print("Choose 1 for Paper")
                print("Choose 2 for Scissors")
                print("Choose 3 for Lizard")
                print("Choose 4 for Spock")
                user_input = int(input("Which move would you like to do Player 1?: "))
                player_1_choice = gesture_list[user_input]
                print("")
                print(f'Player 1 has chosen {player_1_choice}')
            elif player_1 == self.ai_1:
                player_1_choice = gesture_list[self.random_integer()]
                print("")
                print(f'Player 1 has chosen {player_1_choice}')
            if player_2 == self.human_2:
                print("")
                print("Choose 0 for Rock")
                print("Choose 1 for Paper")
                print("Choose 2 for Scissors")
                print("Choose 3 for Lizard")
                print("Choose 4 for Spock")
                user_input_2 = int(input("Which move would you like to do Player 2?: "))
                player_2_choice = gesture_list[user_input_2]
                print("")
                print(f'Player 2 has chosen {player_2_choice}')
            elif player_2 == self.ai_2:
                player_2_choice = gesture_list[self.random_integer()]
                print("")
                print(f'Player 2 has chosen {player_2_choice}')
            winner = self.player_choice(player_1_choice, player_2_choice)
            self.determine_winner(winner)
            if winner == 1:
                win_counter_1 += 1
            elif winner == 2:
                win_counter_2 += 1
            round_counter += 1
        self.final_winner(win_counter_1,win_counter_2)

    def final_winner(self,win_counter_1, win_counter_2):
        if win_counter_1 > win_counter_2:
            print('Congratulations Player 1, you have won the game!')
        elif win_counter_1 < win_counter_2:
            print('Congratulations Player 2, you have won the game!')
        elif win_counter_1 == win_counter_2:
            print('We have a draw, you should play again!')

    def determine_winner(self, winner):
        if winner == 1:
            print("")
            print('Player 1 has won!')
        elif winner == 2:
            print("")
            print('Player 2 has won!')
        elif winner == 3:
            print('')
            print('Its a draw!')

    def repeat_game(self):
        user_input = input('Would you like to play again? (y/n): ')
        if user_input == 'y':
            return True
        elif user_input == 'n':
            return False
