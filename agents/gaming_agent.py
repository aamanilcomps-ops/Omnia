python
import random
from .abstract_agent import AbstractAgent
class GamingAgent(AbstractAgent):
    def __init__(self):
        pass
    def process(self, input):
        if input["game"] == "rock_paper_scissors":
            return self.rock_paper_scissors()
        elif input["game"] == "tic_tac_toe":
            return self.tic_tac_toe()
    def rock_paper_scissors(self):
        choices = ["rock", "paper", "scissors"]
        return random.choice(choices)
    def tic_tac_toe(self):
        # simple tic tac toe implementation
        board = [" " for _ in range(9)]
        while True:
            print(" ".join(board[:3]))
            print(" ".join(board[3:6]))
            print(" ".join(board[6:]))
            move = input("Enter your move (1-9): ")
            board[int(move) - 1] = "X"
            if self.check_win(board):
                print("You win!")
                break
            move = random.choice([i for i, x in enumerate(board) if x == " "])
            board[move] = "O"
            if self.check_win(board):
                print("I win!")
                break
    def check_win(self, board):
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for condition in win_conditions:
            if board[condition[0]] == board[condition[1]] == board[condition[2]] != " ":
                return True
        return False
