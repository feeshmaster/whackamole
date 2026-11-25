import tkinter as tk
import random
import math
import time
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
        self.END_TIME = time.monotonic() + 15
        self.MAX_MOLES = 3
        self.SPAWN_DELAY = (1000, 3000)
        self.game_over = False

        self.posList = [
                        (2, 2), (4, 2), (6, 2),
                        (2, 4), (4, 4), (6, 4),
                        (2, 6), (4, 6), (6, 6)
                        ]

        self.moles = []
        self.cfg.moles = self.moles
        self.activeMoles = 0

        for i in range(3):
            self.attempt_mole_spawn()

        #Mole(self.cfg, self.mole_hit, (2*self.tile_width, 2*self.tile_height))

        self.render()
        self.frame()

        self.root.after(random.randint(*self.SPAWN_DELAY), self.spawn_loop)


    def spot_check(self):
        if self.activeMoles >= self.MAX_MOLES and self.game_over == False:
            print(self.activeMoles)
            return False
        
        pos = random.choice(self.posList)
        for mole in self.moles:
            if pos == mole.pos:
                print(pos, mole.pos)
                return False
        print(pos)
        return pos

    def attempt_mole_spawn(self):
        checkPos = self.spot_check()
        
        if checkPos != False:
            self.activeMoles += 1
            checkPos = (checkPos[0]*self.tile_width, checkPos[1]*self.tile_height)
            self.moles.append(Mole(self.cfg, self.mole_hit, checkPos))
        else:
            print("oops no spots found i guess")

    def spawn_loop(self):
        self.attempt_mole_spawn()
        self.root.after(random.randint(*self.SPAWN_DELAY), self.spawn_loop)

    def mole_hit(self, mole):
        if self.game_over:
            return
        self.moles.remove(mole)
        self.score += 1
        self.activeMoles -= 1
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

        remaining = max(0, math.ceil(self.END_TIME - time.monotonic()))

        if remaining <= 0:
            self.game_over =  True
            self.render()
            w, h = self.canvas.winfo_width(), self.canvas.winfo_height()
            self.canvas.create_text(
                w / 2, h / 2,
                text=f"GAME OVER\nScore: {self.score}",
                fill="white", font=("Whackamole", 48), justify="center",
            )
        
        self.root.after(20, self.frame)
