from components.Piece import Piece

class King(Piece):
    def  __init__(self,color):
      self.color = color
      self.piece_type = "King"
    def display(self):
       return "K"