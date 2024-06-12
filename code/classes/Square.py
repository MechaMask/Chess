class square ():
    def __init__(self, position_x, position_y, color):
        self.position = (position_x,position_y)
        self.color = color
    def __str__(self):
        # s = "."
        # if self.position[0]=='A' and self.position[1] == 1 and self.color == "light":
        s = ' ' + self.position[0] + str(self.position[1]) + self.color + ' '
        return s