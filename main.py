from window import *
from rock_paper_sisors import *
import tkinter as tk
import time


def start_game():
    num_rounds()



#Tab 1 functions
welcome()

rock_img_butt = tk.Button(game_tab, command=start_game, image=rock_img)
rock_img_butt.pack()



win.mainloop()