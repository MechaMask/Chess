from components.Board import Board

# from components.pieces import *



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
print(f"Piece on A2: {board.get_square("A2")}")
board.flip_board()
print(board)

