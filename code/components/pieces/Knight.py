from components.Piece import Piece

class Knight(Piece):
    def  __init__(self,color):
      self.color = color
      self.piece_type = "Knight"
    def display(self):
       return "N"