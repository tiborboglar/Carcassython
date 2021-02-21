import numpy as np
from tiles import Castle

NUMBER_OF_PLAYER = 2  # currently not supporting more than 2 players
INITIAL_GRID = (3, 3)


class Carcassython:
    def __init__(self, num_of_players=2):
        self.num_of_players = num_of_players
        self.cur_board = np.full(shape=(3, 3), fill_value=None)  # the board will start as a 3x3 grid but might expand
        self.cur_player = 0  # when player turn ends we add one to number of rounds and cur player is number_of_rounds%num_of_players
        self.number_of_rounds = 0
        self.available_tiles = {'road_A': 4, 'castle_A': 3, 'castle_B': 1, 'castle_C': 3}  # tiles yet to be bought

    def initialize_board(self):
        """ The initial board is going to be a 2d array"""
        raise NotImplementedError

    def add_tile(self, x, y):
        # suppose it is a castle
        castle = Castle(x, y, owner=None, pennant=False)
        self.cur_board[x, y] = castle
        return castle

    def update_game_state(self):
        raise NotImplementedError

    def view_board(self):
        print('- Current board visualization -')
        print(self.cur_board)


game = Carcassython()
game.view_board()
game.add_tile(1, 1)
game.view_board()
