import tkinter as tk
import random
import math
from PIL import Image, ImageTk
from pygame import mixer
from classes.hammer import Hammer
from classes.text import Text
from classes.mole import Mole

class Game:
    def __init__(self, cfg):
        self.root: tk.Tk = cfg.root
        self.canvas: tk.Canvas = cfg.canvas
        self.cfg = cfg

        

        self.tile_height = 1
        self.tile_width = 1
        self.world_size = 9
        self.setup_tiling()

        self.background = self.load_background("./assets/map.png")
        self.cfg.tile_width = self.tile_width
        self.cfg.tile_height = self.tile_height
        self.hammer = Hammer(self.cfg, self.hit)

        self.t_score = Text(self.canvas, 0, 0, 16, 0, _before="Score: ")
        self.score = 0

        self.moles = [
            Mole(self.cfg, self.mole_hit, (2*self.tile_width, 2*self.tile_height)), Mole(self.cfg, self.mole_hit, (4*self.tile_width, 2*self.tile_height)), Mole(self.cfg, self.mole_hit, (6*self.tile_width, 2*self.tile_height)), 
            Mole(self.cfg, self.mole_hit, (2*self.tile_width, 4*self.tile_height)), Mole(self.cfg, self.mole_hit, (4*self.tile_width, 4*self.tile_height)), Mole(self.cfg, self.mole_hit, (6*self.tile_width, 4*self.tile_height)), 
            Mole(self.cfg, self.mole_hit, (2*self.tile_width, 6*self.tile_height)), Mole(self.cfg, self.mole_hit, (4*self.tile_width, 6*self.tile_height)), Mole(self.cfg, self.mole_hit, (6*self.tile_width, 6*self.tile_height)), 
            ]

        self.render()
        self.frame()
    def mole_hit(self):
        self.score += 1
        self.t_score.update(self.score)
        
        
    def hit(self, x, y):
        return
        

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
        for mole in self.moles:
            mole.render()


        self.hammer.render()

    def frame(self):
        self.render()
        
        
        self.root.after(20, self.frame)
