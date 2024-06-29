from components.Board import Board
# from components.pieces import Knight

from components.pieces import *



# Testing Code for Flip Board
# board = Board()
# print(board)
# board.flip_board()
# print(board)

#Testing code for initializing squares
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


# Testing Code for Square, move_piece, place_piece and flip_board
# print(f" E2 Square: {board.get_square("e2")}")
# board.flip_board()
# print("\nAdding and moving a Pawn: \n")
# board.get_square("e2").place_piece("Pawn")
# print(board)
# board.get_square("e2").move_piece(board.get_square("e4"))
# print(board)
# print("Moving a piece from a place that is there and a place it isn't: \n")
# board.flip_board()
# print(board)
# print(f"E2 Square: {board.get_square("e2")}")
# print(f"Piece on E2: {board.get_square("e2").get_piece()}")
# print(f"Moving a piece from E2: {board.get_square("e2").move_piece(board.get_square("e3"))}")
# print(f"E4 Square: {board.get_square("e4")}")
# print(f"Piece on E4: {board.get_square("e4").get_piece()}")
# print(f"\nMoving a piece from E4:\n")
# print(board)
# board.get_square("e4").move_piece(board.get_square("e5"))
# print(f"E4 Square: {board.get_square("e4")}")
# print(f"Piece on E4: {board.get_square("e4").get_piece()}")
# print(f"E5 Square: {board.get_square("e5")}")
# print(f"Piece on E5: {board.get_square("e5").get_piece()}")


board = Board()
print(board)
print(f"Piece on A2: {board.get_square("B1")}")
# board.flip_board()
k = Knight("White")
print(f"Created a knight: {k}")
b1 = board.get_square("B1")
board.place_piece(k,b1)
print(f"Piece on B1: {board.get_square("B1").get_piece()}")
print(board)
board.display()

for i in range(8):
    letter = chr(i + ord('A'))
    board.place_piece(Pawn("White"),board.get_square(f"{letter}2"))
    board.place_piece(Pawn("Black"),board.get_square(f"{letter}7"))

board.place_piece(Knight("White"),board.get_square("G1"))
board.place_piece(Knight("Black"),board.get_square("B8"))
board.place_piece(Knight("Black"),board.get_square("G8"))

board.place_piece(Rook("White"),board.get_square("A1"))
board.place_piece(Rook("White"),board.get_square("H1"))
board.place_piece(Rook("Black"),board.get_square("A8"))
board.place_piece(Rook("Black"),board.get_square("H8"))

board.place_piece(Bishop("White"),board.get_square("C1"))
board.place_piece(Bishop("White"),board.get_square("F1"))
board.place_piece(Bishop("Black"),board.get_square("C8"))
board.place_piece(Bishop("Black"),board.get_square("F8"))

board.place_piece(Queen("White"),board.get_square("D1"))
board.place_piece(King("White"),board.get_square("E1"))
board.place_piece(Queen("Black"),board.get_square("D8"))
board.place_piece(King("Black"),board.get_square("E8"))


print(board)
board.display()
# print(f"White light square bishop: Color {board.get_square("F1").color}, Square {str(board.get_square("F1"))}")
# print(f"White dark square bishop: Color {board.get_square("C1").color}, Square {str(board.get_square("C1"))}")
# print(f"Black light square bishop: Color {board.get_square("C8").color}, Square {str(board.get_square("C8"))}")
# print(f"Black dark square bishop: Color {board.get_square("f8").color}, Square {str(board.get_square("F8"))}")
# print(f"White King: Color {board.get_square("E1").color}, Square {str(board.get_square("E1"))}")
# print(f"Black King: Color {board.get_square("E8").color}, Square {str(board.get_square("E8"))}")



# Testing out bit representations of the board
# https://www.chessprogramming.org/Board_Representation
# https://mayothi.com/nagaskakichess6.html 
# c = bin(2**64)
# c = bin(2**64 << 1)
# inputA = int('0101',2)
# print ("After shifting in binary: " + bin(inputA << 1))
# print ("After shifting in binary: " + bin(inputA << 1)
# print("After shifting in decimal: " + str(inputA << 1))
# bin(int('0b101',2) ^ int('0b010',2))
# bin(int('0b101',2) & int('0b010',2))
# chess =bin(1 << 64)
# a = int('0x000000000000ff00',16)
# b=  int('0xffffffffffffffff',16)
# bin(a & b)[2:].zfill(64)
# bin(~a & b)[2:].zfill(64)
# c = bin(2**64 | int('1111111111111',2))

