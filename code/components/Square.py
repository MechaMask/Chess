class Square ():
    def __init__(self, file, rank, color):
        self.position = (file,rank)
        self.color = color
    def get_file(self):
        return self.position[0]
    def get_rank(self):
        return self.position[1]
    def __str__(self):
        square = f"{self.get_file()}{self.get_rank()} {self.color}"
        return square
    
    