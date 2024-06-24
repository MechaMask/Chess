class Square ():
    def __init__(self, file, rank, color):
        self.position = (file,rank)
        self.color = color
        self.occupied = False
        self.container = []    
    def place_piece(self,chesspiece):
        self.container.append(chesspiece)
        self.occupied = True
        return self.occupied
    def get_piece(self):
        if self.occupied:
            return self.container[0]
    def move_piece(self,target_square):
        if self.occupied:
            target_square.place_piece(self.container.pop())
            self.occupied = False
    def get_file(self):
        return self.position[0]
    def get_rank(self):
        return self.position[1]
    def __str__(self):
        square = f"{self.get_file()}{self.get_rank()} {self.color if not self.occupied else self.get_piece()}"
        return square
    
    