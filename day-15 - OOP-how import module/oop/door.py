class Door:

    size = 0
    color = ''

    def __init__(self, size, color):
        self.size = size
        self.color = color

    def get_color(self):
        return self.color

    def get_size(self):
        return self.size
