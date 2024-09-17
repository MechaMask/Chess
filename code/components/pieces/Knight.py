from components.Piece import Piece

class Knight(Piece):
    def  __init__(self,color):
      self.color = color
      self.piece_type = "Knight"
      self.relative_coordinates = [(-2, -1), (-2, +1), (+2, -1), (+2, +1), (-1, -2), (-1, +2), (+1, -2), (+1, +2)]
    def display(self):
       return "  N  "
    def moves(self, square):
       # relative_coordinates is the knight's list of differences for each possible move 
       starting_file = square.get_file() #get_file will return an integer value of the file A=0 H=7
       starting_rank = square.get_rank() #same with get_rank
       available_moves = []
       for x,y in self.relative_coordinates:
          new_file = starting_file + x
          new_rank= starting_rank + y
          square_name = f"{chr(new_file + ord('A'))}{new_rank+1}" 
          available_moves.append((square_name,new_file,new_rank))  
       return available_moves
      # output should return 
      # available_moves = [
      #     (file -2, rank -1),(file -2, rank +1),
      #     (file +2, rank -1),(file +2, rank +1),
      #     (file -1, rank -2),(file -1, rank +2),
      #     (file +1, rank -2),(file +1, rank +2)                     
      #   ]
               