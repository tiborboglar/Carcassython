import numpy as np
import pandas as pd
from tiles import Castle

NUMBER_OF_PLAYER = 2  # currently not supporting more than 2 players
INITIAL_GRID = (5, 5)


class Carcassython:
    def __init__(self, num_of_players=2):
        self.num_of_players = num_of_players
        #todo: when game releases, change the initialization board to 71x71
        self.cur_board = np.full(shape=INITIAL_GRID, fill_value=np.nan, dtype=object)  # the board will start as a 3x3 grid but might expand
        self.cur_player = 0  # when player turn ends we add one to number of rounds and cur player is number_of_rounds%num_of_players
        self.number_of_rounds = 0
        self.available_tiles = {'road_A': 4, 'castle_A': 3, 'castle_B': 1, 'castle_C': 3}  # tiles yet to be bought

    def initialize_board(self):
        """ The initial board is going to be a 2d array"""
        # I could initialize the board as a 71x71 sparse matrix
        raise NotImplementedError

    def draw_tile(self, rotation):
        #todo: create a function to draw random tiles given availability
        # currently I am just testing with an arbitrary tile
        # remove rotation later on because players will be
        # able to rotate arbitrarily
        tile_type = 'castle_A'
        tile = Castle(x=-1, y=-1, rotation=rotation, owner=-1, castle_type=tile_type)
        return tile

    def place_tile(self, x, y, tile):
        # suppose it is a castle
        # tile = Castle(x, y, owner=None, pennant=False)
        # if self.can_connect(tile):
        #    self.cur_board[x, y] = tile
        # else:
        #    raise ValueError('The tiles cannot connect')
        tile.x, tile.y = x, y
        # self.__expand_board(x, y)

        if self.can_connect(tile):
           self.cur_board[x, y] = tile
        else:
            raise ValueError('Tile placed incorrectly')

        return tile


    # def __expand_board(self, x, y):
    #     #todo: return a flag to verify if the board was expanded
    #     # if it was, we have to adequate the (x,y) placement of the tile onto our new current board
    #     """ pads the board when a tile is in the border """
    #     if x == 0 and y == 0:
    #         self.cur_board = np.pad(self.cur_board, ((1, 0), (1, 0)), 'constant', constant_values=np.nan)
    #     elif x == 0 and y == self.cur_board.shape[1] - 1:
    #         self.cur_board = np.pad(self.cur_board, ((1, 0), (0, 1)), 'constant', constant_values=np.nan)
    #     elif x == self.cur_board.shape[0] - 1 and y == 0:
    #         self.cur_board = np.pad(self.cur_board, ((0, 1), (1, 0)), 'constant', constant_values=np.nan)
    #     elif x == self.cur_board.shape[0] - 1 and y == self.cur_board.shape[1] - 1:
    #         self.cur_board = np.pad(self.cur_board, ((0, 1), (0, 1)), 'constant', constant_values=np.nan)
    #     elif x == 0:
    #         self.cur_board = np.pad(self.cur_board, ((1, 0), (0, 0)), 'constant', constant_values=np.nan)
    #     elif x == self.cur_board.shape[0] - 1:
    #         self.cur_board = np.pad(self.cur_board, ((0, 1), (0, 0)), 'constant', constant_values=np.nan)
    #     elif y == 0:
    #         self.cur_board = np.pad(self.cur_board, ((0, 0), (1, 0)), 'constant', constant_values=np.nan)
    #     elif y == self.cur_board.shape[1] - 1:
    #         self.cur_board = np.pad(self.cur_board, ((0, 0), (0, 1)), 'constant', constant_values=np.nan)
    #     else:
    #         return

    def can_connect(self, tile):
        """tells whether the connection is valid or not"""
        x, y = tile.x, tile.y

        neighbours = {'left': [], 'up': [], 'right': [], 'down': []}

        # Check if current tile is empty
        if pd.notnull(self.cur_board[x,y]):
            return False
        # Checking if neighbour tiles are not empty
        num_of_neighbours = 0
        if pd.notnull(self.cur_board[x, y - 1]): #left
            neighbours['left'].append(self.cur_board[x, y - 1])
            tile.neighbours['left'].append(self.cur_board[x, y - 1])
            num_of_neighbours += 1
        if pd.notnull(self.cur_board[x, y + 1]): #right
            neighbours['right'].append(self.cur_board[x, y + 1])
            tile.neighbours['right'].append(self.cur_board[x, y + 1])
            num_of_neighbours += 1
        if pd.notnull(self.cur_board[x - 1, y]): #up
            neighbours['up'].append(self.cur_board[x - 1, y])
            tile.neighbours['up'].append(self.cur_board[x - 1, y])
            num_of_neighbours += 1
        if pd.notnull(self.cur_board[x + 1, y]): #down
            neighbours['down'].append(self.cur_board[x + 1, y])
            tile.neighbours['down'].append(self.cur_board[x + 1, y])
            num_of_neighbours += 1

        #todo: iteratively look the neighbours of all neighbours
        # in order to see if everything is complete
        num_of_connections = 0
        for direction in neighbours:
            direction_size = len(neighbours[direction])
            exist_neighbour = True if direction_size > 0 else False
            if direction == 'left' and exist_neighbour:
                if neighbours[direction][0].connections[3] == tile.connections[1]:
                    num_of_connections += 1
            if direction == 'up' and exist_neighbour:
                if neighbours[direction][0].connections[2] == tile.connections[0]:
                    num_of_connections += 1
            if direction == 'right' and exist_neighbour:
                if neighbours[direction][0].connections[1] == tile.connections[3]:
                    num_of_connections += 1
            if direction == 'down' and exist_neighbour:
                if neighbours[direction][0].connections[0] == tile.connections[2]:
                    num_of_connections += 1

        if num_of_connections ==  num_of_neighbours:
            return True
            # to implement the verification of closeness
            # for n in neighbours[direction]:


        return False

    def place_meeple(self, x, y, tile):
        # i dont think we need (x,y) here, since we
        # just played the tile and know its position
        raise NotImplementedError

    def update_game_state(self):
        raise NotImplementedError

    def view_board(self):
        print('- Current board visualization -')
        print(pd.DataFrame(self.cur_board))


# debugging
game = Carcassython(num_of_players=2)
game.view_board()
tile = game.draw_tile(rotation=1)
game.place_tile(1, 1, tile)
tile2 = game.draw_tile(rotation=2)
game.view_board()
game.place_tile(1, 2, tile2)
game.view_board()

game.place_tile(0, 2, tile2)
game.view_board()

game.place_tile(0,3, tile2)
