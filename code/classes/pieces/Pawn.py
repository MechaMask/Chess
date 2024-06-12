from ..pieces import Piece
class Pawn(Piece):
    def __init__(self,color):
        self.color=color
        self.shape="pawn"