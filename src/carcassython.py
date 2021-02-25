import numpy as np
import pandas as pd
from tiles import Castle

NUMBER_OF_PLAYER = 2  # currently not supporting more than 2 players
INITIAL_GRID = (3, 3)


class Carcassython:
    def __init__(self, num_of_players=2):
        self.num_of_players = num_of_players
        self.cur_board = np.full(shape=(3, 3), fill_value=np.nan, dtype=object)  # the board will start as a 3x3 grid but might expand
        self.cur_player = 0  # when player turn ends we add one to number of rounds and cur player is number_of_rounds%num_of_players
        self.number_of_rounds = 0
        self.available_tiles = {'road_A': 4, 'castle_A': 3, 'castle_B': 1, 'castle_C': 3}  # tiles yet to be bought

    def initialize_board(self):
        """ The initial board is going to be a 2d array"""
        # I could initialize the board as a 71x71 sparse matrix
        raise NotImplementedError

    def draw_tile(self):
        #todo: create a function to draw random tiles given availability
        # currently I am just testing with an arbitrary tile
        tile_type = 'castle_A'
        tile = Castle(x=-1, y=-1, rotation=1, owner=-1, castle_type=tile_type)
        return tile

    def place_tile(self, x, y, tile):
        # suppose it is a castle
        # tile = Castle(x, y, owner=None, pennant=False)
        # if self.can_connect(tile):
        #    self.cur_board[x, y] = tile
        # else:
        #    raise ValueError('The tiles cannot connect')
        self.__expand_board(x, y)

        tile.x, tile.y = x, y

        self.cur_board[x, y] = tile
        if self.can_connect(tile):
           print('heyho')
        else:
            raise ValueError('Tile placed incorrectly')
        return tile

    def __expand_board(self, x, y):
        """ pads the board when a tile is in the border """
        if x == 0 and y == 0:
            self.cur_board = np.pad(self.cur_board, ((1, 0), (1, 0)), 'constant', constant_values=np.nan)
        elif x == 0 and y == self.cur_board.shape[1] - 1:
            self.cur_board = np.pad(self.cur_board, ((1, 0), (0, 1)), 'constant', constant_values=np.nan)
        elif x == self.cur_board.shape[0] - 1 and y == 0:
            self.cur_board = np.pad(self.cur_board, ((0, 1), (1, 0)), 'constant', constant_values=np.nan)
        elif x == self.cur_board.shape[0] - 1 and y == self.cur_board.shape[1] - 1:
            self.cur_board = np.pad(self.cur_board, ((0, 1), (0, 1)), 'constant', constant_values=np.nan)
        elif x == 0:
            self.cur_board = np.pad(self.cur_board, ((1, 0), (0, 0)), 'constant', constant_values=np.nan)
        elif x == self.cur_board.shape[0] - 1:
            self.cur_board = np.pad(self.cur_board, ((0, 1), (0, 0)), 'constant', constant_values=np.nan)
        elif y == 0:
            self.cur_board = np.pad(self.cur_board, ((0, 0), (1, 0)), 'constant', constant_values=np.nan)
        elif y == self.cur_board.shape[1] - 1:
            self.cur_board = np.pad(self.cur_board, ((0, 0), (0, 1)), 'constant', constant_values=np.nan)
        else:
            return

    def can_connect(self, tile):
        """tells whether the connection is valid or not"""
        x, y = tile.x, tile.y

        neighbours = {'left': [], 'up': [], 'right': [], 'down': []}

        # Checking if neighbour tiles are not empty
        if ~pd.isnull(self.cur_board[x, y - 1]): #left
            neighbours['left'].append(self.cur_board[x, y - 1])
            tile.neighbours['left'].append(self.cur_board[x, y - 1])
        if ~pd.isnull(self.cur_board[x, y + 1]): #right
            neighbours['right'].append(self.cur_board[x, y + 1])
            tile.neighbours['right'].append(self.cur_board[x, y + 1])
        if ~pd.isnull(self.cur_board[x - 1, y]): #up
            neighbours['up'].append(self.cur_board[x - 1, y])
            tile.neighbours['up'].append(self.cur_board[x - 1, y])
        if ~pd.isnull(self.cur_board[x + 1, y]): #down
            neighbours['down'].append(self.cur_board[x + 1, y])
            tile.neighbours['down'].append(self.cur_board[x + 1, y])

        #todo: iteratively look the neighbours of all neighbours
        # in order to see if everything is complete

        return False

    def place_meeple(self, x, y, tile):
        # i dont think we need (x,y) here, since we
        # just played the tile and know its position
        raise NotImplementedError

    def update_game_state(self):
        raise NotImplementedError

    def view_board(self):
        print('- Current board visualization -')
        print(self.cur_board)


# debugging
game = Carcassython(num_of_players=2)
tile = game.draw_tile()
tile2 = game.draw_tile()
tile2.rotation = 3
game.cur_board = np.array([
    [np.nan, np.nan, tile2],
    [np.nan, tile, np.nan],
    [np.nan, np.nan, np.nan]
    ])

game.view_board()
print(tile.neighbours)
print('Connections available for the tile drawn:', tile.connections)

game.place_tile(1,2, tile)

#game.place_tile(1, 1, tile)
#game.view_board()
#game.place_tile(1, 2, tile)
#game.view_board()
