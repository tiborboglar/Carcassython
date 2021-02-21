import tkinter as tk
from PIL import ImageTk, Image

window = tk.Tk()

for i in range(3):
    for j in range(3):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1,
        )
        img = None
        if i==1 & j==1:
            img = ImageTk.PhotoImage(Image.open('../imgs/tiles/two_castles.PNG'))
        frame.grid(row=i, column=j)
        label = tk.Label(master=frame, text=f'{i}, {j}', image=img)
        label.pack()

window.mainloop()