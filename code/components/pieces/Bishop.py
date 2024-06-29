from components.Piece import Piece
class Bishop(Piece):
    def  __init__(self,color):
      self.color = color
      self.piece_type = "Bishop"
    def display(self):
       return "  B  "