# Carcassython
Implementation of the Carcassonne game using Python, with Tkinter as GUI interface 

## Details

### Tiles
Each tile has an attribute named `connections` which is a list of size 4. Each element of this list represent a possible connection to the tile.

Suppose you have `connections = ['C', 'R', 'R', 'F']`, then your tile can connect to: Castle, Road, Road, Field



Since tiles can be rotated, where `rotation = 1` represents no rotation, `rotation = 2` represents 90º anti-clockwise rotation and so on.
The `connections` list will consider `rotation = 1` as reference frame. 
