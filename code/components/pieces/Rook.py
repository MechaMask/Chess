from components.Piece import Piece

class Rook(Piece):
    def  __init__(self,color):
      self.color = color
      self.piece_type = "Rook"
    def display(self):
       return "  R  "