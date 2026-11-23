import tkinter as tk
from PIL import Image, ImageTk


class Hammer:
    def __init__(self, cfg, hit):
        self.canvas: tk.Canvas = cfg.canvas
        self.root = cfg.root
        self.tile_width = cfg.tile_width
        self.tile_height = cfg.tile_height
        self.hit_after = hit
        self.pos = [0,0]
        self.item = None
        self.cframe = 0
        self.sprites = [self.load_image("./assets/hammer_idle.png"), self.load_image("./assets/hammer_hit.png")]
        self.bind_events()
    def hit(self, e):
        x, y = e.x, e.y

        self.cframe = 1
        self.hit_after(x, y)
        self.render()
        def reset():
            self.cframe = 0
            self.render()
        self.root.after(500, reset)
        
    def bind_events(self):
        self.canvas.bind("<Motion>", self.update_pos)
        self.canvas.bind("<Button-1>", self.hit)
    def update_pos(self, e):
        self.canvas.update_idletasks()
        x = e.x - (self.tile_width // 4)
        y = e.y - (self.tile_height // 4)
        self.pos = [x, y]
        self.render()

    def load_image(self, image):
        self.canvas.update_idletasks()
        w, h = self.canvas.winfo_width(), self.canvas.winfo_height()
        w = w // 16
        h = h // 16

        img = Image.open(image)
        img = img.resize((w, h), Image.Resampling.NEAREST)
        return ImageTk.PhotoImage(img)

    def frame(self):
        pass

    def render(self):
        if self.item is not None:
            self.canvas.delete(self.item)

        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        x = max(0, min(self.pos[0], canvas_width - self.tile_width))
        y = max(0, min(self.pos[1], canvas_height - self.tile_height))

        self.item = self.canvas.create_image(
            x, y, image=self.sprites[self.cframe], anchor="nw", state="disabled"
        )
        
