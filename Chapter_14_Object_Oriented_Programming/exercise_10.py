"""
(a) Write a class called Connect4 that implements the logic of a Connect4 game. Use the
Tic_tac_toe class from this chapter as a starting point.
(b) Use the Connect4 class to create a simple text-based version of the game.
"""


class Connect4:
    def __init__(self):
        self.B = [[0, 0, 0, 0],
                  [0, 0, 0, 0],
                  [0, 0, 0, 0],
                  [0, 0, 0, 0]]

        self.player = 1

    def get_open_spots(self):
        return [[r, c] for r in range(4) for c in range(4)
                if self.B[r][c] == 0]

    def is_valid_move(self, r, c):
        # Checks if there are an entry under current move
        if r == 3:
            pass
        elif self.B[r+1][c] == 0:
            return False
        if 3 >= r >= 0 == self.B[r][c] and 0 <= c <= 3:
            return True
        return False

    def make_move(self, r, c):
        if self.is_valid_move(r, c):
            self.B[r][c] = self.player

        self.player = self.player % 2 + 1

    def check_for_winner(self):
        for c in range(4):
            if self.B[0][c] == self.B[1][c] == self.B[2][c] == self.B[3][c] != 0:
                return self.B[0][c]
        for r in range(3):
            if self.B[r][0] == self.B[r][1] == self.B[r][2] == self.B[r][3] != 0:
                return self.B[r][0]
        if self.B[0][0] == self.B[1][1] == self.B[2][2] == self.B[3][3] != 0:
            return self.B[0][0]
        if self.B[3][0] == self.B[2][1] == self.B[1][2] == self.B[0][3] != 0:
            return self.B[3][0]
        if not self.get_open_spots():
            return 0
        return -1


def print_board():
    chars = ['-', 'R', 'B']

    for row in range(4):
        for col in range(4):
            print(chars[game.B[row][col]], end=' ')
        print()


game = Connect4()
while game.check_for_winner() == -1:
    print_board()
    r, c = eval(input('Enter spot, player ' + str(game.player) + ': '))
    game.make_move(r, c)

print_board()
x = game.check_for_winner()
if x == 0:
    print("It's a draw.")
else:
    print('Player', x, 'wins!')
