


import tkinter as tk
from PIL import Image, ImageTk


class Mole:
    def __init__(self, cfg, hit, pos):
        self.canvas: tk.Canvas = cfg.canvas
        self.root = cfg.root
        self.tile_width = cfg.tile_width
        self.tile_height = cfg.tile_height
        self.hitted = hit
        self.pos = pos
        self.item = None
        self.hidden = False
        self.sprite = self.load_image("./assets/diglett.png")
    def hit(self, e):
        self.hitted()
        self.hide()
        self.root.after(2000, self.appear)
    def bind(self):
        self.canvas.tag_bind(self.item, "<Button-1>", self.hit)
        
    def hide(self):
        self.hidden = True
    def appear(self):
        self.hidden = False
    def load_image(self, image):
        self.canvas.update_idletasks()
        w, h = self.canvas.winfo_width(), self.canvas.winfo_height()
        w = w // 10
        h = h // 10

        img = Image.open(image)
        img = img.resize((w, h), Image.Resampling.NEAREST)
        return ImageTk.PhotoImage(img)

    def frame(self):
        pass

    def render(self):
        if self.item is not None:
            self.canvas.delete(self.item)
        
        if self.hidden:
            return
        
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        x, y = self.pos[0], self.pos[1]

        self.item = self.canvas.create_image(
            x, y, image=self.sprite, anchor="nw"
        )
        self.bind()
