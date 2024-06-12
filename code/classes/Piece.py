class Piece:
    def __init__(self,color,shape):
        self.color=color
        self.shape=shape
    def __str__(self):
        return str(self.color) + str(self.shape)
    