





class Text:
    def __init__(self, canvas, x, y, size=10, initial=None, text_color="#000000", _before=""):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.size = size
        self.text = initial
        self.text_color = text_color
        self.id = None
        self._before = _before

        self.update()

    def update(self, value=None):
        if value:
            self.text = value
        if self.id:
            self.canvas.delete(self.id)
        self.id = self.canvas.create_text(
            self.x, self.y, text=str(self._before)+str(self.text), font=("Whackamole", self.size), fill=self.text_color, anchor="nw"
        )
