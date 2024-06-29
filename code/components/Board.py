from .Square import Square
import re
class Board:
    def __init__(self):
        #a1__position = (0,0)
        self.isflipped = False
        self.board  = self.generate_empty()

    def generate_start(self):
        board = []
        return board
        
    def generate_empty(self):
        number_of_rows=8
        number_of_columns=8
        board = []
      # A row is a rank. A board is stored from white's perspective
      # as [row1,row2,row3,..]  such that row1 has squares A1 to H1 
      #
      # A column is a file. Each file Changes within each row.
      # The board should look something like this [[A1,B1,C1,..],[[A2,B2,C2,..],...]]
        colors = ("dark","light")
        for rank_position in range(number_of_rows):
            rank_squares  = [] #row of squares in a chess board 
            color_switch = (0 + rank_position)%2
            for file_position in range(number_of_columns):
                file = chr(file_position + ord('A')) #get the letter (A-H) from file position (0-7)
                rank = rank_position + 1 
                color = colors[color_switch] 
                color_switch = (color_switch + 1)%2 #aleternate colors per file
                newsquare = Square(file,rank,color)
                rank_squares.append(newsquare)
            board.append(rank_squares)
        return board 
    
    def place_piece(self,piece, square):
        #TODO should be able to handle chess notation or passing a square
        if not square.occupied:
            square.occupied = True
            square.piece = piece

    def legal_moves(self):
        pass

    def get_square(self,square):
        #TODO implement this logic in Square class then use it to get the indecices using get_coords
        matched = re.search(r"[A-Ha-h]{1}[1-8]{1}",square)
        if matched and (len(square) == 2):    
            file = square[0].upper()  
            rank = int(square[1]) 
            first_ind = rank - 1  
            second_ind = ord(file) - ord('A') 
            return self.board[first_ind][second_ind]
    def flip_board(self):
        if self.isflipped:
            self.isflipped = False
        else:
            self.isflipped = True 
        return self.isflipped
    def display(self):
        grid = ""
        if (not self.isflipped):
            for row in reversed(self.board):
                row_squares = ""
                for square in row:   
                    row_squares += f"{square.display()}" 
                grid += f"{row_squares}\n" 
            print(grid)
        else:
            for row in self.board:
                row_squares = ""
                for square in reversed(row):
                    row_squares += f"{square.display()} "
                grid += f"{row_squares}\n"
            print(grid)                

    def __str__(self):
        grid = ""
        if (not self.isflipped):
            for row in reversed(self.board):
                row_squares = ""
                for square in row:   
                    row_squares += f"{str(square)} " 
                grid += f"{row_squares}\n" 
            return grid
        else:
            for row in self.board:
                row_squares = ""
                for square in reversed(row):
                    row_squares += f"{str(square)} "
                grid += f"{row_squares}\n"
            return grid                         
