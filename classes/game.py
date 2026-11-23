import tkinter as tk
import random
from PIL import Image, ImageTk
from pygame import mixer
from classes.hammer import Hammer
from classes.text import Text


class Game:
    def __init__(self, cfg):
        self.root = cfg.root
        self.canvas = cfg.canvas
        self.cfg = cfg

        

        self.tile_height = 1
        self.tile_width = 1
        self.world_size = 9
        self.setup_tiling()

        self.background = self.load_background("./assets/map.png")
        self.cfg.tile_width = self.tile_width
        self.cfg.tile_height = self.tile_height
        self.hammer = Hammer(self.cfg, self.hit)

        self.t_score = Text(self.canvas, 0, 0, 16, "Test")

        self.render()

    def hit(self, x, y):
        pass
    def load_image(self, w, h, image):
        img = Image.open(image)

        img = img.resize((w, h), Image.Resampling.NEAREST)
        return ImageTk.PhotoImage(img)

    def load_background(self, image):

        self.canvas.update_idletasks()
        w, h = self.canvas.winfo_width(), self.canvas.winfo_height()
        return self.load_image(w, h, image)

    def setup_tiling(self):
        self.canvas.update_idletasks()
        w,h = self.canvas.winfo_width(), self.canvas.winfo_height()
        self.tile_width = w / self.world_size
        self.tile_height = h / self.world_size

    def render(self):
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, image=self.background, anchor="nw")
        self.t_score.update()
        self.hammer.render()

    def frame(self):
        self.render()

        self.root.after(20, self.frame)
