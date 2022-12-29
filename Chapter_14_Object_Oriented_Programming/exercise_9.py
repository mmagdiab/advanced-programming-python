"""
Write a class called Rock_paper_scissors that implements the logic of the game Rock-paper-
scissors. For this game the user plays against the computer for a certain number of
rounds. Your class should have fields for how many rounds there will be, the current
round number, and the number of wins each player has. There should be methods for getting
the computer’s choice, finding the winner of a round, and checking to see if someone has won
the (entire) game. You may want more methods.
"""
from random import randint


class RockPaperScissors:
    actions = ['Rock', 'Paper', 'Scissors']
    
    def __init__(self, rounds):
        self.rounds = rounds
        self.current_round = 1
        self.player_wins = 0

    def computer_choice(self):
        choice = randint(0, 2)
        return choice
    
    def round_winner(self, player_choice, computer_choice):
        self.current_round += 1
        if player_choice > computer_choice or player_choice == 3 and computer_choice == 1:
            print('Round winner is player')
            self.player_wins += 1
        elif computer_choice > player_choice:
            print('Round winner is computer')

    def has_winner(self):
        if self.player_wins > self.rounds // 2:
            print('Player is the winner.')
            return True
        if self.current_round - 1 - self.player_wins > self.rounds // 2:
            print('Computer is the winner.')
            return True
        return False
