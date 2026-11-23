import tkinter as tk
from pygame import mixer
# from scenes.selection import Selection
from classes.game import Game
from classes.config import Config
from scenes.start import Start
import ctypes
mixer.init()
# NOTE: dir starts in main.py root dir


# absolutely NO CLUE how to use this library so ill look into this later
# will load the ttf
FR_PRIVATE = 0x10
ctypes.windll.gdi32.AddFontResourceExW(r"./assets/Whackamole.ttf", FR_PRIVATE, 0)


root = tk.Tk()
root.title("Whackamole")
root.attributes("-fullscreen", True)
root.config(bg="black")
root.update_idletasks()

w, h = root.winfo_width(), root.winfo_height()

scale = min(w * 0.90, h * 0.90)
pad = min(w * 0.1, h * 0.1)

canvas = tk.Canvas(
    root,
    width=scale,
    height=scale,
    bg="black",
    highlightbackground="white",
    highlightcolor="white",
    highlightthickness=2,
)

canvas.pack(padx=pad, pady=pad)

cfg = Config({
    "root": root,
    "canvas": canvas
})
game = None
def start():
    global cfg, game
    game = Game(cfg)

Start(root, canvas, start)
# Selection(root, canvas, start)

root.mainloop()
