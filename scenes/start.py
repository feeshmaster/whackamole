import tkinter as tk
from classes.keyboard_handler import KeyboardHandler
from pygame import mixer

mixer.init()
a_select = mixer.Sound("./assets/audio/select.wav")
a_smallSelect = mixer.Sound("./assets/audio/smallSelect.wav")


class Start:
    def __init__(self, root: tk.Tk, canvas: tk.Canvas, exit):
        self.canvas = canvas
        self.root = root
        self.keyboard_handler = KeyboardHandler(self.root)
        self.option = "Start"  # Start | Exit
        self.exit = exit
        self.bind_events()
        self.keyboard_handler.init_handler()
        self.canvas.update_idletasks()
        self.items = []
        self.render()
        self.fade_in(self.items)

    def render(self):
        canvas = self.canvas
        w, h = canvas.winfo_width(), canvas.winfo_height()
        if w <= 1:
            w = canvas.winfo_reqwidth()
        if h <= 1:
            h = canvas.winfo_reqheight()
        canvas.delete("all")

        deco = canvas.create_text(
            w // 2,
            h // 2 - 60,
            text=("Select an option:"),
            fill="white",
            font=("Whackamole", 30),
        )

        play = canvas.create_text(
            w // 2,
            h // 2 - 20,
            text=("> " if self.option == "Start" else "") + "Start",
            fill="white",
            font=("Whackamole", 24),
        )
        exit = canvas.create_text(
            w // 2,
            h // 2 + 20,
            text=("> " if self.option == "Exit" else "") + "Exit",
            fill="white",
            font=("Whackamole", 24),
        )
        self.items = [exit, play, deco]

    def select(self, e):  # only two so i can smoothly just reverse them
        a_smallSelect.play()
        if self.option == "Start":
            self.option = "Exit"
        else:
            self.option = "Start"
        self.render()

    def submit(self, event):
        a_select.play()
        self.fade_out(self.items)
        if self.option == "Exit":
            self.root.after(1000, self.root.destroy)
        else:
            self.unbind_events()
            self.root.after(1000, self.exit)

    def bind_events(self):
        self.keyboard_handler.bind("up", self.select)
        self.keyboard_handler.bind("down", self.select)
        self.keyboard_handler.bind("return", self.submit)

    def unbind_events(self):
        self.keyboard_handler.unbind_all()

    def fade_in(self, item_ids, step=0):
        steps = 20
        gray = round(255 * step / steps)
        color = f"#{gray:02x}{gray:02x}{gray:02x}"
        for item_id in item_ids:
            self.canvas.itemconfigure(item_id, fill=color)

        if step < steps:
            self.root.after(25, self.fade_in, item_ids, step + 1)

    def fade_out(self, item_ids, step=0):
        steps = 20
        gray = round(255 * (1 - step / steps))
        color = f"#{gray:02x}{gray:02x}{gray:02x}"
        for item_id in item_ids:
            self.canvas.itemconfigure(item_id, fill=color)

        if step < steps:
            self.root.after(50, self.fade_out, item_ids, step + 1)
