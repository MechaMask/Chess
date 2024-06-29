from components.Piece import Piece

class Queen(Piece):
    def  __init__(self,color):
      self.color = color
      self.piece_type = "Queen"
    def display(self):
       return "  Q  "