from Square import Square
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
    
    def get_square(self,position):
        file = position[0].upper()  
        rank = int(position[1]) 
        first_ind = rank - 1  
        second_ind = ord(file) - ord('A') 
        return self.board[first_ind][second_ind]

    def flip_board(self):
        if self.isflipped:
            self.isflipped = False
        else:
            self.isflipped = True 
        return self.isflipped
    
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
board = Board()
print(board)
board.flip_board()
print(board)


# board.board = [
#                [Square('A',1,"dark"),Square('B',1,"light"),Square('C',1,"dark"),Square('D',1,"light"),Square('E',1,"dark"),Square('F',1,"light"),Square('G',1,"dark"),Square('H',1,"light")],
#                [Square('A',2,"light"),Square('B',2,"dark"),Square('C',2,"light"),Square('D',2,"dark"),Square('E',2,"light"),Square('F',2,"dark"),Square('G',2,"light"),Square('H',2,"dark")],
#                [Square('A',3,"dark"),Square('B',3,"light"),Square('C',3,"dark"),Square('D',3,"light"),Square('E',3,"dark"),Square('F',3,"light"),Square('G',3,"dark"),Square('H',3,"light")],
#                [Square('A',4,"light"),Square('B',4,"dark"),Square('C',4,"light"),Square('D',4,"dark"),Square('E',4,"light"),Square('F',4,"dark"),Square('G',4,"light"),Square('H',4,"dark")],
#                [Square('A',5,"dark"),Square('B',5,"light"),Square('C',5,"dark"),Square('D',5,"light"),Square('E',5,"dark"),Square('F',5,"light"),Square('G',5,"dark"),Square('H',5,"light")],
#                [Square('A',6,"light"),Square('B',6,"dark"),Square('C',6,"light"),Square('D',6,"dark"),Square('E',6,"light"),Square('F',6,"dark"),Square('G',6,"light"),Square('H',6,"dark")],
#                [Square('A',7,"dark"),Square('B',7,"light"),Square('C',7,"dark"),Square('D',7,"light"),Square('E',7,"dark"),Square('F',7,"light"),Square('G',7,"dark"),Square('H',7,"light")],
#                [Square('A',8,"light"),Square('B',8,"dark"),Square('C',8,"light"),Square('D',8,"dark"),Square('E',8,"light"),Square('F',8,"dark"),Square('G',8,"light"),Square('H',8,"dark")]
#                ]
# print(board)
# print(board.flip_board())