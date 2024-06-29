from components.Piece import Piece
class Pawn(Piece):
    def  __init__(self,color):
      self.color = color
      self.piece_type = "Pawn"
    def display(self):
       return "  P  "