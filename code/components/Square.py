class Square ():
    def __init__(self, file, rank, color):
        self.position = (file,rank)
        self.color = color
        self.occupied = False
        self.piece = None
    def get_piece(self):
        if self.occupied:
            return self.piece
    #TODO Move this to Player
    # def move_piece(self,target_square):
    #     if self.occupied:
    #         target_square.place_piece(self.container.pop())
    #         self.occupied = False
    def get_file(self,notate=False):
        if notate:
            return self.position[0]
        else:
            return ord(self.position[0]) - ord('A')
    def get_rank(self,notate=False):
        if notate:
            return self.position[1]
        else:
           return self.position[1]-1
    def display(self):
        square = f"{"  .  " if not self.occupied else self.get_piece().display()}"
        return square
    def __str__(self):
        square = f"{self.get_file(True)}{self.get_rank(True)} {self.color if not self.occupied else self.get_piece()}"
        return square

#TODO Make these two functions inverse of one another, and give option to retrunt get one of the two    
def notate(file_position,rank_position):
    file_notation =  chr(file_position + ord('A'))
    rank_notation = rank_position + 1
    return file_notation,rank_notation

def get_coords(file_notation,rank_notation):
    file_position = ord(file_notation.upper()) - ord('A')
    rank_position = rank_notation-1
    return (file_position,rank_position)
