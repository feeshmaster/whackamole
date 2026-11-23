import tkinter as tk


class KeyboardHandler:
    def __init__(self, root: tk.Tk | tk.Canvas):
        self.keys = {}
        self.pressed = {}
        self.root = root
        self.paused = False

    def bind(self, key, handler):
        self.keys[key.lower()] = handler
        self.pressed[key.lower()] = False

    def unbind_all(self):
        self.keys = {}  # dumb fix but doesnt matter for this game
        self.pressed = {}

    def reset_pressed(self):
        for key in self.pressed:
            self.pressed[key] = False

    def pause(self):
        self.paused = True

    def unpause(self):
        self.paused = False

    def handler(self, event):
        if self.paused:
            return
        key = event.keysym.lower()
        if key in self.keys:
            self.keys[key](event)
            self.pressed[key] = True

    def release_handler(self, event):
        if self.paused:
            return
        key = event.keysym.lower()
        if key in self.pressed:
            self.pressed[key] = False

    def init_handler(self):
        root = self.root
        root.bind_all("<KeyPress>", self.handler, add="+")
        root.bind_all("<KeyRelease>", self.release_handler, add="+")
