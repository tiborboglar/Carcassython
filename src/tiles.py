# START WITH A MATRIX AND TRANSFORM IT INTO NODES LATER ON, SO WE CAN USE SEARCHES MORE EASILY

ROAD_TYPE_AMOUNT = {'A': 4, 'B': 9, 'C': 4}
CHURCH_TYPE_AMOUNT = {'A': 4, 'B': 2}
CASTLE_TYPE_AMOUNT = {'A': 3, 'B': 1, 'C': 3}


class Tile:
    def __init__(self, x, y, owner, rotation):
        """ Default class for all tiles
        :param x: Horizontal position of tile
        :param y: Vertical position of tile
        :param rotation: Anticlockwise rotation of the tile, 1 = none, 2 = 90º, 3 = 180º, 4 = 270º
        :param owner: Who placed a Meeple into the tile. None if no meeples

        :type x: int
        :type y: int
        :type rotation: int
        :type owner: int
        """
        self.x = x
        self.y = y
        self.rotation = rotation
        self.owner = owner  # not strictly necessary, tiles do not have owners


class Castle(Tile):
    def __init__(self, x, y, owner=-1, rotation=1, pennant=False):
        """ Default class for all tiles
        :param x: Horizontal position of tile
        :param y: Vertical position of tile
        :param rotation: Anticlockwise rotation of the tile, 1 = none, 2 = 90º, 3 = 180º, 4 = 270º
        :param owner: Who placed a Meeple into the tile. None if no meeples
        :param pennant: Whether the tile has a pennant counter

        :type x: int
        :type y: int
        :type rotation: int
        :type owner: int
        :type pennant: bool
        """
        super().__init__(x, y, owner, rotation)
        self.x = x
        self.y = y
        self.owner = owner
        self.rotation = rotation
        self.pennant = pennant


    def __repr__(self):
        return 'Castle'

# castle = Castle(pennant=False)
