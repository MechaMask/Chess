from .Square import Square
import bitboard
import re
class Board:
    
    def __init__(self):
        self.isflipped = False
        self.full_board = bitboard.bitboard().fullboard()
        self.board = {"light" : self.light ,"dark":self.dark,}
        self.light,self.dark  = self.generate_start()
        self.occupied_squares = self.or_boards(*{**self.light,**self.dark}.values())
        
    def or_boards(self,*bitboards):
            res = bitboards[0]
            for board in bitboards[1:]:
                res.bits |=  board.bits
            return res
    def xor_boards(self,*bitboards):
            res = bitboards[0]
            for board in bitboards[1:]:
                res.bits ^=  board.bits
            return res
    def generate_start(self):
        light = {
            "pawns" : bitboard.bitboard(0x000000000000ff00),
            "rooks" : bitboard.bitboard(0x000000000000018),
            "knights" : bitboard.bitboard(0x000000000000042),
            "bishops":bitboard.bitboard(0x000000000000024),
            "queens": bitboard.bitboard(0x0000000000000008),
            "king": bitboard.bitboard(0x0000000000000010)}
        dark = {
            "pawns" : bitboard.bitboard(0x00ff000000000000),
            "rooks" : bitboard.bitboard(0x1800000000000000),
            "knights" : bitboard.bitboard(0x4200000000000000),
            "bishops":bitboard.bitboard(0x2400000000000000),
            "queens": bitboard.bitboard(0x0800000000000000),
            "king": bitboard.bitboard(0x1000000000000000)}
        
        return light, dark

    def generate_empty(self):
        light ={
            "pawns" : bitboard.bitboard(),
            "rooks" : bitboard.bitboard(),
            "knights" : bitboard.bitboard(),
            "bishops":bitboard.bitboard(),
            "queens": bitboard.bitboard(),
            "king": bitboard.bitboard()} 
        dark = {
            "pawns" : bitboard.bitboard(),
            "rooks" : bitboard.bitboard(),
            "knights" : bitboard.bitboard(),
            "bishops":bitboard.bitboard(),
            "queens": bitboard.bitboard(),
            "king": bitboard.bitboard()}
        return light, dark
    
    def legal_moves(self):
        pass
    def flip_board(self):
        if self.isflipped:
            self.isflipped = False
        else:
            self.isflipped = True 
        return self.isflipped   
    # def display(self):
    #     grid = ""
    #     if (not self.isflipped):
    #         for row in reversed(self.board):
    #             row_squares = ""
    #             for square in row:   
    #                 row_squares += f"{square.display()}" 
    #             grid += f"{row_squares}\n" 
    #         print(grid)
    #     else:
    #         for row in self.board:
    #             row_squares = ""
    #             for square in reversed(row):
    #                 row_squares += f"{square.display()} "
    #             grid += f"{row_squares}\n"
    #         print(grid)                

    # def __str__(self):
    #     grid = ""
    #     if (not self.isflipped):
    #         for row in reversed(self.board):
    #             row_squares = ""
    #             for square in row:   
    #                 row_squares += f"{str(square)} " 
    #             grid += f"{row_squares}\n" 
    #         return grid
    #     else:
    #         for row in self.board:
    #             row_squares = ""
    #             for square in reversed(row):
    #                 row_squares += f"{str(square)} "
    #             grid += f"{row_squares}\n"
    #         return grid                         
