import tkinter as tk
from PIL import ImageTk, Image
import os

print(os.getcwd())

TILE_IMG_DIR = r"../imgs/tiles/church.PNG"

window = tk.Tk()
img = ImageTk.PhotoImage(Image.open(TILE_IMG_DIR))
panel = tk.Label(window, image=img)
panel.pack(side='bottom', fill='both', expand='yes')

window.mainloop()
