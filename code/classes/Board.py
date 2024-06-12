import numpy as np
import Square 
class Board:
    BOARD_LENGTH = 8
    BOARD_WIDTH = 8
    def __init__(self,length=BOARD_LENGTH,width=BOARD_LENGTH):
        self.length = length
        self.width = width
        a1__position = (0,0)   
        self.board  = [] 
        # self.board = [x%2 for x in range(length)]  
        current_rank = 1
        current_file  = 'A'
        current_color = 'dark'
        for row in range(self.length):
            file  = []
            for column in range(self.width):
                newsquare = Square.square(current_file,current_rank,current_color)
                file.append(newsquare)
                current_rank =  current_rank + 1
                current_file = chr((ord(current_file.upper())+1 - 65) % 26 + 65)
                current_color = "dark" if current_color == "light" else "light"
                self.board.append(file)




        
      

    def __str__(self):
        grid = ""
        for row in (range(self.length)):
            for column in range(self.width):
                grid += str(self.board[row][column]) 
                if column == self.width-1:
                    grid += "\n"
        return grid
 

                

board = Board()

print(board)

