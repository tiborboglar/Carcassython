# Carcassython
Implementation of the Carcassonne game using Python, with Tkinter as GUI interface (to-do)

## Details

### Board

The board is a fixed `numpy array`, with shape (71, 71)

### Tiles
Each tile has an attribute named `connections` which is a list of size 4. Each element of this list represent a possible connection to the tile.

Suppose you have `connections = ['C', 'R', 'R', 'F']`, then your tile can connect to: Castle, Road, Road, Field

![connection_scheme](https://user-images.githubusercontent.com/25236592/108631076-857e4d80-7468-11eb-99dd-4ed1c5cb1041.png)


Since tiles can be rotated, where `rotation = 1` represents no rotation, `rotation = 2` represents 90º anti-clockwise rotation and so on.
The `connections` list will consider `rotation = 1` as reference frame. 

### Agent

### Scoring

### Monte Carlo Tree Search
